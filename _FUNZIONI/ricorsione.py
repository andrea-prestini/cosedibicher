import time


def ricorri(x):
    for val in x:
        if isinstance(val, list):
            ricorri(val)
        else:
            print(val)
            time.sleep(1)


lista = [1, 2, 3, ["uno", "due", "tre"], 4, 5, ["sei", "sette", "otto"], 9, 10]

ricorri(lista)
