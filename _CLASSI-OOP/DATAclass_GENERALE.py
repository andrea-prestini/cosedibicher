from dataclasses import dataclass
import time
import os


@dataclass
class Omino:
    """
    Attributes: -> str
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

    def get_colorito(self):
        ' metodo get attributo colorito'
        return self._colorito

    def set_colorito(self, new_colorito):
        'metodo set attributo colorito'
        self._colorito = new_colorito

    def get_capelli(self):
        ' metodo get attributo capelli'
        return self._capelli

    def set_capelli(self, new_capelli):
        'metodo set attributo capelli'
        self._capelli = new_capelli

    def get_occhi(self):
        ' metodo get attributo occhi'
        return self._occhi

    def set_occhi(self, new_occhi):
        'metodo set attributo occhi'
        self._occhi = new_occhi

    def get_bocca(self):
        ' metodo get attributo bocca'
        return self._bocca

    def set_bocca(self, new_bocca):
        'metodo set attributo bocca'
        self._bocca = new_bocca

    def get_pantaloni(self):
        ' metodo get attributo pantaloni'
        return self._pantaloni

    def set_pantaloni(self, new_pantaloni):
        'metodo set attributo pantaloni'
        self._pantaloni = new_pantaloni

    def get_maglietta(self):
        ' metodo get attributo maglietta'
        return self._maglietta

    def set_maglietta(self, new_maglietta):
        'metodo set attributo maglietta'
        self._maglietta = new_maglietta

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
print("il nostro omino A ha la bocca", A.get_bocca())
time.sleep(1)
print("il nostro omino A ha la maglietta", A.get_maglietta())
time.sleep(1)
print("il nostro omino B ha la maglietta", B.get_maglietta())
time.sleep(1)
print("il nostro omino C porta i capelli", C.get_capelli())
time.sleep(1)
print("il nostro omino A ha un colorito", A.get_colorito())
time.sleep(1)

C.camminare(50)
time.sleep(1)
A.girare(3)
time.sleep(3)
os.system("clear")
print("Adesso cambiamo la maglietta di A")
time.sleep(2)
print("A aveva la maglietta color", A.get_maglietta())
A.set_maglietta("verde")
time.sleep(2)
print("Adesso l'omino A ha la maglietta color", A.get_maglietta())
