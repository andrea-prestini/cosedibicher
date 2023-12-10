class Client:

    _loaded = {}
    _db_file = "file.db"

    def __new__(cls, client_id):
        if (client := cls._loaded.get(client_id)) is not None:
            print(f'returning existing client {client_id} from cache')
            return client
        client = super().__new__(cls)
        cls._loaded[client_id] = client
        client._init_from_file(client_id, cls._db_file)
        return client

    def _init_from_file(self, client_id, file):
        print(f'reading client {client_id} data from file, db, etc.')
        name = ...
        email = ...
        self.name = name
        self.email = email
        self.id = client_id


x = Client(0)
y = Client(0)
z = Client(1)
print(f"x is y: {x is y}")
print(f"x is z: {x is z}")


class A:
    def __new__(cls, *args, **kwargs):
        print("new", cls, args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print("init", self, args, kwargs)

    def message(self):
        print("Ciao sono stata creata...")


uno = A()


class UppercaseTuple(tuple):
    def __new__(cls, iterable):
        upper_iterable = (s.upper() for s in iterable)
        return super().__new__(cls, upper_iterable)


class Animal:
    def __new__(cls, legs):
        if legs == 2:
            return Biped()
        else:
            return Quadruped()


class Biped:
    def __init__(self):
        print("Initializing 2-legged animal")


class Quadruped:
    def __init__(self):
        print("Initializing 4-legged animal")


anim1 = Animal(legs=4)
anim1 = Animal(legs=2)
