'''
Interrogazione in diretta su Discort con Enkk
'''

lista = []
new = 0
old = 0


while True:
    new = int(input("inserisci un numero "))
    if len(lista) == 0:
        lista.append(new)
    else:
        if new > old:
            old = new -1
            lista.append(new)
        else:
            break


print("la lista inserita è:\n",lista)

'''
Versione Enkk
'''


lista = []
new = 0
old = 0
proc = True

while proc:
    new = int(input("inserisci un numero "))
    if len(lista) == 0:
        lista.append(new)
    else:
        if new > old:
            old = new -1
            lista.append(new)
        else:
            proc = False


print("la lista inserita è:\n",lista)
