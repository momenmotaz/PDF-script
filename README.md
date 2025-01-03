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

## 🌐 دليل الاستخدام بالعربي المصري

# 🚀 أدوات معالجة ملفات PDF

مجموعة سكريبتات بايثون بتساعدك تتعامل مع ملفات PDF، تقدر تقرا وتستخرج صفحات وتحول لنص.

## ✨ المميزات

### ١. قارئ PDF (pdf_reader.py)
بيقرا محتوى الـ PDF ويعرضه بشكل منظم على الشاشة.

**المميزات:**
- بيتعرف على النص في الصور (OCR)
- بيشتغل على ٤ صفحات في نفس الوقت عشان يخلص بسرعة
- بيطلع النص منظم في فقرات
- تقدر تختار الصفحات اللي عايزها
- جودة معالجة محسنة (150 DPI)

### ٢. مستخرج PDF (pdf_extractor.py)
بيطلع صفحات معينة من ملف PDF في ملف جديد.

**المميزات:**
- بيحافظ على جودة الملف الأصلي
- بيعمل الفولدرات اللي محتاجها لوحده
- تقدر تختار أي صفحات عايزها
- بيحافظ على شكل الـ PDF زي ما هو

### ٣. محول PDF لنص (pdf_to_text.py)
بيحول ملفات PDF لملفات نصية.

**المميزات:**
- بيتعرف على النص في الصور
- بيسمي الملفات لوحده بشكل منظم
- تقدر تختار الصفحات اللي عايزها
- بيحط الملفات في فولدرات منظمة

## 📋 المتطلبات

١. مكتبات بايثون (تقدر تنزلها كلها مرة واحدة بالأمر ده):
   ```bash
   pip install -r requirements.txt
   ```
   - PyPDF2 (نسخة ٣.٠.٠ أو أحدث)
   - pdf2image (نسخة ١.١٦.٣ أو أحدث)
   - pytesseract (نسخة ٠.٣.١٠ أو أحدث)
   - Pillow (نسخة ١٠.٠.٠ أو أحدث)

٢. برامج لازم تنزلها على جهازك:
   - برنامج Tesseract OCR للتعرف على النصوص
   - برنامج Poppler للتعامل مع الـ PDF

## 🛠️ التنزيل والإعداد

١. نزل الملفات على جهازك
٢. نزل مكتبات بايثون:
   ```bash
   pip install -r requirements.txt
   ```
٣. نزل البرامج المطلوبة:
   - نزل وسطب Tesseract OCR
   - نزل وسطب Poppler
٤. لو محتاج تغير المسارات في السكريبتات:
   ```python
   POPPLER_PATH = "مسار/فولدر/poppler/bin"
   TESSERACT_PATH = "مسار/برنامج/tesseract.exe"
   ```

## 📖 طريقة الاستخدام

### قارئ PDF
```bash
# الطريقة الأولى: تفاعلي
python pdf_reader.py

# الطريقة التانية: بالأوامر على طول
python pdf_reader.py [مسار_الملف] [صفحة_البداية] [صفحة_النهاية]

# مثال
python pdf_reader.py ./documents/book.pdf 1 5
```

### مستخرج PDF
```bash
# الطريقة الأولى: تفاعلي
python pdf_extractor.py

# الطريقة التانية: بالأوامر على طول
python pdf_extractor.py [مسار_المصدر] [صفحة_البداية] [صفحة_النهاية] [مسار_الناتج]

# مثال
python pdf_extractor.py ./book.pdf 10 15 ./output/chapter1.pdf
```

### محول PDF لنص
```bash
# الطريقة الأولى: تفاعلي
python pdf_to_text.py

# الطريقة التانية: بالأوامر على طول
python pdf_to_text.py [مسار_الملف] [صفحة_البداية] [صفحة_النهاية]

# مثال
python pdf_to_text.py ./document.pdf 1 10
```

## 📁 تنظيم الفولدرات
```
output/
├── pdfs/         # للملفات PDF اللي اتعملت
└── texts/        # للملفات النصية
```

## 🔍 أمثلة عملية

### ١. قراءة PDF
```bash
python pdf_reader.py ./lecs_pdf/Robotics.pdf 1 5
# النتيجة: هيعرض النص من صفحة ١ لـ ٥
```

### ٢. استخراج شابتر من PDF
```bash
python pdf_extractor.py ./AI_II.pdf 320 323 ./output/pdfs/AI_II_ch27.pdf
# النتيجة: هيعمل ملف PDF جديد فيه الصفحات من ٣٢٠ لـ ٣٢٣
```

### ٣. تحويل PDF لنص
```bash
python pdf_to_text.py ./Robotics.pdf 1 5
# النتيجة: هيعمل ملف نصي في فولدر output/texts/
```

## 📝 ملاحظات مهمة
- أرقام الصفحات بتبدأ من ١
- تقدر تستخدم مسارات نسبية أو كاملة
- لو مش هتحدد مسار للملفات الناتجة، هتتحفظ تلقائي في فولدر output
- سرعة المعالجة بتعتمد على إمكانيات جهازك

## 🤝 المساهمة في المشروع
تقدر تساعد في تطوير المشروع عن طريق:
١. الإبلاغ عن المشاكل
٢. اقتراح تحسينات
٣. عمل pull requests

## 📄 الترخيص
المشروع مفتوح المصدر ومتاح تحت رخصة MIT.
