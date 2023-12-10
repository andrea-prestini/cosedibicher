# from glob import glob
import webbrowser
import time
# from random import choice
from pyttsx3 import init
from speech_recognition import Recognizer, Microphone

engine = init()
voices = engine.getProperty("voices")
# Versione con voce da Mac = id 1
# Versione con voce da linux = id 41
engine.setProperty("voice", voices[1].id)
engine.say("che cavolo vuoi?")
engine.runAndWait()


risposta = "ESPRIMITI MEGLIO, DANNAZIONE!"

r = Recognizer()


with Microphone() as source:
    print("pronto ad ascoltare...")
    audio = r.listen(source)
    testo = r.recognize_google(audio, language="it-IT")

    print(testo)

    # richieste
    if "ricetta" in testo:
        risposta = "non sei capace di cucinare, vai al ristorante"

    elif any(parola in testo for parola in ["ore", "ora", "orario"]):
        risposta = "vai a comprarti un orologio"
        time.sleep(2)
        webbrowser.open("https://www.amazon.it/s?k=orologio rolex")

    elif any(parola in testo for parola in ["Come", "Quanto", "Cosa"]):
        risposta = "che cazzo ne sò, chiedi ad Alexa"

    elif any(parola in testo for parola in ["Cerca", "Google"]):
        risposta = "prova a chiedere al mio amico google"
        time.sleep(1)
        webbrowser.open("https://www.google.it/")

    elif any(parola in testo for parola in [
        "andare", "mappa", "cartina", "GPS",
        "percorso", "traffico"
    ]):
        risposta = "ti faccio cercare con il navigatore, inserisci il luogo perchè me lo sono dimenticato"
        webbrowser.open("https://www.google.it/maps")

    engine.say(risposta)
    engine.runAndWait()
