class MyClass:
    def __init__(self):
        self.capacity = 1000
        print(self.capacity)


uno = MyClass.__new__(MyClass)
print(uno.capacity) # Errore perchè l'istanza non è stata creata!
