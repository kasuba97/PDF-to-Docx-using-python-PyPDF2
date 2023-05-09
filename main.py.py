from PyPDF2 import (PdfReader)

# Open the PDF file in read-binary mode
with open('climate.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    
    pdf_reader = PdfReader(pdf_file)

    # Get the number of pages in the PDF file
    num_pages = len(pdf_reader.pages)

    # Create a new file to write the extracted text to
    with open('climate.docx', 'w',encoding='utf-8') as text_file:
        # Loop through each page in the PDF file
        for page_num in range(num_pages):
            # Get the page object for the current page
            page_obj = pdf_reader.pages[page_num]

            # Extract the text from the page object
            text = page_obj.extract_text()

            # Write the text to the output file
            text_file.write(text)
            
            # Write a page break or delimiter to separate the text from each page
            text_file.write('\n\nPAGE BREAK\n\n')
            break

