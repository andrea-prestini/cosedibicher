import json
import time
import os
from prettytable import PrettyTable


set_anno = "2000"
set_mese = "December"
set_day = "31"


table = PrettyTable()
table.field_names = (["nome", "eta"])

with open("deadge.json") as f:
    file = json.load(f)


def morti_anno_mese_giorno():
    table.title = f"Morti in {set_mese} {set_anno} giorno {set_day}"
    table.field_names = (["nome", "eta"])
    # stampo tabella persone giorno 1
    for person in file[set_anno][set_mese][set_day]:
        table.add_row([person['name'], person['age']])
        print(table)
        time.sleep(1)
        os.system("clear")
    print(table)


morti_anno_mese_giorno()
