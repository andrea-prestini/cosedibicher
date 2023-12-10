#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("incassi.csv", delimiter=",")
# df["importo"].astype(float)
print(df.groupby("provincia")["ente"].count())
print(df[df.provincia == "SO"])
dati = df[df["provincia"] == "LO"].count()
print(f'nella provincia di lodi ci sono {dati.provincia} elementi')
