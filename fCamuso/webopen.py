import webbrowser
import time


destinazione = input("Dove vuoi andare?\n")
time.sleep(1)
print("Ti porto dove hai richiesto...")
webbrowser.open("https://www.google.com/maps/place/" + destinazione)
