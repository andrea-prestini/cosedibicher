import requests

r = requests.get(
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")


dataset = r.json()

features = dataset["features"]

data = []
for f in features:
    data.append({
        "impact": f["properties"]["sig"],
        "magnitude": f["properties"]["mag"],
        "tsunami": f["properties"]["tsunami"],
        "location": f["properties"]["place"]
    })


for i in range(len(data)):
    print(f''' "impatto": {data[i]["impact"]}
          "magnitude": {data[i]["magnitude"]}
          "tsunami": {data[i]["tsunami"]}
          "location": {data[i]["location"]}
          ''')
