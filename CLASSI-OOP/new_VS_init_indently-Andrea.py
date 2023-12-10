import time


class Connessione_1:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print(f'Connecting Connessione_1 ... ID: {id(cls._instance)}')
        else:
            print(f'WARNING: already connected Connessione_1! ID: {id(cls._instance)}')


class Connessione_2:
    _instance = None

    def __init__(self) -> None:
        if Connessione_2._instance is None:
            Connessione_2._instance = "Connessione"
            print(f'Mi connetto con ID: {id(Connessione_2._instance)}')
        else:
            print(f'Uso connessione esistente... ID: {id(Connessione_2._instance)}')


uno = Connessione_1()
time.sleep(2)
due = Connessione_1()
print("-" * 50)
time.sleep(2)
tre = Connessione_2()
time.sleep(2)
quattro = Connessione_2()


