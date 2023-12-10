class Persona:

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def scheda_persona(self):
        return "nome " + self.nome + "\ncognome " + self.cognome

    
class Studente(Persona):
    profilo = "Studente"
    
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia

    def scheda_studente(self):
        return "Profilo "+ self.profilo + "\nnome " + self.Ìnome + "\ncognome " + self.cognome + "\nmateria " + self.materia

    @classmethod
    def from_string(cls, stringa_persona):
        nome, cognome, materia = stringa_persona.split("-")
        return cls(nome, cognome, materia)


iron_man = "Tony-Stark-ingegneria"

utente = Studente("andrea", "prestini", "informatica")
persona1 = Studente.from_string(iron_man)
print(utente.scheda_studente())
print()
print(persona1.scheda_studente())
