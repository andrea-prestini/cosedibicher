import requests
import time


url = 'https://sg-bus-arrival.haris-samingan.repl.co/?id=18141'
data = requests.get(url)

data_dictionary = data.json()

print("Show all bus...")
for val in data_dictionary["services"]:
    print(val)
    time.sleep(1)

minuti = []
for val in data_dictionary["services"]:
    if val["next_bus_mins"] > 0:
        minuti.append(val["next_bus_mins"])

time.sleep(2)
print("il primo bus arriverà in:", min(minuti), "minuti")
time.sleep(3)
print("fine procedura...")
