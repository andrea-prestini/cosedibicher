import tabula


pdf_path = "https://sedl.org/afterschool/toolkits/science/pdf/ast_sci_data_tables_sample.pdf"

dfs = tabula.read_pdf(pdf_path, pages="2")

for i in range(len(dfs)):
    print(dfs[i])


print("Fine procedura...")
