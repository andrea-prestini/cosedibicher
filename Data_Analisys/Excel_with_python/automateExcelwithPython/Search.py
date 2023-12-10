#pip3 install pandas
import pandas as pd
#pip3 install numpy
import numpy as np

#specify the files location (or path)
files = ['./SampleData.xlsx', './SampleData2.xlsx']

#loop through the "files" list
for file in files:
    #read each file in a dataframe
    df = pd.read_excel(file)
    #locate the "Item" column and return the "Rep" where the condition matches "Pencil"
    pencil = df[['Rep', 'Item', 'Region']].where(df['Item'] == 'Pencil').dropna()
    jones = df[['Rep', 'Item', 'Region']].query("Rep == 'Jones'").dropna()


    #print file name
    print(file)
    #print filtered results
    print(pencil)
    print(jones)




# Rep = Jones

