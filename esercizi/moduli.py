#!/usr/bin/python3
# questo programma ci fornisce 10 numeri casuali compresi tra 1 e 50

from math import sqrt
import random
for numero in range(10):
    valore = random.randint(1, 50)
    print(valore)

valore = int(input("inserisci un valore...\n "))
print(sqrt(valore))
