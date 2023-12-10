import sys
import random


nomi = ["andrea", "roberto", "eleonora", "franco", "giovanni"]
cognomi = ["prestini", "tanzini", "favagrossa", "premi"]

numero = 1000000

def lista_persone(num_people):
    result = []
    for i in range(num_people):
        persona = {
            'id': i,
            'nome': random.choice(nomi),
            'cognome': random.choice(cognomi)
        }
        result.append(persona)
    return result

def generatore_persone(num_people):
    for i in range(num_people):
        persona = {
            'id': random.choice(nomi),
            'nome': random.choice(cognomi),
        }
        yield persona