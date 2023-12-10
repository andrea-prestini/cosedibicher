'''
Programma ricerca personaggi famosi morti
Dato un nome scritto con iniziali maiuscole,
trova tutte le occorrenze nel file json estratto da wikipedia
'''

import json
import time

# carico il file json contenente i dati
with open("./deadge.json", 'r') as f:
    data = json.load(f)

# parametri morte su richiesta: chi vuoi cercare?
x = input("Chi è morto?\n").title()
print("Cerchiamo: ", x)

# lista che conterrà i risultati trovati
founded = []

# ciclo sul json per trovare la corrispondeza con la richiesta
for year in data.keys():
    for month in data[year].keys():
        for day, deaths_of_day in data[year][month].items():
            for person in deaths_of_day:
                if x in person["name"]:
                    matched = [
                            person["name"], year, month, day, person["info"]
                                ]
                    founded.append(matched)
# controllo la lunghezza della lista risultati, se maggiore di 0 messaggio
# e stampa dei risultati, diversamente messaggio di "Valore NON presente"
if len(founded) > 0:
    print("TROVATO!")
    print("Ho trovato:", len(founded), "valori")
    time.sleep(3)
    for i in range(len(founded)):
        print(f'''
valore: {i+1}
nome: {founded[i][0]}
anno: {founded[i][1]}
mese: {founded[i][2]}
giorno: {founded[i][3]}
info: {founded[i][4]}
''')
        if len(founded) > 10:
            time.sleep(0.01)
        else:
            time.sleep(1.5)
    print("Ho trovato:", len(founded), "valori")

else:
    print("Valore NON presente!")
