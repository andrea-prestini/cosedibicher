def decoratore_M(funzione):
    def wrapper(*args):
        return funzione(*args).upper()
    return wrapper

def decoratore_C(funzione):
    def wrapper(*args):
        return                               funzione(*args).capitalize()
    return wrapper

def decoratore_Testo(funzione):
    def wrapper(*args):
        return f'''
        Ciao amico mio
        {funzione(*args)}
        ci vedremo presto'''
    return wrapper


@decoratore_Testo
def miaFunzione(text):
    return text



print(miaFunzione("bicher the one"))