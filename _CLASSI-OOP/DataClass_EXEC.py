
import dataclasses

elenco = [
    ("andrea", "prestini", "esine"),
    ("eleonora", "favagrossa", "leno"),
    ("mario", "mometto", "gambara"),
    ("federica", "braccagnini", "breno"),
    ("filippo", "braccagnini", "breno"),
    ("aldo", "tanzini", "breno"),
    ("pio", "taranto", "cividate camuno"),
    ("roberto", "tanzini", "breno"),
]


class Elemento:
    def __init__(self, nome, cognome, paese):
        self.nome = nome
        self.cognome = cognome
        self.paese = paese


for i in range(len(elenco)):
    exec(f'squadra{i} = Elemento(elenco[i][0], elenco[i][1], elenco[i][2])')

for x in range(len(elenco)):
    exec(
        f'print(squadra{x}.nome.upper(),"::", squadra{x}.cognome.capitalize(),\
                "-->", squadra{x}.paese.title())')
