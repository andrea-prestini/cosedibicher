class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self._cognome = cognome

    def scheda(self):
        if hasattr(Persona, 'cognome') :
            return f'''
            nome: {self.nome}
            cognome: "non disposibile"'''
        else:
            return f'''
            nome:  {self.nome}
            cognome: {self._cognome}'''
       
        
           

    @property
    def cognome(self):
        return self._cognome

    @cognome.setter
    def cognome(self, new):
        self._cognome = new

    @cognome.deleter
    def cognome(self):
        del self._cognome
    



s = Persona("Andrea", "Prestini")

print(s.scheda())
s.cognome = "Mometto"
print(s.scheda())

del s.cognome

print(s.scheda())


class PersonaValle:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        

    @property
    def paese(self):
        return self._paese

    @paese.setter
    def paese(self, value):
        self._paese = value
        return self._paese

    @property
    def zona(self):
        if self._zona != "Valle Camonica":
            self._zona = "STRANIERO"
            return self._zona
        else:
            return self._zona
        
    @zona.setter
    def zona(self, value):
        self._zona = value
        return self._zona

    def scheda(self):
        return f'''
        nome: {self.nome}
        cognome: {self.cognome}
        paese: {self._paese}
        zona: {self.zona}'''
        



s = PersonaValle("Andrea", "Prestini")
s.paese = "Esine"
s.zona = "Padania"
print(s.nome) 
print(s.cognome)
print(s.paese)
print(s.zona)

print(s.scheda())