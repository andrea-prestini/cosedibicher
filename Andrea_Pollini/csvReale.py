import csv

data = []


def parse_row(row):
    data.append(
        {
            "id": row[0],
            "impact": int(row[3]),
            "location": row[6],
        }
    )


with open("./earthquakes.csv", "r") as file_csv:
    reader = csv.reader(file_csv, delimiter=",")
    for pos, riga in enumerate(reader):
        if pos > 0:
            parse_row(riga)

for i in range(len(data)):
    if data[i]["impact"] > 800:
        print("id: {} impact: {} location: {}".format(
            data[i]["id"], data[i]["impact"], data[i]["location"]))

print()
print(f'Sono presenti: {len(data)} dati')
