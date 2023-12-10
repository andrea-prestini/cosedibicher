#!/usr/bin/env python3
import pickle

listaNumeri = ["uno", "due", "tre", 4, 5]

with open("test.dat", "wb") as fp:
    pickle.dump(listaNumeri, fp)

with open("test.dat", "rb") as fp:
    x = pickle.load(fp)

print(x)
