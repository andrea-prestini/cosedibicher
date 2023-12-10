class UppercaseTuple(tuple):
    """
    classe che genera un errore tentando di modificare un
    oggetto immutable (tupla) dopo
    averlo creato con init
    """

    def __init__(self, iterable) -> None:
        print(f'init {iterable}')
        for i, arg in enumerate(iterable):
            self[i] = arg.upper()


class UppercaseTupleNew(tuple):
    """
    classe che utilizzando il metodo new prima di init permette di  modificare
    un oggetto immutabile quale la tupla
    """

    def __new__(cls, iterable):
        upper_iterable = (s.upper() for s in iterable)
        return super().__new__(cls, upper_iterable)


uno = UppercaseTupleNew(['andrea', 'prestini'])
print(uno)

due = UppercaseTuple(['andrea', 'prestini'])
print(due)
