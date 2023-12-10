#!/usr/bin/python3
class Studente:
    
    def __init__(self, nome, cognome, corso_di_studi):
        self.__nome = nome
        self.__cognome = cognome
        self.__corso_di_studi = corso_di_studi
    def scheda_personale(self):
        return f"Scheda studente\nNome: {self.__nome}\nCognome: {self.__cognome}\nCorso di studi: {self.__corso_di_studi}\n"


studente1 = Studente("andrea", "prestini", "programmazione")
studente2 = Studente("pietro", "galli", "elettronica")
studente3 = Studente("giovanni", "andreoli", "musica")

persona = eval(input("di chi vuoi conoscere i dati presenti nel database? "))
print(persona.scheda_personale())
