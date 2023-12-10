from dataclasses import dataclass, astuple, asdict

@dataclass
class Persona:
    """
    Attributes: -> str
    nome: -> str
    cognome: -> str
    paese: -> str
    zona: -> str
    valore: -> int
    mese: -> str
    giorno: -> int
    segno: -> str

    """
    nome: str
    cognome: str
    paese: str
    zona: str
    valore: int
    mese: str
    giorno: int
    segno: str
    sesso: str = "maschio"


uno = Persona("andrea", "prestini", "esine", "valle camonica",
              100, "gennaio", 20, "capricorno")

for k, v in uno.__dict__.items():
    print(f' {k} -> {v}')

print("funzioni dataclasses")
print(asdict(uno))
print(astuple(uno))