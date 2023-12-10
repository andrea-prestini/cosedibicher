''' Siamo degli agenti e fermiamo una macchina che ha 4 passeggeri. Vogliamo controllare il contenuto delle tasche dei nostri quattro passeggeri e conteggiare i vari elementi che hanno in tasca.
Se la quantità supera il limite importo, il programma invierà un segnale all'utente per applicare il fermo cautelare
'''

# Soglie consentite SENZA i CANNONI
max = {
    "sugar": 12,
    "armi": 0,
    "soldi": 3000,
    "pastiglie": 5,
    #"cannoni": 1
}

# Contenuto della macchina
macchina = {
    "sugar": [10, 5, 7, 9, 9],
    "armi": [1, 2, 0, 0, 0],
    "soldi": [10, 50, 65, 24, 0],
    "pastiglie":[4, 0, 0, 0],
    "cannoni": [1, 1, 0, 0]
}


'''
for key, value in macchina.items():
  tot = 0
   for i in range(len(value)):
      tot = value[i]
  tot_macchina[key] = tot
'''

# Calcoliamo la sommatoria per ogni oggetto trovato in tasca
tot_macchina = {}
for k, v in macchina.items():
    tot_macchina[k] = sum(v)

# Stampa risultati perquisizione macchina
for k, v in tot_macchina.items():
    print(f'''
          chiave: {k.upper()}
          valore: {v}''')
print("-" * 40)

# Verifica arresto occupanti macchina 
try:
    for k in tot_macchina.keys():
        if tot_macchina[k] > max[k]:
            print("soglia %s superata... ARRESTO!" %(k.upper()))
        else:
            print("tutto a posto per %s... LIBERO!" %(k.upper()))
except:
    print("massimale %s non trovato!" %k)
else:
    print("verificati TUTTI gli elementi con successo!")