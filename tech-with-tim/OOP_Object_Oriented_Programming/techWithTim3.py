import time


class Person:

    number_of_people = 0
    GRAVITY = 9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return f'Nella stanza sono presenti {cls.number_of_people} persone'

    @classmethod
    def add_person(cls):
        print("Aggiunta 1 persona...")
        cls.number_of_people += 1


p1 = Person("tim")
time.sleep(2)
p2 = Person("jim")
time.sleep(2)
p3 = Person("Andrea")

time.sleep(2)
print(Person.number_of_people_())
