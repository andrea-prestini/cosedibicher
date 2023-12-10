def get_guess():
    guess = input("inserisci un numero: ")
    min = 0
    max = 100

    def valid_number(str_number):
        try:
            number = int(str_number)
        except ValueError:
            return False
        return min <= number <= max

    if valid_number(guess):
        return 'hai inserito: {}'.format(int(guess))
    else:
        print(f"solo numeri compresi nell'intervallo {min}-{max}...")
        return get_guess()


print(get_guess())
