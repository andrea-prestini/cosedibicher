class Persona(object):
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def __repr__(self):
        return f'''
        nome-> {self.nome}
        cognome-> {self.cognome}'''


class Studente(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia

    def __repr__(self):
        return f'''
        nome: {self.nome}
        cognome: {self.cognome}
        materia: {self.materia}'''


uno = Persona("Andrea", "Prestini")
due = Studente("Mario", "Rossi", "matematica")

print("stampiamo scheda persona")
print(uno)
print()
print("stampiamo scheda studente")
print(due)
