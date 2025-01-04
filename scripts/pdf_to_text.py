import pytesseract
from pdf2image import convert_from_path
import os

# Set paths for external tools
#غير الباث حسب جهازك
#change path for depend on your device
POPPLER_PATH = r"d:/momen fci 3/AI apps/lec/poppler/poppler-23.11.0/Library/bin"
TESSERACT_PATH = r"d:/momen fci 3/AI apps/lec/tesseract-ocr/tesseract.exe"

# Configure tesseract path
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def pdf_to_text(input_pdf, start_page=None, end_page=None, output_txt=None):
    """
    Convert PDF to text file using OCR.
    
    Args:
        input_pdf (str): Path to input PDF file
        start_page (int, optional): Start page number (1-based)
        end_page (int, optional): End page number
                                If None, will convert until the last page
        output_txt (str, optional): Path to save output text file
                                  If None, will create 'output/texts/<input_name>.txt'
    
    Returns:
        str: Path to output text file if successful, None otherwise
    """
    try:
        # Create output filename if not provided
        if output_txt is None:
            base_name = os.path.splitext(os.path.basename(input_pdf))[0]
            if start_page and end_page:
                output_txt = os.path.join("output", "texts", f"{base_name}_p{start_page}-{end_page}.txt")
            else:
                output_txt = os.path.join("output", "texts", f"{base_name}.txt")
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_txt), exist_ok=True)
        
        print("Converting PDF to images...")
        # Convert PDF to images
        images = convert_from_path(input_pdf, poppler_path=POPPLER_PATH)
        
        # Adjust page range
        if start_page is None:
            start_page = 1
        if end_page is None:
            end_page = len(images)
            
        # Validate page numbers
        if start_page < 1 or start_page > len(images):
            raise ValueError(f"Start page must be between 1 and {len(images)}")
        if end_page < start_page or end_page > len(images):
            raise ValueError(f"End page must be between {start_page} and {len(images)}")
        
        # Convert to 0-based index
        start_idx = start_page - 1
        end_idx = end_page - 1
        
        # Extract text from each page
        with open(output_txt, 'w', encoding='utf-8') as f:
            for i in range(start_idx, end_idx + 1):
                print(f"Processing page {i+1}/{end_page}...")
                
                # Extract text using Tesseract
                text = pytesseract.image_to_string(images[i], lang='eng')
                
                if text.strip():
                    # Write page number and content
                    f.write(f"\n=== Page {i+1} ===\n\n")
                    f.write(text.strip() + "\n")
        
        print(f"Successfully created: {output_txt}")
        return output_txt
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    # Get input from user
    input_pdf = input("Enter path to PDF file: ")
    
    # Page range is optional
    start_input = input("Enter start page number (press Enter for first page): ")
    start_page = int(start_input) if start_input.strip() else None
    
    end_input = input("Enter end page number (press Enter for last page): ")
    end_page = int(end_input) if end_input.strip() else None
    
    # Convert PDF to text
    pdf_to_text(input_pdf, start_page, end_page)
