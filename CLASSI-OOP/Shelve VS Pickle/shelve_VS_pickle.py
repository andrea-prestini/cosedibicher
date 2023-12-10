import shelve


with shelve.open("mioDB") as db:
    db["a"] = 1
    db["b"] = 2
    db["c"] = 3
    db["d"] = 4
    db["e"] = 5

new_entry = {
    "uno": "andrea",
    "due": "mario",
}

print("-" * 50)
with shelve.open("mioDB") as db:
    print(type(db))
    print(dict(db))
    print("DB valore chiave c:", db["c"])

print("-" * 50)
with shelve.open("mioDB") as db:
    db.update(new_entry)
    print(dict(db))

class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def __str__(self):
        return f'{self.name}: {self.calories}'


data: dict = {
    "apple": Fruit("Apple", 10),
    "banana": Fruit("Banana", 15),
    "orange": Fruit("Orange", 20),
}


print("-" * 50)
with shelve.open("FruitsDB") as db:
    db.update(data)
    mela = db.get("apple")
    print(mela)
