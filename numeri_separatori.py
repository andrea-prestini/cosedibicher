import os
import time


def decoratoreCornice(funzione):
    def wrapper(*args):
        return f'''
        Prezzo applicato al prodotto € {x}
        Quantità: {y}
        {"-" * 40}
        Totale spesa transazione:
        € {funzione(x,y):,.2f}'''
        
    return wrapper

@decoratoreCornice
def funzione(x, y):
    x = int(x)
    y = int(y)
    return (x * y)



lista = []

while True:
    ris = input("vuoi inserire i numeri? ")
    if ris == "n":
        print("Arrivederci...")
        
        break
    else:
        x = input("inserisci primo numero: ")
        y = input("inserisci secondo numero: ")
        lista.append((x,y))
        
    
    

os.system("clear")
print(lista)
totale = 0
for val in lista:
    x, y = val[0], val[1]
    print(funzione(x,y))
    time.sleep(2)
    totale = totale + (int(x) * int(y))
print()
print("Nel carrello abbiamo {} prodotti".format(len(lista)))
print(f"la spesa totale è € {totale:,.2f}")
