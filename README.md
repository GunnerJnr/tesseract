# 📸 Interactive Image Cropper with OCR and HTML Output  

This Streamlit application enables users to upload an image, select a crop region, preprocess the image, and extract text using Tesseract OCR. The extracted text can be previewed, converted into HTML, and downloaded as `.txt` or `.html` files.

---

## **Features** 🚀

- **Image Upload**: Upload PNG, JPG, or JPEG files.
- **Image Preprocessing**:
  - Enhance Contrast
  - Convert to Grayscale
  - Apply Thresholding
  - Apply Blurring
- **Interactive Cropper**: Select any region of the uploaded image to crop.
- **OCR Text Extraction**: Extract text from the cropped image using Tesseract OCR.
- **HTML Output**: Convert extracted text into formatted HTML.
- **Download Options**: Save extracted text as `.txt` and HTML as `.html`.

---

## **Requirements**

- Python **3.8+**
- Tesseract OCR installed and configured.

### **System Requirements**

- **Linux**: `tesseract-ocr`  
- **macOS**: Install via Homebrew: `brew install tesseract`  
- **Windows**: Download and install Tesseract OCR:  
  [Tesseract for Windows](https://github.com/UB-Mannheim/tesseract/wiki)  

---

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/image-ocr-app.git
cd image-ocr-app
```

---

### **2. Install Python Dependencies**

1. Set up a virtual environment:

   - **Linux/macOS**:

     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

   - **Windows**:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

2. Install required packages:

```bash
pip install -r requirements.txt
```

---

### **3. Install Tesseract OCR**

Follow the instructions for your OS:

- **Linux**:

  ```bash
  sudo apt-get update
  sudo apt-get install tesseract-ocr
  ```

- **macOS**:

  ```bash
  brew install tesseract
  ```

- **Windows**:
  - Download the installer: [Tesseract for Windows](https://github.com/UB-Mannheim/tesseract/wiki).
  - Add the Tesseract executable path (e.g., `C:\Program Files\Tesseract-OCR`) to your system's environment variables.

---

### **4. Run the Application**

Start the Streamlit app:

```bash
streamlit run app.py
```

The app will launch in your browser at **[http://localhost:8501](http://localhost:8501)**.

---

## **Project Structure**

```plaintext
image-ocr-app/
├── app.py                # Main Streamlit application script
├── requirements.txt      # Python dependencies
├── packages.txt          # System-level dependencies for deployment
├── .streamlit/
│   └── config.toml       # Streamlit configuration file
├── .gitignore            # Ignore unnecessary files
└── README.md             # Project documentation
```

---

## **Deployment Instructions**

1. Push the repository to GitHub:

   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. Deploy on [Streamlit Community Cloud](https://share.streamlit.io/):

   - Sign in to Streamlit Community Cloud.
   - Connect your GitHub repository.
   - Set the **entry point** as `app.py`.
   - Ensure `packages.txt` includes `tesseract-ocr` for Linux support.

---

## **Usage Instructions**

1. **Upload an Image**:
   - Click the "Upload an Image" button to upload a PNG, JPG, or JPEG file.

2. **Preprocess the Image**:
   - Use the options in the sidebar to preprocess the image.

3. **Select the Region to Crop**:
   - Use the interactive cropper to select a region of interest.

4. **Perform OCR**:
   - View the extracted text in the "Extracted Text" section.
   - Convert the text into HTML format.

5. **Download Output**:
   - Download the extracted text as `.txt` or `.html`.

---

## **Troubleshooting**

- **Tesseract Not Found**:
  - Ensure Tesseract is installed and added to your system's PATH.
  - Verify the installation with:

    ```bash
    tesseract --version
    ```

- **Streamlit Deployment Issues**:
  - Ensure `packages.txt` contains `tesseract-ocr` for Linux environments.

---

## **Screenshots**

### **1. Application Interface**

![App Interface](path/to/screenshot1.png)

### **2. Text Extraction Output**

![Text Extraction](path/to/screenshot2.png)

---

## **Contributing**

Contributions are welcome! Fork the repository and submit a pull request with your changes.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Author**

- Developed by **[David Gunner (Jnr)]**
- Email: [davidgunner@gunnerjnr.uk](davidgunner@gunnerjnr.uk)
- GitHub: [https://github.com/gunnerjnr](https://github.com/gunnerjnr)
- Personal Website: [https://gunnerjnr.uk](https://gunnerjnr.uk)

---
