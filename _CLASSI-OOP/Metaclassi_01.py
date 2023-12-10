class Foo:
    def show(self):
        print("Ciao")


def add_attribute(self):
    self.z = 99
    print("ritorno il valore z:", self.z)


Test = type("Persona", (Foo,), {"x": 5, "add_attribute": add_attribute})

t = Test()
t.add_attribute()
print("accedo direttamente al valore z di t", t.z)
