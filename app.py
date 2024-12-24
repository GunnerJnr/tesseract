import os
import re
import subprocess

import pytesseract
import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
from streamlit_cropper import st_cropper


# Function to dynamically find Tesseract executable
def find_tesseract():
    try:
        if os.name == "nt":  # For Windows
            tesseract_path = os.getenv("TESSERACT_CMD") or r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            if os.path.exists(tesseract_path):
                return tesseract_path
        else:  # For Linux and macOS
            tesseract_path = subprocess.check_output(["which", "tesseract"]).decode("utf-8").strip()
            return tesseract_path
    except Exception:
        st.error("Tesseract executable not found. Ensure Tesseract-OCR is installed.")
        return None

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = find_tesseract()

# Set page configuration to use full width
st.set_page_config(layout="wide")

# Inject custom CSS to clean up the appearance
st.markdown(
    """
    <style>
    div[data-testid="stImage"] {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to perform OCR on an image
def extract_text(image, psm_mode=3):
    config = f"--oem 3 --psm {psm_mode}"
    return pytesseract.image_to_string(image, config=config)

# Function to convert extracted text to HTML
def convert_text_to_html(text):
    paragraphs = re.split(r'\n\s*\n', text.strip())
    html_content = "<html>\n<body>\n"
    for paragraph in paragraphs:
        clean_paragraph = paragraph.replace("\n", " ")
        html_content += f"<p>{clean_paragraph}</p>\n"
    html_content += "</body>\n</html>"
    return html_content

# Streamlit app
st.title("Interactive Image Cropper with OCR and HTML Output 📰")

# Upload image
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Load the image
    image = Image.open(uploaded_file)

    # Sidebar options
    st.sidebar.header("Image Preprocessing Options")
    enhance_contrast = st.sidebar.checkbox("Enhance Contrast")
    apply_grayscale = st.sidebar.checkbox("Convert to Grayscale")
    apply_threshold = st.sidebar.checkbox("Apply Thresholding")
    apply_blur = st.sidebar.checkbox("Apply Blurring")

    # New Sidebar Cropper Enhancements
    st.sidebar.header("Cropping Options")
    realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
    box_colour = st.sidebar.color_picker(label="Crop Box Colour", value='#0000FF')
    aspect_choice = st.sidebar.radio(
        label="Aspect Ratio",
        options=["1:1", "16:9", "4:3", "2:3", "Free"],
        index=4  # Default to "Free"
    )
    aspect_dict = {
        "1:1": (1, 1),
        "16:9": (16, 9),
        "4:3": (4, 3),
        "2:3": (2, 3),
        "Free": None
    }
    aspect_ratio = aspect_dict[aspect_choice]

    # Apply preprocessing based on user selection
    processed_image = image.copy()
    if enhance_contrast:
        enhancer = ImageEnhance.Contrast(processed_image)
        processed_image = enhancer.enhance(2.0)
    if apply_grayscale:
        processed_image = processed_image.convert("L")
    if apply_threshold:
        processed_image = processed_image.convert("L").point(lambda x: 0 if x < 128 else 255, '1')
    if apply_blur:
        processed_image = processed_image.filter(ImageFilter.GaussianBlur(1))

    # Side-by-side comparison of uploaded and processed images
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)
    with col2:
        st.image(processed_image, caption="Processed Image", use_container_width=True)

    # Crop selection tool and cropped image preview side by side
    st.write("**Crop Selection and Preview:**")
    col_crop, col_preview = st.columns([1.5, 2.5])  # Adjusted to 60% cropper, 40% preview

    with col_crop:
        st.write("**Select the region to crop:**")
        cropped_image = st_cropper(
            processed_image,
            realtime_update=realtime_update,
            box_color=box_colour,  # Dynamically update crop box colour
            aspect_ratio=aspect_ratio,  # Dynamically update aspect ratio
            return_type='image',
            key=f"cropper-{box_colour}",  # Ensure a unique key for box colour updates
        )

    with col_preview:
        st.write("**Cropped Image Preview:**")
        st.image(cropped_image, caption="Cropped Image", use_container_width=True)

    # Perform OCR on the cropped image
    st.subheader("Extracted Text:")
    psm_mode = st.selectbox("Select OCR Page Segmentation Mode", [3, 4, 6, 11, 12])
    extracted_text = extract_text(cropped_image, psm_mode)
    st.text_area("Text from Cropped Region", extracted_text, height=200)

    # Convert extracted text to HTML
    html_output = convert_text_to_html(extracted_text)
    st.subheader("Generated HTML:")
    st.code(html_output, language="html")

    # Download options
    st.download_button(
        "Download Extracted Text",
        data=extracted_text,
        file_name="extracted_text.txt",
        mime="text/plain",
    )
    st.download_button(
        "Download HTML",
        data=html_output,
        file_name="extracted_output.html",
        mime="text/html",
    )
