#!/usr/bin/python3
while True:
    print('''
        Benvenuto nel programma CALCOLATRICE!
        creato da Andrea Prestini

        Di seguito un elenco delle opzioni disponibili:



        - per ADDIZIONE  seleziona           1
        - per SOTTRAZIONE seleziona          2
        - per MOLTIPLICAZIONE seleziona      3
        - per DIVISIONE seleziona            4
        - per calcolo ESPONENZIALE seleziona 5
        - per uscire dal programma seleziona ESC
        ''')
    print()
    print()
    scelta = input("inserisci il numero corrispondente all'azione desiderata ")

    if scelta == "1":
        print("\nHai scelto ADDIZIONE\n")
        a = int(input("digita il primo valore -->  "))
        b = int(input("digita il secondo valore-->  "))
        print("il risultato dell'operazione è: ", (a+b))
    elif scelta == "2":
        print("\nHai scelto SOTTRAZIONE\n")
        a = int(input("digita il primo valore -->  "))
        b = int(input("digita il secondo valore-->  "))
        print("il risultato dell'operazione è: ", (a-b))
    elif scelta == "3":
        print("\nHai scelto MOLTIPLICAZIONE\n")
        a = int(input("digita il primo valore -->  "))
        b = int(input("digita il secondo valore-->  "))
        print("il risultato dell'operazione è: ", (a*b))
    elif scelta == "4":
        print("\nHai scelto DIVISIONE\n")
        a = int(input("digita il primo valore -->  "))
        b = int(input("digita il secondo valore-->  "))
        print("il risultato dell'operazione è: ", (a/b))
    elif scelta == "5":
        print("\nHai scelto CALCOLO ESPONENZIALE\n")
        a = int(input("digita il primo valore -->  "))
        b = int(input("digita il secondo valore-->  "))
        print("il risultato dell'operazione è: ", (a**b))
    elif scelta == "esc":
        print("Hai scelto di uscire dal programma")
        print("arrivederci")
        break
    ciclo = input("vuoi continuare a fare i calcoli? (y/n)\n")
    if ciclo == "y":
        print('''
              Torno al menu principale
++++++++++++++++++++++++++++++++++++++++++++++++++
              ''')
        continue
    else:
        print('''
grazie per aver usato la nostra appliazione, ARRIVEDERCI
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
              ''')
        break
