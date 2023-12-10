import pandas as pd
import numpy as np

def get_dataset(size):
        df = pd.DataFrame()
        df["position"] = np.random.choice(["left", "middle", "right"], size)
        df["age"] = np.random.randint(1,50)
        df["time"] = np.random.choice(["red", "blue", "yellow", "green"], size)
        df["win"] = np.random.choice(["yes", "no"], size)
        df["prob"] = np.random.uniform(0,1, size)
        return df


df = get_dataset(1000)

results = df.query("win == 'yes' and position == 'middle'")
print("codice nuovo")
print(results)
print("-" * 50)

print("codice vecchio")
uno = df[["age", "prob"]][(df["win"] == "yes") & (df["position"] == "middle")]
print(uno)
