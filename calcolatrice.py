print('''
      Benvenuto nel programma calcolatrice
      creato da Andrea Prestini
      Di seguito un elenco delle funzioni disponibili:
      - per effettuare un'addizione seleziona 1
      - per effettuare una sottrazione seleziona 2
      - per effettuare una moltiplicazione seleziona 3
      - per effettuare una divisione seleziona 4
      - per uscire seleziona 0''')


operazione = input("seleziona l'operazione che vuoi eseguire\n")

if operazione == "1":
    print("hai scelto addizione")
    a = int(input("inserisci il primo valore\n"))
    b = int(input("inserisci il secondo valore\n"))
    print("il risultato è", (a+b))
elif operazione == "2":
    print("hai scelto la sottrazione")
    a = int(input("inserisci il primo valore\n"))
    b = int(input("inserisci il secondo valore\n"))
    print("il risultato è", a-b)
elif operazione == "3":
    print("hai scelto la moltiplicazione")
    a = int(input("inserisci il primo valore\n"))
    b = int(input("inserisci il secondo valore\n"))
    print("il risultato è", a*b)
elif operazione == "4":
    print("hai scelto la divisione")
    a = int(input("inserisci il primo valore\n"))
    b = int(input("inserisci il secondo valore\n"))
    print("il risultato è", a//b)
    print("il resto della divisione è", a % b)
elif operazione == "0":
    print("arrivederci e grazie")
