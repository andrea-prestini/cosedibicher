#!/usr/bin/python3


class Impiegati():

    cittadinanza = "Italiana"

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def scheda(self):
        if self.cognome == "prestini":
            self.cittadinanza = "marocchina"
        print(f'''
                nome: {self.nome}
                cognome: {self.cognome}
                cittadinanza: {self.cittadinanza}
                ''')

    def info(self):
        print(f'''
        il personaggio si chiama {self.nome}
        ed ha cittadinanza {self.cittadinanza}
                ''')


impiegato4 = Impiegati("giovanni", "conzadori")
impiegato1 = Impiegati("andrea", "prestini")
impiegato2 = Impiegati("mario", "mometto")
impiegato3 = Impiegati("francesca", "maffezzoni")
impiegato5 = Impiegati("paolo", "foresti")

Impiegati.scheda(impiegato1)
Impiegati.info(impiegato1)
