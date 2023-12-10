import requests
import json
import os
import numpy as np

ARTIST_BASE_URL = "https://api.deezer.com/artist/"

with open("../data/artists.json", "r") as f:
    artists = json.load(f)


while True:
    two_artists = (np.random.choice(list(artists.keys()), 2)) # random choice sceglie tra elementi di una lista, non dict_keys
    two_artists = two_artists.tolist()

# creare input chiedendo 2 autori
    user_answer = input("Chi ha pubblicato più album tra {} (1) e {} (2): ".format(two_artists[0], two_artists[1]))
    # user_answer = int(user_answer)

    if user_answer not in ["1", "2"]:
        raise Exception("Risposta non accettata")


# funzione accesso API e ricava i dati dei 2 artisti
    def get_album(artistID):
        a_name = requests.get(ARTIST_BASE_URL + str(artistID)).json()["name"]
        a_album = requests.get(ARTIST_BASE_URL + str(artistID)).json()["nb_album"]
        return a_album

    artistID1 = artists[two_artists[0]]
    artistID2 = artists[two_artists[1]]

# confrontare i valori e trovare la risposta corretta
    winner = "" 
    if get_album(artistID1) > get_album(artistID2):
        print(f"risultato {two_artists[0]} con {get_album(artistID1)} album")
        print(f"contro {two_artists[1]} con {get_album(artistID2)} album")
        winner = "1"
    else:
        print(f"risultato {two_artists[1]} con {get_album(artistID2)} album")
        print(f"contro {two_artists[0]} con {get_album(artistID1)} album")
        winner = "2"

# confrontare risposta corretta con quella fornita dall'utente, feedback finale
    if user_answer == "1":
        print("risposta {}: {}".format(user_answer, two_artists[0]))
    else:
        print("risposta {}: {}".format(user_answer, two_artists[1]))

    
    
    sol_feedback = "You WIN" if user_answer == winner else "You LOOSE!" 
    sol_feedback += "\nVuoi continuare s/n? "
    
    check = input(sol_feedback)
    if check == "n":
        break
    else:
        os.system("clear")