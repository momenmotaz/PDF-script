# PDF Processing Tools

A collection of Python scripts for processing PDF files, including reading, extracting pages, and converting to text.

## 🚀 Features

### 1. PDF Reader (`pdf_reader.py`)
Reads PDF content and displays it in a formatted way on the console.

**Features:**
- OCR text recognition
- Parallel processing for faster execution
- Formatted output with paragraphs
- Support for page range selection
- Optimized image processing (150 DPI)

### 2. PDF Extractor (`pdf_extractor.py`)
Extracts specific pages from a PDF file into a new PDF file.

**Features:**
- Maintains original PDF quality
- Creates output directories automatically
- Supports page range selection
- Preserves original PDF formatting

### 3. PDF to Text (`pdf_to_text.py`)
Converts PDF files to text files using OCR.

**Features:**
- OCR text recognition
- Automatic file naming
- Support for page range selection
- Organized output directory structure

## 📋 Requirements

1. Python Libraries (install using `pip install -r requirements.txt`):
   - PyPDF2 (≥3.0.0)
   - pdf2image (≥1.16.3)
   - pytesseract (≥0.3.10)
   - Pillow (≥10.0.0)

2. System Dependencies:
   - [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
   - [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/)

## 🛠️ Installation

1. Clone or download this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install system dependencies:
   - Download and install Tesseract OCR
   - Download and install Poppler
4. Update paths in scripts if necessary:
   ```python
   POPPLER_PATH = "path/to/poppler/bin"
   TESSERACT_PATH = "path/to/tesseract.exe"
   ```

## 📖 Usage

### PDF Reader
```bash
# Method 1: Interactive
python pdf_reader.py

# Method 2: Command line arguments
python pdf_reader.py [input_pdf] [start_page] [end_page]

# Example
python pdf_reader.py ./documents/book.pdf 1 5
```

### PDF Extractor
```bash
# Method 1: Interactive
python pdf_extractor.py

# Method 2: Command line arguments
python pdf_extractor.py [input_pdf] [start_page] [end_page] [output_pdf]

# Example
python pdf_extractor.py ./book.pdf 10 15 ./output/chapter1.pdf
```

### PDF to Text
```bash
# Method 1: Interactive
python pdf_to_text.py

# Method 2: Command line arguments
python pdf_to_text.py [input_pdf] [start_page] [end_page]

# Example
python pdf_to_text.py ./document.pdf 1 10
```

## 📁 Output Directory Structure
```
output/
├── pdfs/         # For extracted PDF files
└── texts/        # For converted text files
```

## 🔍 Examples

### 1. Reading a PDF
```bash
python pdf_reader.py ./lecs_pdf/Robotics.pdf 1 5
# Output: Displays formatted text from pages 1-5
```

### 2. Extracting Chapter from PDF
```bash
python pdf_extractor.py ./AI_II.pdf 320 323 ./output/pdfs/AI_II_ch27.pdf
# Output: Creates a new PDF with pages 320-323
```

### 3. Converting PDF to Text
```bash
python pdf_to_text.py ./Robotics.pdf 1 5
# Output: Creates a text file in output/texts/
```

## 🌐 Arabic Usage Guide (دليل الاستخدام بالعربي)

### قارئ PDF
- يقرأ محتوى PDF ويعرضه بشكل منسق
- يدعم التعرف على النصوص باستخدام OCR
- يمكن تحديد نطاق الصفحات

### مستخرج PDF
- يستخرج صفحات محددة من ملف PDF
- يحتفظ بجودة الملف الأصلي
- ينشئ المجلدات تلقائياً

### محول PDF إلى نص
- يحول ملفات PDF إلى ملفات نصية
- يدعم التعرف على النصوص
- ينظم الملفات في مجلدات

## 📝 Notes
- Page numbers start from 1
- All scripts support both relative and absolute paths
- Output files are automatically saved in the output directory if no path is specified
- Processing speed depends on your system specifications

## 🤝 Contributing
Feel free to contribute to this project by:
1. Reporting bugs
2. Suggesting enhancements
3. Creating pull requests

## 📄 License
This project is open source and available under the MIT License.
