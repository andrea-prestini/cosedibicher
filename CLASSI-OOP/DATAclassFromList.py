import dataclasses

elenco = [
    ("andrea", "prestini"),
    ("eleonora", "favagrossa"),
    ("mario", "mometto"),
]

Operatori = dataclasses.make_dataclass("Operatori", ["nome", "cognome"])

for i in range(len(elenco)):
    exec(f'operatore{i} = {Operatori(elenco[i][0], elenco[i][1])}')

print(operatore0)
print(operatore1)
print(operatore2)
