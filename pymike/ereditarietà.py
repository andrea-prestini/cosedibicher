#!/usr/bin/python3

class Persona:
    def __init__(self, nome, cognome, eta, residenza):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.residenza = residenza

    def scheda_personale(self):
        scheda = f'''
        Nome: {self.nome}
        Cognome: {self.cognome}
        eta: {self.eta}
        Residenza: {self.residenza}'''

        return scheda

    def modifica_scheda(self):
        print('''Modifica Scheda:
        1- Nome
        2- Cognome
        3- eta
        4- Residenza''')

        scelta = input("Cosa desideri modificare? ")
        if scelta == "1":
            self.nome = input("Nuovo nome ===> ")
        if scelta == "2":
            self.nome = input("Nuovo cognome ===> ")
        if scelta == "3":
            self.eta = input("Nuova eta ===> ")
        if scelta == "4":
            self.residenza = input("Nuova residenza ===> ")


class Studente(Persona):
    profilo = "Studente"

    def __init__(self, nome, cognome, eta, residenza, materia):
        super().__init__(nome, cognome, eta, residenza)
        self.materia = materia

    def scheda_personale(self):
        scheda = f"""
        Profilo: {Studente.profilo}
        Materia: {self.materia}
        ***"""

        return super().scheda_personale() + scheda

    def cambio_materia(self, materia):
        self.materia = materia
        print("Materia aggiornata!")


class Insegnante(Persona):
    profilo = "Insegnante"

    def __init__(self, nome, cognome, eta, residenza, materie=None):
        super().__init__(nome, cognome, eta, residenza)
        if materie is None:
            self.materie = []
        else:
            self.materie = materie

    def scheda_personale(self):
        scheda = f"""
        Profilo: {Insegnante.profilo}
        Materia: {self.materie}
        ***"""

        return super().scheda_personale() + scheda

    def aggiungi_materie(self, nuova):
        if nuova not in self.materie:
            self.materie.append(nuova)
        print("Elenco materie aggiornato!")


# elenco studenti
studente1 = Studente("andrea", "prestini", "47",
                     "casa dello studente", "informatica")
studente2 = Studente("francesca", "maffezzoni", "45",
                     "via parma 24", "matematica")

# elenco insegnanti
insegnante1 = Insegnante("mario", "rossi", "67", "vicolo rovina", [
                         "matematica", "fisica"])
insegnante2 = Insegnante("paolo", "marcheni", "59", "piazza brusati", "fisica")


# output a terminale
print(studente1.scheda_personale())
print(studente2.scheda_personale())
print(insegnante1.scheda_personale())
print(insegnante2.scheda_personale())
# insegnante1.modifica_scheda()
print(insegnante1.scheda_personale())
studente1.cambio_materia("statistica")
insegnante1.aggiungi_materie("fisica applicata")
print(studente1.scheda_personale())
print(insegnante1.scheda_personale())
