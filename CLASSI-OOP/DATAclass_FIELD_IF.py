from dataclasses import dataclass, field
import time


comuni_valle = [
    "Esine",
    "Breno",
    "Cividate Camuno",
    "Darfo Boario Terme",
    "Edolo",
    "Piancogno",
    "Paspardo",
]


@dataclass
class Persona:

    nome: str
    cognome: str
    paese: str
    eta: int
    ingresso: bool = field(init=False)
    valle: str = field(init=False)

    def __post_init__(self):
        self.ingresso = self.eta >= 18
        if self.paese in comuni_valle:
            self.valle = "Bene, sei un camuno doc!"
        else:
            self.valle = "Mi dispiace sei un ciuccianebbia"

    def scheda(self):
        print(f'''
            nome: {self.nome.title()}
            cognome: {self.cognome.title()}
            paese: {self.paese.title()}
            eta: {self.eta}
            ingresso: {self.ingresso}
            valle: {self.valle}
            ''')


uno = Persona("andrea", "prestini", "Gambara", 52)
due = Persona("nicola", "damiola", "Esine", 15)
tre = Persona("eleonora", "favagrossa", "Leno", 40)
quattro = Persona("roberto", "tanzini", "Breno", 40)
cinque = Persona("sofia", "tanzini", "Breno", 6)


uno.scheda()
print()
time.sleep(2)
due.scheda()
print()
time.sleep(2)
tre.scheda()
print()
time.sleep(2)
quattro.scheda()
print()
time.sleep(2)
cinque.scheda()
