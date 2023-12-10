#!/usr/bin/python3
from random import randint

print("ciao premi INVIO per iniziare")
input()
print("adesso inserisci i dettagli seguenti:")
print("nome:")
nome = input()
print("cognome:")
cognome = input()
print("ciao", nome, cognome, "come stai?")
print("data di nascita:")
print("devi avere 12 anni o più")
controllo_giorno = "s"
while controllo_giorno == "s":
    print("giorno:")
    giorno = int(input())
    if (giorno < 1) or (giorno > 31):
        print("giorno errato, inserire un valore corretto")
        controllo_giorno = "s"
    else:
        controllo_giorno = "n"
ListaMese = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
             "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]
controllo_mese = "s"
while controllo_mese == "s":
    print("mese: es. (settembre)")
    mese = input()
    if mese not in ListaMese:
        print("inserisci un mese valido!")
        controllo_mese = "s"
    else:
        controllo_mese = "n"
print("anno:")
anno = int(input())
controllo_anno = "s"
while controllo_anno == "s":
    if anno > 2003:
        print("sei troppo giovane!")
        print("mi dispiace, arrivederci")
        exit()
    else:
        controllo_anno = "n"
pswd = "asa"
pswd_check = "s"
while pswd_check == "s":
    Npswd = input("inserisci la tua password: ")
    if Npswd != pswd:
        print("ERRATA!")
        pswd_check = "s"
    else:
        pswd_check = "n"
        print("bene allora possiamo andare avanti!")
        print("Tu sei", nome, cognome, "e sei nato", giorno, mese, anno)
obiettivo = randint(1, 10)
for x in range(1, 6):
    print("indovina il numero")
    risposta = int(input("da 1 a 10\n"))
    if risposta == obiettivo:
        print()
        print("hai indovinato")
        print("bravo")
        break
    else:
        print()
        print("Sbagliato!")
        print("ti rimangono", 5-x, "tentativi!")
print("ARRIVEDERCI")
