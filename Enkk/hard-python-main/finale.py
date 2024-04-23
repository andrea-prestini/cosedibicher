import json

# load data
with open("deadge.json") as f:
    data = json.load(f)

risultato = {}
for anno, anno_vals in data.items():
    for mese, mese_vals in anno_vals.items():
        for giorno, giorno_vals in mese_vals.items():
            for persona in giorno_vals:
                if persona["age"] < 2:
                    risultato[persona["name"]] = {
                        persona["age"]: persona["info"]}
print(risultato)
