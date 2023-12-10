lista = [1, 2, 3, 4, 5]

for val in lista:
    if val > 13:
        print(val)
        print("processo interrotto")
        break
else:
    print("processo terminato con successo")


print("-" * 50)

for val in lista:
    if val > 3:
        print("valore di STOP:", val)
        print("processo interrotto")
        break
else:
    print("processo terminato con successo")