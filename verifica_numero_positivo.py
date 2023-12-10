def num_verify(x):
    """
    Verifico che il valore inserito sia un numero; se True
    Casting str -> int e restituisco il valore,
    se False eccezzione e messaggio per l'utente

    Args:
        x (): str

    Returns: x -> int

    """

    try:
        int(x)
        if int(x) > 0:
            return int(x)
        else:
            print("Deve essere un numero positivo...")
    except ValueError:
        print("Inserimento testo non ammesso...")
        return False


check = True

while check:
    answer = input("inserisci un numero: ")
    if num_verify(answer):
        answer_number = num_verify(answer)
        print("Modifico il valore inserito:", (answer_number + 100))
        check = False
    else:
        print("ERRATO!")
