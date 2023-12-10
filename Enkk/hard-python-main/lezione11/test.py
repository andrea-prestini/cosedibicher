import time


class Rubrica:

    def __init__(self):
        self.contatti = []

    def add_contatto(self, contatto):
        self.contatti.append(contatto)


class Contatto:

    def __init__(self):
        self.nome = input("Nome contatto:\n")
        self.cognome = input("Cognome contatto:\n")
        self.numero = input("Numero contatto:\n")
        time.sleep(2)
        print("Contatto creato correttamente...")

    def change_number(self, new_number):
        print("il vecchio numero era: %s" % self.numero)
        self.numero = new_number

    def stampa(self):
        print("Nome->", self.nome)
        print("Cognome->", self.cognome)
        print("Numero->", self.numero)


contatto_1 = Contatto()
# contatto_1.change_number(999999)
contatto_1.stampa()
