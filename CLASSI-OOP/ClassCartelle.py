#!/usr/bin/python3
import os
import shutil
import time


class Cartelle:
    def __init__(self, name):
        self.nome = name

    def create(self):
        print("creo la cartella come richiesto")
        print()
        time.sleep(2)
        os.mkdir(nome)
        time.sleep(2)
        print("ho creato la cartella\n%s" %(nome))


    def delete(self):
        print("CANCELLO la cartella come richiesto")
        print()
        time.sleep(2)
        shutil.rmtree(nome)
        time.sleep(2)
        print("ho rimosso la cartella\n%s" %(nome))

risp = input("vogliamo cominciare?\n")
if risp == "y":
    nome = input("nome della cartella\n")
    Cartelle.create(nome)
else:
    print("arrivederci")


risp = input("cancello la cartella?\n")
if risp == "y":
    Cartelle.delete(nome)


