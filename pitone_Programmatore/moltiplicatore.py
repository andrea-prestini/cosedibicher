def moltiplicatore(times):
    def deco(func):
        def inner(*args):
            for x in range(times):
                func(), print("Andrea")
        return inner
    return deco

@moltiplicatore(5)
def stampa():
    print("ciao amico mio...",end=" ")





stampa()