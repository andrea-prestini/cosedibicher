''' Siamo degli agenti e fermiamo una macchina che ha 4 passeggeri. Vogliamo controllare il contenuto delle tasche dei nostri quattro passeggeri e conteggiare i vari elementi che hanno in tasca.
Se la quantità supera il limite importo, il programma invierà un segnale all'utente per applicare il fermo cautelare
'''
'''
# Sugar
p1_sugar = 0
p2_sugar = 0
p3_sugar = 0
p4_sugar = 0

# Armi
p1_armi = 0
p2_armi = 0
p3_armi = 0
p4_armi = 0
'''

# usiamo le liste

sugar = [10, 5, 7, 9]
armi = [ 1, 2, 0, 0]
soldi = [10, 50, 65, 24]

lista_sugar = len(sugar)
lista_armi = len(armi)
lista_soldi = len(soldi)

for i in range(len(sugar)):
    print(sugar[i])
print("=" *30)

'''
for i in range(amici):
    if i == 0 or i == 1:
        print(amici[i])
Il problema di questa forma è che si eseguono (in caso di lista con 1000 elementi, tutti i 998 cicli prima di ottenere output, si sprecano risorse. Nel caso precedente stoppiamo il tutto dopo 2 cicli!)
'''
indici_che_ci_interessano = [0, 2]

for i in indici_che_ci_interessano:
    print(sugar[i])
print("=" * 30)

if 10 in sugar:
    print("presente")
else:
    print("assente")
print("=" * 20)


# lo slicing delle LISTE
print("tutti tranne ultimo")
print(sugar[:-1])
print("-" * 20)
print("il primo ed il secondo")
print(sugar[0:2])
print("-" * 20)
print("dal terzo alla fine della lista")
print(sugar[2:])
print("-" * 20)

# leggiamo la lista al contrario
print(sugar[::-1])
print("-" * 20)
for i in reversed(sugar):
    print(i)

# amici.reverse() la lista viene invertita IN PLACE

# reversed si usa solo come iterabile...


