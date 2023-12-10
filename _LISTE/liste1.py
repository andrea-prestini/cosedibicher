elenco = [10, "andrea", "pietro", "casa", 34, "analisi"]  # lista ordinata
elenco[0] = "albero"
lista_lista = [1, 5, "pietro", ["casa", "bicher", "piadina"]]
elenco.append("BICHER")

print(elenco)
print(elenco[-1])
print(elenco[1])
print(elenco[0:2])
print(elenco[2:])

print("-"*50)

for valore in elenco:
    print("abbiamo trovato questo elemento:\n" + str(valore))


print("-"*50)
print("creiamo una lista...")
scatola = list(range(30))
print(scatola)
# le liste sono flessibili, possono contenere anche altre liste!
print("eliminiamo un elemento")
elenco.remove("BICHER")
print(elenco)

print("-"*50)
print("Adesso le TUPLE")
tuple1 = ("primo", "secondo")
tuple2 = "primo", "secondo"
print(tuple2)
print(tuple1)
# le TUPLE sono FISSE, non modificabili!
# iterare una tupla è molto più veloce rispetto alle liste
numeri_tpl = (1, 3, 45, 22, 11)
print(max(numeri_tpl))
print(min(numeri_tpl))

print(numeri_tpl.index(3))# se 3 è presente ci restituisce la posizione, altrimenti ValueError
print(numeri_tpl.count(3))# restituisce le occorrenze del valore tra parentesi,
# se non presente il risultato sarà 0

nome_str = "andrea"
print(list(nome_str))# crea una lista con ogni lettera della stringa
print(tuple(nome_str))# crea una tupla con ogni lettera della stringa

print(lista_lista[3][2])  # piadina prendendolo da un elemento lista della lst
print(list(reversed(elenco)))