class Persona:
    def __init__(self, nome, cognome, paese) -> None:
        self.nome = nome
        self.cognome = cognome
        self.paese = paese

    def scheda(self):
        return f'''
        nome: {self.nome}
        cognome: {self.cognome}
        paese: {self.paese}'''






