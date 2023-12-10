dizionario = {"casa": "esine",
              "nome": "andrea",
              "stato": "italia",
              "regione": "lombardia"}


ordinato = sorted(dizionario.items(), key=lambda x: x[0])

print(ordinato)