import pprint



elenco_prova = {"key":"andrea", "key1":"prestini"}
elenco = {"nome":"andrea","cognome":"prestini"}
print(elenco["nome"])
print(elenco["cognome"])
elenco["città"] = "Esine"
elenco["via"] = "BICHER"
print(elenco)
#per cancellare del elenco["nome"] elimina la coppia chiave valore
print(elenco.keys())#ci mostra le chiavi presenti nel dizionario
print(elenco.values())#ci mostra i valori presenti nel dizionario
print(elenco.items())#ci mostra tutto il contenuto del dizionario
nomi = list(elenco.values())
print(list(elenco.values()))#abbiamo ottenuto una lista dei valori del dizionario

print("-"*100)
for chiave, valore in elenco.items():
    print("chiave: " + chiave + " | valore: " + str(valore)) 
print("="*100)
for chiave, valore in elenco.items():
    pprint.pprint(chiave)#pprint modulo per stampa dei dizionari migliore di print 
    pprint.pprint(valore)
print("="*100)
for chiave, valore in elenco.items():
    print(pprint.pformat(chiave))#pprint modulo per stampa dei dizionari migliore di print 
    print(pprint.pformat(valore))#pprint modulo per stampa dei dizionari migliore di print 
print("="*100)



print(elenco.get("colore", "CHIAVE non trovata"))
#strumento dei dizionari per cercare una chiave e restituire un messaggio di errore nel caso
#in cui non sia presente
elenco.setdefault("sesso","maschio")
#cerca la chiave e se non presente la crea con il valore definito nel modulo
# sesso non era una chiave presente, ha cercato e non trovandola l'ha creata
#assegnandole come valore quello passato dal nostro codice 
print(elenco)

