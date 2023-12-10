from dataclasses import dataclass, astuple, asdict, field


# se aggiungo (frozen=True) NON possiamo modificare gli attributi default
@dataclass
class Persona:

    nome: str
    cognome: str
    age: int
    paese: str
    zona: str
    valore: int
    mese: str
    giorno: int
    segno: str
    sesso: str = "maschio"
    can_vote: bool = field(init=False)

    def __post_init__(self):
        self.can_vote = 18 <= self.age <= 70


uno = Persona("andrea", "prestini", 13, "Esine", "Valle Camonica",
              100, "gennaio", 20, "capricorno")
# uno.sesso = "Femmina" genera errore perchè settato frozen True
print(uno)
print()
print("metodo asdict di dataclass")
print(asdict(uno))
print()
print("metodo astuple di dataclass")
print(astuple(uno))
