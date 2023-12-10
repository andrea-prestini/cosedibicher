import random


# creare una lista di interi e mischiarla
elementi = [x for x in range(10)]


def mischia(l):
    for _ in range(100):
        i1 = random.randint(0, len(l)-1)
        i2 = random.randint(0, len(l)-1)
        l[i1], l[i2] = l[i2], l[i1]

    return l


print(elementi)
print(mischia(elementi))
random.shuffle(elementi)
print(elementi)
print("-" * 50)
# dizionario
d = {"chiave1": [1, 2, 3], "chiave2": ["uno", "due", "tre"], }
d1 = {"andrea": "prestini"}
d2 = {"esine": "brescia"}
d3 = {x: x**2 for x in range(10)}

print(d["chiave2"])
print(d.get("chiave3", "chiave non presente!"))
new_dict = d | d1
print("Merged dict")
for k, v in new_dict.items():
    print(f'chiave: {k}- valore: {v}')

print("in place")
d |= d2
print(d)
