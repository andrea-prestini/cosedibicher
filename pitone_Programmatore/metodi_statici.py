class Persona:

    persone = []

    def __init__(self, nome, cognome, residenza):
        self.nome = nome
        self.cognome = cognome
        self.persone.append(self)

    @classmethod
    def quante_persone(cls):
        return len(cls.persone)

    @staticmethod
    def parla(x):
        for i in range(x):
         print("ciao amico", i)


persona1 = Persona("Andrea", "Prestini", "Esine")
persona2 = Persona("Mario", "Mometto", "Gambara")

print(Persona.quante_persone())
Persona.parla(5)


    

   



