import time


class MyClass(object):
    limit = 10

    def __init__(self):
        self.data = []

    def item(self, i):
        return self.data[i]

    def add(self, e):
        if len(self.data) >= self.limit:
            raise Exception("Too many elements")
        self.data.append(e)


print("il limite come attributo di CLASSE")
time.sleep(2)
print(MyClass.limit)

foo = MyClass()
time.sleep(1)
print("il limite come attributo di ISTANZA")
print("NON modificato lo prende dalla classe -> namespacing")
time.sleep(1)
print("limite di classe senza limite di istanza", foo.limit)

foo.limit = 100
time.sleep(1)
print("dopo aver modificato quello di istanza viene intercettato!")
print("limite di istanza prima di limite di classe", foo.limit)
