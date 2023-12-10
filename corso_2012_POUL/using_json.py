#!/usr/bin/env python3
import json
import time
import os


#cameCase VS snake_case
lista_operatori = {
        "Amministratore": {"nome": "Andrea", "cognome": "Prestini"},
        "Gestione finanziaria": {"nome": "Mario", "cognome": "Mometto"},
        "Gestione industriale": {"nome": "Franco", "cognome": "Cabra"},
        "Gestione personale": {"nome": "Eleonora", "cognome": "Favagrossa"},
        "Capo reparto": {"nome": "Roberto", "cognome": "Tanzini"},
        "Operaio Specializzato": {"nome": "Filippo", "cognome": "Braccagnini"},
        "Operaio Generico": {"nome": "Aldo", "cognome": "Tanzini"}
        }

with open("test.json", "w") as fp:
    json.dump(lista_operatori, fp)

with open("test.json", "r") as fp:
    x = json.load(fp)

for i in range(11):
    os.system('clear')
    print("adesso carico il file ed importo i dati JSON...")
    print(i * 5 * "-")
    time.sleep(.2)


if __name__ == "__main__":

    try:
        print()
        print("fatto... vediamo il risultato")
        time.sleep(1)
        i = 1
        for k, v in x.items():
            print(f'''
                    Matricola:\t{i}
                    ruolo:\t{k}
                    nome:\t{x[k]['nome']}
                    cognome:\t{x[k]['cognome']}
                    ----------------------------
                    ''')
            i += 1
            time.sleep(1)

        print("=" * 60)
    except: 
        print("Errore di esecuzione...")
    else: 
        print("Elenco operatori completato!")
    finally:
        print("Procedura terminata...")
