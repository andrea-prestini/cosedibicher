def controllaSeIndovinato(tentativo, numero):
    if tentativo == numero:
        print("indovinato!")
        return True
    elif tentativo < numero:
        print("troppo piccolo...")
    elif tentativo > numero:
        print("troppo grande...")

    return False