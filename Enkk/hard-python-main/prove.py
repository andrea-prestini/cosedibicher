import json
import pandas as pd
import time


with open("deadge.json") as f:
    data = json.load(f)


df = pd.DataFrame(data)
print(df["1992"].value_counts())
