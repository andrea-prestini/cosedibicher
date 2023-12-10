from pathlib import Path
import PyPDF2
import re
from typing import List

# Meglio usare la nuova libreria PyPDF4
# NEURALNiNe ----------------------------------------------------


def extract_text_from_pdf(pdf_file: str) -> List[str]:
    with open(pdf_file, "rb") as pdf:
        reader = PyPDF2.PdfFileReader(pdf, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text


# testo_estratto = extract_text_from_pdf("./Lettera Terzani Fallaci.pdf")
# print(testo_estratto[0:2])

# INDENTLY -------------------------------------------------------
"""
pdfFileObj = open("./Lettera Terzani Fallaci.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print("Numero pagine del documento pdf:", pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
"""

# CHART Explorers

pdf = PyPDF2.PdfFileReader("./Lettera Terzani Fallaci.pdf")

# Grab the page(s)
page_1 = pdf.getPage(0)

# Extract Text
page_1_text = page_1.extractText()

# Combine text from pdf into txt
with Path("./Lettera Terzani Fallaci.txt").open(mode="w") as output_file:
    text = ""
    for page in pdf.pages:
        text += page.extractText()
    output_file.write(text)
    print("File txt da pdf creato con successo!")

# Where's Bush?

bush_pages = []
for page in pdf.pages:
    page_num = pdf.get_page_number(page)
    page_text = page.extractText()

    if "Bush" in page_text:
        bush_pages.append(page_num)
print(bush_pages)

# Save Bush pages to pdf

# create PdfFileReader object
input_pdf = PyPDF2.PdfFileReader("./Lettera Terzani Fallaci.pdf")

# create PdfFileWriter object
pdf_writer = PyPDF2.PdfWriter()

# Get the text from pages with Bush
for page in bush_pages:
    page_object = input_pdf.getPage(page)
    pdf_writer.addPage(page_object)

# Save Pages as PDF
with Path("bush.pdf").open(mode="wb") as output_file_2:
    pdf_writer.write(output_file_2)
print("Creato PDF delle pagine contenenti Bush")

# Get Sentence & page number Bush

pages_sentences = []
for page in pdf.pages:
    page_num = pdf.get_page_number(page)
    page_text = page.extractText()

    if "Bush" in page_text:
        sentence_list = ['pagina ' + str(page_num + 1) +
                         ': ' + sentence.replace('\n', '')
                         for sentence in re.split(r"\. |\? |\! ", page_text)
                         if "Bush" in sentence][0]
        pages_sentences.append(sentence_list)

text = '\n'.join(pages_sentences)
print(text)
