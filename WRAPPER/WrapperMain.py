from functools import wraps
from time import perf_counter, sleep


def decoratore(func):
    @wraps(func)
    def wrapper():
        risultato = func()
        wrapper.incartata = "Funzione decorata"
        if risultato.isdecimal():
            print("Sono in fase di analisi...")
            sleep(2)
            print("hai inserito un numero!")
        else:
            print("Sono in fase di analisi...")
            sleep(2)
            print("hai inserito una stringa!")
    return wrapper


def get_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.incartata = "Funzione decorata"
        start_time = perf_counter()
        func(*args, **kwargs)
        end_time = perf_counter()
        total_time = round(end_time - start_time, 2)
        print("Time", total_time, "seconds")
    return wrapper


@get_time
@decoratore
def miaFunzione():
    response = input("inserisci alcuni caratteri:\n")
    print("Ora ci penso e ripenso...")
    sleep(2)
    print("Hai inserito:", response)
    return response


def is_decorated(func):
    return getattr(func, "incartata", "Funzione NON decorata")


if __name__ == "__main__":
    miaFunzione()
    print("-" * 40)
    sleep(2)
    print("La tua funzione:", is_decorated(miaFunzione))
