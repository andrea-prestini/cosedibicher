import os
import shutil
import time

elenco = ["bicher", "casa", "esine"]

for nome in elenco:
    print("creo la cartella " + str(nome))
    time.sleep(1)
    os.makedirs(nome, exist_ok=True)


risposta = input("vuoi cancellare le cartelle create?\n")

if risposta == "si":
    for nome in elenco:
        os.rmdir(nome)
        time.sleep(2)
        print("ho rimosso la cartella " + str(nome) + " come richiesto!")
else:
    print("ok arrivederci e grazie")
