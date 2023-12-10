import numpy as np


x = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)],

             dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])

print(x["name"])

print("-" * 60)
operai = np.array([
    ("andrea", "prestini", "esine"),
    ("eleonora", "favagrossa", "leno"),
    ("roberto", "tanzini", "breno")
],
    dtype=[("nome", "U10"), ("cognome", "U10"), ("paese", "U10")])

print(operai)
print()
print(operai["nome"])
print()
print(operai["paese"])

print("-" * 60)
for val in operai:
    print(val)
