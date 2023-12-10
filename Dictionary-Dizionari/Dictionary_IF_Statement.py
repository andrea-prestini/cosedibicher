# Elenco return funzione domanda
risposta1 = "Ciao amico mio"
risposta2 = "Ciao tutto bene nel paesello Gambara?"
risposta3 = "Buongiorno, come stanno le bambine?"
risposta4 = "Complimenti per i tuoi ultimi risultati scolastici!"
risposta5 = "Dovrei effettuare il cambio pastiglie dei freni..."
risposta6 = "Ci sono novità nella Valle Camonica?"
risposta7 = "Hai trovato una motocicletta di tuo gradimento?"
risposta8 = "Ci sono problemi di approvigionamento idrico!"
risposta9 = "Abbiamo attivato il processo di fatturazione elettronica?"
risposta10 = "Spero tu possa stare meglio per ritornare in palestra"

# Elenco risposte disponibili
RISPOSTE = {
    "andrea": risposta1,
    "mario": risposta2,
    "eleonora": risposta3,
    "federica": risposta4,
    "roberto": risposta5,
    "ancilla": risposta6,
    "simone": risposta7,
    "giuseppe": risposta8,
    "anna": risposta9,
    "claudio": risposta10,
}


def come_ti_chiami(nome: str) -> str:
    ''' La funzione controlla se la risposta è presente nel dizionario e risponde di conseguenza'''
    # Casting della variabile per ottenere una chiave dizionario compatibile nel caso di scrittura con lettere Maiuscole
    nome = nome.lower()
    if nome not in RISPOSTE.keys():
        return "Mi dispiace non ti conosco" # caso escluso dall'elenco risposte predefinite
    else:
        return RISPOSTE[nome]

# Poniamo la domanda al nostro utente
print(come_ti_chiami(input("Come ti chiami? ")))