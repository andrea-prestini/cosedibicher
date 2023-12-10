from typing import overload, Union, NewType, TypeVar, Callable, Any, Dict, Pattern, Tuple, List, Generator, Iterator, ClassVar, Optional, Sequence, reveal_type
import re


def f(point: Tuple[int, int]):
    return point


risultato = f((100, 1000))
print(risultato)
print(type(risultato))


def fib(n: int) -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    while n > 0:
        yield a
        b, a = a + b, b
        n -= 1


g: Generator = fib(10)
i: Iterator[int] = (x for x in range(3))

stringa: Pattern = re.compile("(https?)://www.python.org/")
print(g)
print(i)


class Foo:
    x: int = 1
    y: ClassVar[str] = "class var"

    def __init__(self) -> None:
        self.i: List[int] = [0]

    def foo(self, a: int, b: str) -> Dict[int, str]:
        return {a: b}


foo = Foo()
foo.x = 123

print(foo.x)
print(foo.i)
print(Foo.y)
print(foo.foo(1, "abc"))


def param_opzionale(output: Optional[bool] = False):
    return output


param_opzionale()


def out_sequence(seq: Sequence[int]):
    # for list, tuple, string...
    return seq


print(out_sequence([1, 2]))

x: Tuple[int, int, int] = (1, 2, 3)
print(x)
print()

# Callable per paramentro una funzione con suoi parametri e return

print("Callable per funzioni come paramentro")


def add(x: int, y: int) -> int:
    return x + y


def calcolatore(func: Callable[[int, int], int]) -> str:
    return f"risultato {func(10, 2)}"


def calcolatore1() -> Callable[[int, int], int]:
    def add(x: int, y: int) -> int:
        return x + y
    return add


# Classe generica TypeVar
T = TypeVar("T")
R = TypeVar("R")


def get_one(x: List[T]) -> T:
    pass


def swap(x: T, y: R) -> Tuple[R, T]:
    return y, x


AnyStr = TypeVar("AnyStr", str, bytes)
# versione più particolare di typevar, abbiamo definito
# la classe string o bytes
# diverso da any che prenderebbe qualsiasi cosa!


def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b


concat("uno", b"due")  # check errore devono essere entrambi str o bytes
concat("uno", "due")  # corretto sono entrambe stringa

# Classe NewType
# A NewType is for when you want to declare a
# distinct type without actually doing the work of creating a new
# type or worry about the overhead of creating new class instances.


UserId = NewType("UserId", int)


def get_user(x: UserId):
    return UserId


# Questo funziona...
"get_user(UserId(12345))"

# Questo NON funziona...manca UserId

"get_user(12345)"


# UNION per un tipo o l'altro

def get_foo_or_bar(id: Foo) -> Union[Foo, None]:
    return id


def get_foo_or_none(id: Foo) -> Optional[Foo]:
    # like previuous: Foo or None
    return id


def get_foo(foo_id: Optional[int]) -> Optional[Any]:
    if foo_id == 10:
        return "Ciao"
    return 'wrong id'


print(get_foo(11))

# decoratore overload


@overload
def get_something(foo_id: None) -> None:
    pass


@overload
def get_something(foo_id: int) -> Foo:
    pass


def get_something(foo_id: Optional[int]) -> Optional[Foo]:
    if foo_id is None:
        return None
