import time
import os


magazzino = {}
max_magazzino = int(input("Capienza del magazzino: "))
i = 1


class Scatola:
    colore = "Rossa"
    merce = "Mele"

    def __init__(self):
        global i
        self.codice = input("Inserisci codice: ")
        self.volume = int(input("Inserisci volume: "))
        i += 1

    def show(self):
        print(f'''
        Codice Scatola: {self.codice}
        volume: {self.volume:.2f}
        colore: {self.colore}
        merce: {self.merce}
        ''')


while i <= max_magazzino:
    magazzino[i] = Scatola()
else:
    print("Magazzino completato!")

time.sleep(3)
os.system("clear")

"Stampiamo gli elementi del magazzino"
for k, v in magazzino.items():
    print(f'''
          chiave: {k}
          codice:{v.codice}
          volume:{v.volume}
          merce: {v.merce}
          ''')
    time.sleep(1)
