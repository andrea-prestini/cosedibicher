import pandas as pd
import time


df = pd.read_json("deadge.json")
print(type(df))


gennaio = df.loc["January"]

for anno in gennaio.keys():
    for giorno in gennaio[anno]:
        for persona in gennaio[anno][giorno]:
            scheda = (f'{persona["name"]} -> {persona["age"]}')
            print(scheda)
            time.sleep(0.5)
