'''
Interrogazione in diretta su Discort con Enkk
'''

def fDizionario(x, y):
    dizionario = {}
    dizionario[x] = y 
    print("il tuo dizionario è: ", dizionario)


fDizionario("andrea", "esine")

print("=" * 50)


'''
Troviamo il massimo valore presente tra 2 liste fornite
'''

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 3, 5, 7]

# Versione sintentica che usa la somma di liste per crearne una con tutti i valori
print("Versione sintetica")
print("il valore massimo è", max(lista1+lista2))

print("-" * 50)

print("Versione esplicita")
if max(lista1) > max(lista2):
    print("il valore massimo è", max(lista1))
else:
    print("il valore massimo è", max(lista2))
