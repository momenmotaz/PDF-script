import PyPDF2
import os
import sys

def extract_pages(input_pdf, start_page, end_page, output_pdf):
    """
    Extract specific pages from a PDF file and save them as a new PDF.
    
    Args:
        input_pdf (str): Path to input PDF file
        start_page (int): Start page number (1-based)
        end_page (int): End page number
        output_pdf (str): Path to output PDF file
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)
        
        print(f"\nExtracting pages {start_page} to {end_page} from {input_pdf}...")
        
        # Open the PDF file
        with open(input_pdf, 'rb') as file:
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Get number of pages in PDF
            num_pages = len(pdf_reader.pages)
            
            # Validate page numbers
            if start_page < 1 or start_page > num_pages:
                raise ValueError(f"Start page must be between 1 and {num_pages}")
            if end_page < start_page or end_page > num_pages:
                raise ValueError(f"End page must be between {start_page} and {num_pages}")
            
            # Create PDF writer object
            pdf_writer = PyPDF2.PdfWriter()
            
            # Add specified pages to writer
            for page_num in range(start_page - 1, end_page):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
            
            # Write the extracted pages to output file
            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)
            
            print(f"\nSuccessfully extracted {end_page - start_page + 1} pages to {output_pdf}")
            
    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    # Check if arguments are provided
    if len(sys.argv) > 4:
        input_pdf = sys.argv[1]
        start_page = int(sys.argv[2])
        end_page = int(sys.argv[3])
        output_pdf = sys.argv[4]
    else:
        # Get input from user
        input_pdf = input("Enter path to PDF file: ")
        start_page = int(input("Enter start page number: "))
        end_page = int(input("Enter end page number: "))
        output_pdf = input("Enter path for output PDF file: ")
    
    # Extract pages
    extract_pages(input_pdf, start_page, end_page, output_pdf)
