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
        Età: {self.eta}
        Residenza: {self.residenza}\n'''

        return scheda

    @classmethod
    def from_string(cls, stringa_persona):
        nome, cognome, eta, residenza = stringa_persona.split("-")
        return cls(nome, cognome, eta, residenza)



uno = "Andrea-Prestini-52-Esine"

persona1 = Persona.from_string(uno)

print(persona1.scheda_personale())



