from pdf2docx import parse
from pdf2docx import Converter

pdf_file = "./bush.pdf"
docx_file = "esportazioneDoc.docx"

# Using Converter class
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()

print("Fine procedura...")


pdf_file = "./bush.pdf"
docx_file = "./convertito_parse.docx"

parse(pdf_file, docx_file)


pdf_file = "./Demografia_Pensioni.pdf"
docx_file = "esportazioneDemoPensioni_2_pagine.docx"

pages_list = [0, 1]
cv = Converter(pdf_file)
cv.convert(docx_file, pages=pages_list)
cv.close()

print("Fine procedura...")
