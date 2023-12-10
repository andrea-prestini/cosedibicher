from PyPDF2 import PdfReader

# Meglio utilizzare la nuova libreria PyPDF4
# Define path to PDF file
pdf_path = "./Lettera Terzani Fallaci.pdf"

# Open the file in binary mode for reading
with open(pdf_path, "rb") as pdf_file:
    # Read pdf file
    pdf_reader = PdfReader(pdf_file)
    # Get number of pages in the pdf file
    page_nums = len(pdf_reader.pages)

    # Iterate over each page number
    for page_num in range(page_nums):
        # Read the pdf page
        page = pdf_reader.pages[page_num]
        # Extract text from pdf page
        text = page.extract_text()
        # Print text from pdf page
        print(text)


print("Fine procedura")
