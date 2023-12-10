class Meta(type):

    def __new__(cls, class_name, bases, attrs):
        def show():
            return 'stampo la scheda della classe'

        def testo():
            return 'abbiamo del testo da aggiungere...'
        attrs[show.__name__] = show
        attrs[testo.__name__] = testo
        return super(Meta, cls).__new__(cls, class_name, bases, attrs)


class Fruit(metaclass=Meta):
    color = "Green"


print(Fruit.color)
print(Fruit.show())
print(Fruit.testo())
