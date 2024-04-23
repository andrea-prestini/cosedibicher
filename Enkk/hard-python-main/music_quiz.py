risposta_utente = int(input("Inserisci un numero: "))

feedback_risposta = "bravo" if risposta_utente > 10 else "sbagliato!"
feedback_risposta += "\nVuoi ripetere il test? (y)\n"

what = input(feedback_risposta)
feedback_what = "allora andiamo avanti" if what == "y" else "Arrivederci!"

print(feedback_what)
