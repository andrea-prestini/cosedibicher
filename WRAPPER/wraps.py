import time
from functools import wraps


def log_calls(func):
    fname = func.__name__

    @wraps(func)
    def logger(*args, **kwargs):
        print(fname, 'chiamata')
        return func(*args, **kwargs)
    return logger


@log_calls
def add(x, y):
    """Return the sum of x and y"""
    return x + y


print(add(1, 1))
print(add.__doc__)
print(add.__module__)


def my_caps_lock(funzione_parametro):
    @wraps(funzione_parametro)
    def wrapper():
        """ wrapper significa 'incarto, confezione' """
        return funzione_parametro().upper()
    return wrapper


@my_caps_lock
def mia_funzione():
    return "hello world!"


def caps_lock(funzione_parametro):
    @wraps(funzione_parametro)
    def wrapper(*args, **kwargs):
        """ wrapper significa 'incarto, confezione' """
        return funzione_parametro(*args, **kwargs).upper()
    return wrapper


@caps_lock
def echo(msg):
    return msg


# ----------------------------------------------------------------------


def decoratore(func):
    @wraps(func)
    def wrapper():
        risultato = func()
        # inserisco una proprietà da verificare con apposita funzione
        # attenzione alla sintazzi nome.proprietà
        # senza il punto avremmo una assegnazione di valore a variabile!
        wrapper.incartata = True
        if risultato.isdecimal():
            print("Sono in fase di analisi...")
            time.sleep(2)
            print("hai inserito un numero...")
        else:
            print("Sono in fase di analisi...")
            time.sleep(2)
            print("hai inserito una stringa...")
    return wrapper


@decoratore
def miaFunzione():
    response = input("inserisci alcuni caratteri: ")
    return response


# funzione di verifica incartamento
# se la proprietà incartata è presente (getattr) allora la funzione è incartata
# se la proprietà non è presente la funzione non è incartata
def is_decorated(func):
    return getattr(func, "incartata", False)


miaFunzione()
print("-" * 50)
print(is_decorated(miaFunzione))
