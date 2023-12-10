from dataclasses import dataclass
import time
import os


@dataclass
class Omino:
    """
    Attributes:
        colorito: -> str
        capelli: -> str
        occhi: -> str
        bocca: -> str
        pantaloni: -> str
        maglietta: -> str
    """
    _colorito: str
    _capelli: str
    _occhi: str
    _bocca: str
    _pantaloni: str
    _maglietta: str

    @property
    def colorito(self):
        'property colorito'
        return self._colorito

    @colorito.setter
    def colorito(self, value):
        self._colorito = value

    @property
    def capelli(self):
        'property capelli'
        return self._colorito

    @capelli.setter
    def capelli(self, value):
        self._capelli = value

    @property
    def occhi(self):
        'property occhi'
        return self._occhi

    @occhi.setter
    def occhi(self, value):
        self._occhi = value

    @property
    def bocca(self):
        'property bocca'
        return self._bocca

    @bocca.setter
    def bocca(self, value):
        self._bocca = value

    @property
    def pantaloni(self):
        'property pantaloni'
        return self._pantaloni

    @pantaloni.setter
    def pantaloni(self, value):
        self._pantaloni = value

    @property
    def maglietta(self):
        'property maglietta'
        return self._maglietta

    @maglietta.setter
    def maglietta(self, value):
        self._maglietta = value

    def camminare(self, val):
        'Quanto cammina il nostro omino'
        print(f"il nostro omino cammnina per {val} cm")

    def saltare(self, val):
        'Quanto salta il nostro omino'
        print(f"il nostro omino salta per {val} cm")

    def girare(self, val):
        'Quanto si gira il nostro omino'
        print(f"il nostro omino si gira ad una velocità pari a {val}")


# Genero 3 istanze della classe Omino
A = Omino("rosa", "biondo", "neri", "rossa", "grigi", "nera")
B = Omino("rosa", "niente", "blu", "rosa", "neri", "marrone")
C = Omino("rosso", "rosa", "neri", "rossa", "nera", "nera")

# Attivo alcuni metodi della classe Omino
print("il nostro omino A ha la bocca", A.bocca)
time.sleep(1)
print("il nostro omino A ha la maglietta", A.maglietta)
time.sleep(1)
print("il nostro omino B ha la maglietta", B.maglietta)
time.sleep(1)
print("il nostro omino C porta i capelli", C.capelli)
time.sleep(1)
print("il nostro omino A ha un colorito", A.colorito)
time.sleep(1)

C.camminare(50)
time.sleep(1)
A.girare(3)
time.sleep(3)
os.system("clear")

print("Adesso cambiamo la maglietta di A")
time.sleep(2)
print("A aveva la maglietta color", A.maglietta)
A.maglietta = "verde"
time.sleep(2)

print("Adesso l'omino A ha la maglietta color", A.maglietta)
