#!/usr/bin/python3
import os
import time
import shutil

lista = []

while True:
    x = input("scrivi il nome della directory ")
    if x == "no":
        print(f"abbiamo la seguente lista\n {lista}")
        break
    else:
        lista.append(x)
        print(f"ho inserito {x} nella lista")

for x in lista:
    if os.path.exists(x):
        print(f"la directory {x} esiste già, non faccio nulla...")
    else:
        os.mkdir(x)
        print("ho creato la cartella %s" % (x))
        time.sleep(3)


risposta = input("vuoi cancellare le cartelle create? ")
if risposta == "y":
    for x in lista:
        try:
            shutil.rmtree(x, ignore_errors=True)
            print(f"ho eliminato la cartella {x}")
            time.sleep(3)
        except:
            print(f"non esiste la directory {x}")
else:
    print("ok allora non faccio nulla")


print()
print()
print()

print("Esecuzione terminata... arrivederci e grazie!")
