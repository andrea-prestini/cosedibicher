from unittest import result
import openpyxl
import pandas as pd


# book = openpyxl.load_workbook(r'./supermarkt_sales.xlsx')
# sheet = book["Sales"]

# for row in sheet.iter_rows(min_row=4, max_row=100, min_col=2, max_col=10, values_only=True):
#     print(row)


df = pd.read_excel(r'./supermercati.xlsx', engine="openpyxl")
results = df.iloc[:5, :10]
df_query = df[df["Rating"] > 2]

print(df_query)
