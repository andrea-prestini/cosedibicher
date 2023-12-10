'''
funzione unaria
funzione binaria
funzione ternaria
etc. in funzione dei parametri richiesti
Quando chiamiamo una funzione passiamo argomenti che vengono trasferiti ai parametri della stessa
'''

# Calcola la media aritmetica di 2 valori
def fconto(x, y):
    z = (x + y) / 2
    return z

# Abbellisce una stampa con dei bordini
def fprint_ma_bella(str):
    print("==================")
    print(str.upper())
    print("==================")

'''
la funzione print_ma_bella non ha un valore di ritorno per il chiamante
Procedura:
1- crea il frame della funzione
2 -passa gli argomenti ai parametri, per posizione
3 -esegue le cose
4- restituisce eventualmente il risultato
5- passa il risultato al frame chiamante
6- la funzione ed il suo contenuto (variabili etc.) MUOIONO
'''

# Esegue semplice moltiplicazione, paramentro default 10
def fmoltiplica(x, y=10):
    z = x * y
    return z

print("fornisco un solo paramentro:", fmoltiplica(3))
print("fornisco 2 parametri espliciti:", fmoltiplica(10, 5))
print("fornisco 2 parametri precisi:", fmoltiplica(x=10, y=7))