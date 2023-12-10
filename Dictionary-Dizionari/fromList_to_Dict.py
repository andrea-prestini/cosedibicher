lista = ["andrea prestini", "mario mometto", "anna ferrari"]

elenco = {}


for x in range(len(lista)):
    elenco[x] = lista[x]
    


print("questo è elenco",elenco)


scatola = {i:lista[i] for i in range(len(lista))}
print("questa è scatola", scatola)

           
