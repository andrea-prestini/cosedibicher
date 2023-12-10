from PyPDF2 import PdfFileMerger
# Meglio utilizzare la nuova libreria PyPDF4


# Create an instance of PDdfFileMerger() class
merger = PdfFileMerger()

# List of files path
pdf_files = ["./Lettera Terzani Fallaci.pdf", "./Demografia_Pensioni.pdf"]

# Iterate over the list of the file paths
for pdf_file in pdf_files:
    # Append PDF files
    merger.append(pdf_file)

# Write out the serged PDF file
merger.write("merged_files.pdf")
merger.close()

print("Fine procedura...")
