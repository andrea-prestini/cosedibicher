import os, sys # standard python library
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu
# import win32com.client as win32

# change path to current working directory
os.chdir(sys.path[0])

doc = DocxTemplate("template.docx")
# il placeholder è un dizionario
# Cm indica la misura dell'immagine espressa in centimetri
placeholder_1 = InlineImage(doc, "./Placeholders/Placeholder_1.png", Cm(5))
placeholder_2 = InlineImage(doc, "./Placeholders/Placeholder_2.png", Cm(5))
context = {
    "name": "Andrea",
    "placeholder_1": placeholder_1,
    "placeholder_2": placeholder_2,
    }

# scriviamo le info nel placeholder
doc.render(context)

# creiamo un nuovo file contenente le informazioni
doc.save("template.rendered.docx")

def convert_to_pdf(doc): # pip install pypiwin32

    """ Convert given word documento to pdf"""
    # word = win32.DispatchEx("Word.Application")
    # new_name = doc.replace(".docx", r".pdf")
    # worddoc = word.Documents.Open(doc)
    # worddoc.SaveAs(new_name, FileFormat=17)
    # worddoc.close()
    return None

convert_to_pdf("./template.rendered.docx")






