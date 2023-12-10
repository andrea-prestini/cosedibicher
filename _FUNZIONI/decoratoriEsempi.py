def decoratore_P(funzione):
    def wrapper():
        return f'''
        prima della funzione
        {funzione()}
        dopo la funzione'''
    return wrapper


def decoratore_M(funzione):
    def wrapper():
        return funzione().upper()
    return wrapper


def decoratore_C(funzione):
    def wrapper():
        return funzione().capitalize()
    return wrapper


def decoratore_checkTesto(funzione):
    def wrapper(*args):
        ris = input("cosa vuoi verificare?\n")
        if funzione(*args) == ris:
            return 'Corretto'
        else:
            return 'ERRATO'
    return wrapper


def decoratore_checkNumero(funzione):
    def wrapper(*args):
        ris = input("numero:\n")
        if funzione(*args) == int(ris):
            return 'CORRETTO'
        else:
            return 'ERRATO'
    return wrapper


def decoratore_Sost(funzione):
    def wrapper(*args):
        ris = input("quale valore? \n")
        if funzione(*args) != ris:
            return ris
    return wrapper


@decoratore_Sost
def funzione_calcolo(x, y):
    return x * y


print(funzione_calcolo(10, 10))
