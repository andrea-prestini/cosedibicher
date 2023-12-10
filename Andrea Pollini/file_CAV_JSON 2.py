import json
import csv


data = [
    "primo messaggio di testo",
    "secondo messaggio di testo",
    "terzo messaggio di testo",
    "quarto messaggio di testo",
    "quinto messaggio di testo"
]

# Scruttura su file
with open("./output.txt", "w") as file:
    for d in data:
        file.write(d + "\n")

print("Stampo file csv")
# Lettura CSV
with open("./file.csv", "r") as file_csv:
    reader = csv.reader(file_csv, delimiter="\n")
    for riga in reader:
        print(riga[0].replace(",", ""))

# Scrittura CSV
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]

with open("./file.csv", "w") as file_csv:
    scrittore = csv.writer(file_csv)
    # writerows con stringhe usa ogni lettera come elemento separato da virgola (write meglio)
    scrittore.writerows(data)

print()
print()

# formato JSON
data = [
    {
        "player": "Cristiano Ronaldo",
        "team": "Juventus",
        "age": 34,
        "statistics": [
                {
                    "matches": 989,
                    "goals": 712,
                    "assists": 219
                }
        ]
    },
    {
        "player": "Roberto Baggio",
        "team": "Juventus",
        "age": 45,
        "statistics": [
                {
                    "matches": 400,
                    "goals": 500,
                    "assists": 100
                }
        ]
    }
]

data_json = json.dumps(data)

with open("./test.json", "w") as f:
    f.write(data_json)

# LOADs prende in input una stringa (risultato di read())
print("Stampo file JSON input come stringa")
with open("./test.json", "r") as lettura:
    data_from_json = json.loads(lettura.read())
    print(data_from_json)

print()
print()
# LOAD prende in input un file
print("Stampo file JSON input come file")
with open("./test.json") as f_file:
    dataJF = json.load(f_file)
    print(dataJF)


dataProf = [
    1,
    2,
    3,
    "test",
    {"pinco": "pallo"}
]

# Stesso discorso per dump da file, dumps da stringa
print("-" * 40)
dataProf_Json = json.dumps(dataProf)
print(dataProf_Json)
