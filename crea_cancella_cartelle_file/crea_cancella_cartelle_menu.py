from ast import match_case
import os
import shutil
import time

def create(nome):
    ''' modulo creazione cartella da nome inserito'''
    print("creo la cartella come richiesto")
    print()
    time.sleep(2)
    os.mkdir(nome)
    time.sleep(2)
    print(f"ho creato la cartella {nome}")
    print()
    print(list(filter(lambda x: os.path.isdir(x), os.listdir("."))))


def delete(nome):
    '''modulo cancellazione cartella da nome inserito'''
    print("CANCELLO la cartella come richiesto")
    print()
    time.sleep(2)
    shutil.rmtree(nome)
    time.sleep(2)
    print(f"ho rimosso la cartella {nome}")


risp = input("vogliamo cominciare?\n")
print(list(filter(lambda x: os.path.isdir(x), os.listdir())))

if risp == "y":
    r_menu = input('''                                                          
    1 - Crea cartella                                                           
    2 - Cancella cartella\n''')

    if r_menu == str(1):
        nome = input("nome della cartella\n")
        create(nome)
    else:
        try:
            nome = input("nome della cartella\n")
            delete(nome)
        except:
            print("errore nome cartella...")
else:
    print("arrivederci")

