def myFunction(myparameter: int):
    print(myparameter)


if __name__ == "__main__":
    myFunction("ciao")

"""
Usiamo mypy per lanciare il codice: otterremo
un'analisi della tipizzazione
variabili rispetto a quanto inserito
come parametro; se non conforme verrà visualizzato
un messaggio di errore!
"""
