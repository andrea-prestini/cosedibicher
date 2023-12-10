
import time
check = True
print('''
      Benvenuto al lancio del nostro razzo!

      Adesso inizieremo il conto alla rovescia, poi, al termine, potrai decidere
      se far partire un altro razzo oppure abbandonare la missione...
      A te la scelta migliore!

      Buon divertimento...

      si parte.........................
      ''')
print("premi invio per far partire il primo RAZZO!")
input()
while check is True:
    for number in range(20, 0, -1):
        print(str(number) + " elemento pronto")
        time.sleep(1)
    print("PARTENZA...")
    print("Bene adesso vediamo cosa fare...")
    print('''
          Decidi tu cosa vuoi fare, far partire un nuovo razzo per aiutare il precedente
          oppure lasciar perdere la missione e rivedere le informazioni di bordo
          quando saranno disponibili!

          Attento perchè ogni decisione avrà delle conseguenze!
          ''')
    risposta = input("vuoi continuare' (s/n) ")
    if risposta == "s":
        print("bene, ricominciamo...")
    else:
        print("ok ci vedremo per un altro lancio!")
        check = False
