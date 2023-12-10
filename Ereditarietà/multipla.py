class Human:

    def __init__(self, age, name) -> None:
        self.age = age
        self.name = name


class Scuola:

    def __init__(self, materia) -> None:
        self.materia = materia


class Student(Human, Dancer):
    def __init__(self, age, name, materia) -> None:
        Human.__init__(self, age, name)
        Scuola.__init__(self, materia)


uno = Student(25, "Federica", "Lingue")
print(uno.name)
print(uno.age)
print(uno.materia)
