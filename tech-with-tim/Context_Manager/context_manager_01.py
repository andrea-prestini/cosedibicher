# Open file by Context Manager
from contextlib import contextmanager


class File:
    def __init__(self, filename, method) -> None:
        self.filename = filename
        self.file = open(filename, method)

    def __enter__(self):
        print(f"Enter: opened file -> {self.filename}")
        return self.file

    def __exit__(self, type, value, traceback):
        print(f"{type}, {value}, {traceback}")
        print(f"Exit... closing file -> {self.filename}")
        self.file.close()
        if type == Exception:
            return True


with File("file.txt", "r") as f:
    print(f.read())


@contextmanager
def file(filename, method):
    file = open(filename, method)
    yield file
    file.close()


with file("./file.txt", "r") as f:
    print(f.read())
