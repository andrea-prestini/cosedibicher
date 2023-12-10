""" Soluzione 1
guess = 1
    while True:
        num = input("Indovina il numero (0-100)")
        try:
            num = int(num)
        except ValueError:
            print("Invalid number, insert again...")

        if num < 45:
            print("Your guess was under.")
        elif num > 45:
            print("Your gess was over.")
        else:
            break

        guess += 1

    print(f'You guessed it in {guess} guesses')
"""
"""
    guess = 1
    NUMBER = 45

    while True:
        num = input("Indovina il numero (0-100)")
        try:
            num = int(num)
        except ValueError:
            print("Invalid number, insert again...")

        if num < NUMBER:
            print("Your guess was under.")
        elif num > NUMBER:
            print("Your gess was over.")
        else:
            break

        guess += 1

    print(f'You guessed it in {guess} guesses')
"""
"Soluzione 2 con classi"

# Semplification: metodi o funzioni che eseguono bene una ed una sola cosa
# anche il debugging risulta più semplice potendo testare singolarmente
# cosa succede all'interno del codice (verifica dei side effects)


class GuessNumber:
    def __init__(self, number, mn=0, mx=100):
        self.number = number
        self.guesses = 0
        self.min = mn
        self.max = mx

    def get_guess(self):
        guess = input(f"Please guess a number ({self.min} - {self.max})")

        if self.valid_number(guess):
            return int(guess)
        else:
            print("Please enter a valid number...")
            return self.get_guess()

    def valid_number(self, str_number):
        try:
            number = int(str_number)
        except ValueError:
            return False

        return self.min <= number <= self.max

    def play(self):
        while True:
            self.guesses += 1

            guess = self.get_guess()

            if guess < self.number:
                print("You guess was under.")
            elif guess > self.number:
                print("You guess was over")
            else:
                break


game = GuessNumber(56, 0, 100)
game.play()
