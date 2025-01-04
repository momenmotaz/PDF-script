import pytesseract
from pdf2image import convert_from_path
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# Set paths for external tools
#غير الباث حسب جهازك
#change path for depend on your device
POPPLER_PATH = r"d:/momen fci 3/AI apps/lec/poppler/poppler-23.11.0/Library/bin"
TESSERACT_PATH = r"d:/momen fci 3/AI apps/lec/tesseract-ocr/tesseract.exe"

# Configure tesseract path
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def process_page(image, page_num, total_pages):
    """Process a single page using OCR"""
    try:
        # Extract text using Tesseract
        text = pytesseract.image_to_string(image, lang='eng')
        
        if text.strip():
            return (page_num, text.strip())
        return None
    except Exception as e:
        print(f"\nError processing page {page_num}: {str(e)}")
        return None

def print_page(page_num, text, total_pages):
    """Print page content with formatting"""
    print("\n" + "-"*60)
    print(f"\n[Page {page_num}/{total_pages}]\n" + "-"*60 + "\n")
    
    # Split text into paragraphs and print with proper spacing
    paragraphs = [p.strip() for p in text.strip().split('\n\n') if p.strip()]
    for p in paragraphs:
        # Replace multiple spaces and newlines with single space
        p = ' '.join(p.split())
        print(f">> {p}\n")
    
    print("-"*60 + "\n")

def read_pdf(input_pdf, start_page=None, end_page=None):
    """
    Read text from PDF file using OCR.
    
    Args:
        input_pdf (str): Path to input PDF file
        start_page (int, optional): Start page number (1-based)
        end_page (int, optional): End page number
                                If None, will read until the last page
    
    Returns:
        list: List of tuples (page_number, text_content)
    """
    try:
        print("\nConverting PDF to images...")
        # Convert PDF to images with lower DPI for faster processing
        images = convert_from_path(
            input_pdf, 
            poppler_path=POPPLER_PATH,
            dpi=150,  # Good balance between speed and quality
            thread_count=4
        )
        
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
        
        # Process pages in parallel using ThreadPoolExecutor
        selected_images = images[start_idx:end_idx + 1]
        page_numbers = range(start_page, end_page + 1)
        
        results = []
        with ThreadPoolExecutor(max_workers=4) as executor:
            # Submit all tasks and store with their page numbers
            future_to_page = {
                executor.submit(process_page, img, page_num, end_page): page_num
                for img, page_num in zip(selected_images, page_numbers)
            }
            
            # Process results as they complete and store them
            for future in as_completed(future_to_page):
                result = future.result()
                if result:
                    results.append(result)
        
        # Sort results by page number
        results.sort(key=lambda x: x[0])
        
        # Print pages in order
        for page_num, text in results:
            print_page(page_num, text, end_page)
        
        return results
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        return []

if __name__ == "__main__":
    # Check if PDF path is provided as argument
    if len(sys.argv) > 1:
        input_pdf = sys.argv[1]
        start_page = int(sys.argv[2]) if len(sys.argv) > 2 else None
        end_page = int(sys.argv[3]) if len(sys.argv) > 3 else None
    else:
        # Get input from user
        input_pdf = input("Enter path to PDF file: ")
        
        # Page range is optional
        start_input = input("Enter start page number (press Enter for first page): ")
        start_page = int(start_input) if start_input.strip() else None
        
        end_input = input("Enter end page number (press Enter for last page): ")
        end_page = int(end_input) if end_input.strip() else None
    
    # Read PDF
    read_pdf(input_pdf, start_page, end_page)
