from fpdf import FPDF, YPos, XPos

# create FPDF object

# layout ("P", "L")
# unit ("mm", "cm", "in")
# format ("A3", "A4", "A5", "Letter", "Legal", (100, 150))
# fonts ("time", "courier", "helvetica", "symbol", "zpfdingbats")
# "B" bold, "U" underline, "I" italics, "" regular
# ln (0 or False, 1 True - move cursor down)

pdf = FPDF('P', 'mm', 'Letter')

# Add a page
pdf.add_page()

# specify font
pdf.set_font("helvetica", "", 16)

# Add text
# w = width
# h = height
pdf.cell(40, 10, "Hello World", ln=True, border=True)
pdf.cell(80, 10, "Good Bye World!")
pdf.output("documento1.pdf")
