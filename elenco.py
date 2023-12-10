"""
v 0.1

carica il file numeri e mette i contatti in memoria
"""
import os


def carica():
    lines = []
    try:
        fin = open("rubrica.txt")
        lines = fin.redlines()
        fin.close()
    except:
        print("file non trovato")
    return lines


def mostra(lines):
    for el in nomi:
        print("nome: ", el["nome"], el["cognome"])


def ordina(nomi):
    nomi.sort()
    return nomi


def splitta(lines):
    res = []
    linenum = 0

    for x in lines:
        x = x.strip()
        vals = x.split("\t")

        linenum += 1

        if len(vals) != 3:
            print("la riga: %d non è valida" % linenum)
            continue

        diz = {"nome": vals[0], "cognome": vals[1], "tel": vals[2]}
        res.append(diz)

    return res


lines = carica()
nomi = splitta(lines)
nomi = ordina(nomi)
mostra(nomi)
