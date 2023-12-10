class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f'''
        Rappresentazione metodo STR verso utente!
        nome:     {self.nome.capitalize()}
        cognome:  {self.cognome.capitalize()}'''

    def __del__(self):
        print("Elimino il valore richiesto -->", self.nome, self.cognome)
        del self

    


uno = Persona("andrea", "prestini")
due = Persona("eleonora", "favagrossa")
tre = Persona("roberto", "tanzini")
