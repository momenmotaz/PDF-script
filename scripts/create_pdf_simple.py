from fpdf import FPDF
import os

def create_pdf(input_file, output_file):
    # Initialize PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Read content and preprocess
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace special character with **
    content = content.replace('✓', '**')
    lines = content.split('\n')
    
    # Process each line
    for line in lines:
        # Remove trailing whitespace but keep indentation
        line = line.rstrip()
        if not line:
            pdf.ln(6)  # Empty line spacing
            continue
            
        # Question header (starts with number)
        if line[0].isdigit() and '. ' in line:
            pdf.set_font('Arial', 'B', 11)  # Bold for questions
            pdf.multi_cell(0, 6, line)
            pdf.set_font('Arial', '', 11)  # Reset to normal
            
        # Correct answer (contains **)
        elif '**' in line:
            pdf.set_font('Arial', 'B', 11)  # Bold for correct answers
            pdf.multi_cell(0, 6, line)
            pdf.set_font('Arial', '', 11)  # Reset to normal
            
        # Other lines (normal text)
        else:
            pdf.set_font('Arial', '', 11)
            pdf.multi_cell(0, 6, line)
            
        # Check if we need a new page
        if pdf.get_y() > 270:
            pdf.add_page()
    
    pdf.output(output_file)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python create_pdf.py input_file output_file")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
        
    create_pdf(input_file, output_file)
    print(f"PDF created successfully: {output_file}")
