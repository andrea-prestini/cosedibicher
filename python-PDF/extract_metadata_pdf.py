# Import the required dependency
import pikepdf


# Open pdf file with pikepdf
pdf = pikepdf.open("./Lettera Terzani Fallaci.pdf")

# Extract metadata
pdf_metadata = pdf.docinfo  # Dictionary

for k, v in pdf_metadata.items():
    print(f'key: {k} value: {v}')
