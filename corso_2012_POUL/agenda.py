#!/usr/bin/env python3
import gzip
import pickle

agenda = {
        "prestini": 111111,
        "archetti": 222222,
        "mometto": 333333,
        "damiola": 444444,
        "ferrari": 555555,
        "sala": 666666,
        }

def cerca(cognome):
    try:
        return agenda[cognome]
    except KeyError as errore:
        codice = "Cognome non trovato: {}. Riprova..."
        print(codice.format(errore))

def elenca(cognome = True):
    for num in enumerate(sorted(agenda)):
        print(num)

def elimina(cognome):
    del agenda[cognome]

def salva(dummy):
    with gzip.open("agenda.dat", "wb") as dati:
        pickle.dump(agenda, dati)

def carica(dummy):
    with gzip.open("agenda.dat", "rb") as dati:
        agenda = pickle.load(dati)



comandi = {
        'cerca': cerca,
        'elenca': elenca,
        'elimina': elimina,
        'salva': salva,
        'carica': carica,
        }

if __name__ == '__main__':
    import sys

    funzione = comandi[sys.argv[1]]

    try:
        funzione(sys.argv[1])
    except IndexError:
        funzione(None)
