import tabula


pdf_path = "./Demografia_Pensioni.pdf"
dfs = tabula.read_pdf(pdf_path, pages="6")
dfs[0].to_csv("first_table.csv")


print("fine procedura")
