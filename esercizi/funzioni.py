#!/usr/bin/python3
# adesso vediamo la creazione di una funzione!


def sommatrice(a, b):
    print("questa è la funzione somma")
    print("fornisce la somma di due numeri passati come parametri")
    risultato = a + b
    print("\nil risultato della funzione è ", risultato)


a = int(input("inserisci il primo numero "))
b = int(input("inserisci il secondo numero "))
print()
print()
sommatrice(a, b)
