#!/usr/bin/python3

class Persona:

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    @staticmethod
    def info_progetto():
        info = "Nome: Persona"+"\nCreato da: Andrea Prestini"+"\nscritto usando python 3.6"+"\n*********************************************"
        return info
    
    @classmethod
    def occupazione(cls):
        if cls.__name__ == "Studente":
            return "Studente"
        else:
            return "Insegnante"

    @classmethod
    def from_string(cls, stringa_persona,*args):
        nome, cognome = stringa_persona.split("-")
        return cls(nome, cognome, *args)

    def scheda_personale(self):
        scheda = "\nnome "+self.nome+"\ncognome "+self.cognome + "\n****************************************************"
        return scheda


class Studente(Persona):
    profilo = "Studente"

    def __init__(self, nome, cognome, materia):
        super().__init__ (nome, cognome)
        self.materia = materia

    def scheda_personale(self):
        scheda = "Profilo: " + self.profilo + "\nMateria: " + self.materia
        return scheda + super().scheda_personale()
        


iron_man = "Tony-Stark" #stringa di ingresso

studente1 = Studente("andrea", "prestini", "informatica")
studente2 = Studente.from_string(iron_man, "ingegneria")

print(Persona.info_progetto())
print(studente1.scheda_personale())
print(studente2.scheda_personale())


print(Persona.scheda_personale(studente2))
print(studente1.occupazione())
