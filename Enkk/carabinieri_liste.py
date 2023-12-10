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

# i limiti legali
max_sugar = 12
max_armi = 0
max_soldi = 3000

# Sugar dei 4 in macchina
sugar = [10, 5, 7, 9]

# Armi dei 4 in macchina
armi = [ 1, 2, 0, 0]

# Soldi dei 4 in macchina
soldi = [10, 50, 65, 24]

# risultato ispezione
tot_sugar = 0
tot_armi = 0
tot_soldi = 0

for s in range(len(sugar)):
    tot_sugar += sugar[s]
    tot_armi += armi[s]
    tot_soldi += soldi[s]

# lo stesso risultato si ottiene nel formato tot_sugar = sum(sugar)... etc

# possiamo riutilizzare la s perchè è una variabile locale, all'interno del ciclo for dove viene utilizzata

print(f'''
     totale sugar: {tot_sugar} grammi
     totale armi: {tot_armi} pezzi
     totale soldi: {tot_soldi} euro
     ''')

if tot_sugar > max_sugar:
    print("troppo sugar... IN ARRESTO")
else:
    print("sugar OK... libero!")
if tot_armi > max_armi:
    print("troppe armi... IN ARRESTO")
else:
    print("armi OK... libero!")
if tot_soldi > max_soldi:
    print("troppi soldi... IN ARRESTO")
else:
    print("soldi OK... libero!")

