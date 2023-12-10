from abc import (ABCMeta, abstractmethod)


class Vehicle(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def change_gear(self):
        pass

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model, color) -> None:
        self.make = make
        self.model = model
        self.color = color


car = Car("Toyota", "Avensis", "silver")
print(car.make)
print(car.model)
print(car.color)
print(car.start_engine())
