from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def show(self):
        pass


class Laptop(Computer):
    def process(self):
        print("Running...")


class Workstation(Computer):
    def process(self):
        print("Workstation calculating...")

    def show(self):
        print("Very hard computation")


try:
    comp = Laptop()
except Exception as e:
    print(e)
    print("Verifica i metodi della classe istanziata...")
finally:
    pass



