class Persona:
    def __init__(self, nome, cognome,
                 paese, zona, valore, mese,
                 giorno, segno):

        self.nome = nome
        self.cognome = cognome
        self.paese = paese
        self.zona = zona
        self.valore = valore
        self.mese = mese
        self.giorno = giorno
        self.segno = segno


uno = Persona(
    "andrea",
    "prestini",
    "esine",
    "valle camonica",
    100,
    "gennaio",
    20,
    "capricorno",
)
p = vars(uno)

print("\n".join("%s--> %s" % item for item in p.items()))
print()
print("stampiamo vars(uno)")
print(p)
print()
print("usiamo metodo dict")
print(uno.__dict__)
