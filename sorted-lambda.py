d1 = {"uno":10, "due": 20, "tre":"valore"}
d2 = {"quattro": 10, "cinque": 100, "sei": 1200}

d3 = d2
print(max(d1, key=d1.get))

x = [
    ["marco", 44],
    ["roberta", 37],
    ["mattia", 8],
]

y = sorted(x, key=lambda persone: persone[1])

print(y)

v = lambda x, y: f"il risultato è {x+y}"

print(v(10, 12))


x = {
    "marco": 44,
    "roberta": 37,
    "mattia": 8,
}

y = sorted(x, key=x.get)

print(y)


x = {
    "marco": 44,
    "roberta": 37,
    "mattia": 8,
}

print(x.get("mario", "non presente"))