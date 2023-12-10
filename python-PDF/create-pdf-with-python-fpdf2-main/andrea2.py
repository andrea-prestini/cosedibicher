from fpdf import FPDF


class PDF(FPDF):
    def header(self) -> None:
        # a logo
        self.image("./fox_face.png", 10, 8, 25)
        # font
        self.set_font('helvetica', 'B', 20)
        # Padding
        self.cell(80)
        # Title
        self.cell(30, 10, "Title", border=True, ln=True, align="C")
        # line break
        self.ln(20)

    def footer(self):
        # set the position of the footer
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()} of {{nb}}', align="R")


pdf = PDF("P", "mm", "Letter")
pdf.add_page()
pdf.set_font("helvetica", "BIU", 12)
pdf.set_text_color(220, 50, 50)

# Set auto page break
pdf.set_auto_page_break(auto=True, margin=100)


for i in range(1, 40):
    pdf.cell(0, 10, f'This is line {i}', ln=1)


pdf.output("documento2.pdf")
