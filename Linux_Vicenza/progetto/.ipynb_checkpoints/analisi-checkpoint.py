import os
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

os.getcwd()
os.chdir("/home/andrea/andrea.prestini@gmail.com/pythonWorld/prove Coding/Linux_Vicenza/progetto/")

def leggi_dati():
    risultato = {} 

    db_conn = sqlite3.connect("dati.db")
    
    c = db_conn.cursor()
    
    for row in c.execute("SELECT * FROM misurazioni"):
        stanza = row[0]
        temp = row[1]
        hum = row[2]
        
        if not stanza in risultato:
            risultato[stanza] = []
        risultato[stanza].append(
            (temp, hum)
            )
    
    db_conn.close()
    return risultato
    
    
dati = (leggi_dati())
print(dati)

for stanza in dati:
    fig, ax = plt.subplots()
    temp = [r[0] for r in dati[stanza]]
    hum = [r[1] for r in dati[stanza]]
    plt.title(stanza)
    plt.xlabel("tempo")
    plt.ylabel("temp - hum")
    plt.grid()
    plt.plot(temp, color="red", marker="o", label="temperatura")
    plt.plot(hum, color="blue", linestyle="--", marker="D", label="umidità")
    plt.legend(loc="upper left")
plt.show()