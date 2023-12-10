class DocMeta(type):
    def __init__(self, name, bases, attrs):
        for key, value in attrs.items():
            if key.startswith("__"):
                continue
            if not hasattr(value, "__call__"):
                continue
            if not getattr(value, "__doc__"):
                raise TypeError("%s must have a docstring" % key)
        type.__init__(self, name, bases, attrs)


class Door(metaclass=DocMeta):
    def __init__(self, number, status) -> None:
        self.number = number
        self.status = status

    def open(self):
        self.status = "open"

    def close(self):
        self.status = "closed"


D = Door(1, "open")
