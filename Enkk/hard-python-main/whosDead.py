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

# ciclo sul json per trovare la corrispondeza con la richiesta
# se esiste stampo le informazioni, diversamente stampo un messaggio

for year in data.keys():
    for month in data[year].keys():
        for day, deaths_of_day in data[year][month].items():
            for person in deaths_of_day:
                if x in person["name"]:
                    print(f'''
nome: {person["name"]}
anno: {year}
mese: {month}
giorno: {day}
info: {person["info"]}
------------------------
                            ''')

                    time.sleep(0.3)

print("Fine processo!")
