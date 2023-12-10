personale = [
    {
        "operaio1": {
            "nome": "andrea",
            "cognome": "prestini",
            "paese": "Esine"
        }
    },
    {
        "operaio2": {
            "nome": "eleonora",
            "cognome": "favagrossa",
            "paese": "Leno"
        }
    },
    {
        "operaio3": {
            "nome": "Aldo",
            "cognome": "Tanzini",
            "paese": "Breno"
        }
    },
    {
        "operaio4": {
            "nome": "Roberto",
            "cognome": "Tanzini",
            "paese": "Breno"
        }
    },
    {
        "operaio5": {
            "nome": "Filippo",
            "cognome": "Braccagnini",
            "paese": "Breno"
        }
    },
]

print("PRIMA Versione")
for val in personale:
    for k, v in val.items():
        print(f"""
              qualifica: {k}
              nome: {v["nome"]}
              cognome: {v["cognome"]}
              paese: {v["paese"]} wS
              """)

print("SECONDA versione")
for val in personale:
    for k, v in val.items():
        print("qualifica: {}".format(k))
        print("nome: {}".format(v["nome"]))
        print("cognome: {}".format(v["cognome"]))
        print("paese {}".format(v["paese"]))
        print("-" * 50)


print(f'''
La nostra azineda impiega {len(personale)} operai...)