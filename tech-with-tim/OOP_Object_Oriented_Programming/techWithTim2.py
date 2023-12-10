import time


class Pet:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def show(self):
        print(f"""
              Animale: {self.name}
              Età: {self.age}
              """)


class Dog(Pet):
    def __init__(self, name, age, verso):
        super().__init__(name, age)
        self.verso = verso

    def speak(self):
        print(self.verso)

    def show(self):
        return f'''
    Animale: {self.name}
    Età: {self.age}
    Verso: {self.verso}
    '''


class Cat(Pet):
    def __init__(self, name, age, verso):
        super().__init__(name, age)
        self.verso = verso

    def speak(self):
        print(self.verso)

    def show(self):
        return f'''
    Animale: {self.name}
    Età: {self.age}
    Verso: {self.verso}
    '''


p1 = Cat("gatto", 11, "Miao")
p2 = Dog("cane", 5, "Bau")

print(p1.show())
time.sleep(2)
print(p2.show())
print("procedura terminata!")
