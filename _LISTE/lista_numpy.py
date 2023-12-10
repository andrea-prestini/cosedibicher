import pandas as pd
import numpy as np

base_dati = pd.DataFrame()
size = 1000_000

base_dati["nome"] = np.random.choice(["andrea", "mario", "eleonora", "roberto"], size)
base_dati["cognome"] = np.random.choice(["prestini", "mometto", "favagrossa", "tanzini"], size)
base_dati["paese"] = np.random.choice(["esine", "gambara", "breno", "breno"], size)
base_dati["eta"] = [np.random.randint(20,60) for i in range(size)]

filtro = base_dati[["nome", "cognome", "eta"]].where(base_dati["paese"] == "breno").dropna()

print(base_dati.describe())