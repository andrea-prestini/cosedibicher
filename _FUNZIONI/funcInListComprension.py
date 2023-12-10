import random

nomi = ("andrea", "enrico", "mario", "eleonora", "franco", "anna", "elvino",
        "roberto", "biagio", "carlo", "dario", "giacomo", "ivo", "luca",
        "nicola", "odino", "paolo", "quasimodo", "salvo", "tiberio", "ugo",
        "valentino")
cognomi = ("prestini", "mometto", "favagrossa")


def generatore(n):
    elenco = []
    for _ in range(1, n):
        uno = [random.choice(nomi), random.choice(cognomi)]
        elenco.append(uno)
    return elenco


numeri = int(input("Quante persone vuoi generare? "))
lettera = input("Quale iniziale nome vuoi filtrare? ")
elenco = [x for x in generatore(numeri) if x[0].startswith(lettera)]

print("in elenco ci sono", len(elenco), "nomi")
for val in elenco:
    print(val)
