class Meta(type):
    def __new__(cls, class_name, bases, attrs):
        print(attrs)
        return type(class_name, bases, attrs)


class Dog(metaclass=Meta):
    color = "black"
    name = "kitty"

    def hello(self):
        print("Ciao amico mio...")


d = Dog()


""" Risultato esecuzione codice
{'__module__': '__main__', '__qualname__': 'Dog', 'color': 'black', 'name': 'kitty', 'hello': <function Dog.hello at 0x7f65e15c5e50>}

"""
        
