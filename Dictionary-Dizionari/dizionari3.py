name_us = {
    2010: {1: "andrea", 2: "mario", 3: "anna"},
    2011: {1: "paolo", 2: "francesco", 3: "silvia"},
    2012: {},
    2013: {3: "valerio", 2: "tiberio", 1: "roberto"}
}

for year in name_us:
    if name_us[year] == {}:
        print(year, "nessun nome presente nella lista")
    else:
        for rank in sorted(name_us[year])[:1]:
            print(year, "primo nome dizionario--> ", name_us[year][rank].upper())

#creare una lista di chiavi per un dizionario:
for a in anni:
    dizionario[a] = dict.fromkeys(chiavi,"") #il secondo argomento definisce il valore della chiave!