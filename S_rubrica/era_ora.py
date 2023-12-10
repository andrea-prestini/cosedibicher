#!/usr/bin/python3
from contatto import Contatto
from contatto_manager import ContattoManager
import os

data = input("come si chiama il file archivio dati?\n")
if not os.path.exists(data):
    res = input("il file non esiste, devo crearlo?... ")
    if res == "y":
        ContattoManager().save(data)
        print("file archivio", data, "creato...possiamo continuare!")
    else:
        print("mi dispiace non posso continuare, ARRIVEDERCI...")
        exit(0)


class Rubrica(ContattoManager):
    def menu(self):
        print("""
        1- Nuovo contatto
        2- Elenco contatti
        3- Cerca contatti
        4- Cancella elenco
        5- Cancella file DATI

        X- esci
        """)

        scelta = ""

        while scelta not in ("1", "2", "3", "4", "5"):
            scelta = input("Fai la tua scelta:\n")
            scelta = scelta.strip().lower()

            if scelta == "x":
                print("ARRIVEDERCI, torna presto a trovarci...")
                self.save(data)
                exit(0)

            if scelta not in ("1", "2", "3", "4", "5"):
                continue

            if scelta == "1":
                self.nuovo_contatto()
            elif scelta == "2":
                self.elenco_contatti()
            elif scelta == "3":
                self.cerca_contatti()
            elif scelta == "4":
                if input("sei sicuro di voler procedere? ") == "y":
                    self.clear()
                    print("elenco VUOTO, reinserire i dati da memorizzare...")
            elif scelta == "5":
                if input("VUOI PROCEDERE?...\n") == "y":
                    os.remove(data)
                    print("archivio dati cancellato...\n \
                            esco dal programma, ARRIVEDERCI...")
                    exit(0)
            scelta = "a"

    def _get_nome(self):
        nome = input("nome: ")
        cognome = input("cognome: ")
        nome = nome.strip()
        cognome = cognome.strip()

        return nome, cognome

    def nuovo_contatto(self):
        n, c = self._get_nome()

        return self.add(n, c)

    def elenco_contatti(self):
        res = ("\n".join([str(c) for c in self.lista()]))
        if res == "":
            print("lista vuota, nessun contatto da visualizzare")
        else:
            print(res)

    def cerca_contatti(self):
        nome = input("nome: ")
        res = ([str(c) for c in self. find(nome)])
        if res == []:
            print("nessuna corrispondeza trovata...")
        else:
            print("\n".join(res))


if __name__ == "__main__":
    r = Rubrica()
    r.load(data)
    r.menu()
