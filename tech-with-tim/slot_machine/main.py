def deposit():
    'chiediamo importo da inserire nella macchinetta'

    while True:
        amount = input("Quanto vuoi depositare? Euro: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Devi versare una somma maggiore di 0.")
        else:
            print("Inserisci un numero.\n")

    return amount


print("Hai inserito: Euro", deposit())
print("Doc della funzione:\n", deposit.__doc__)
