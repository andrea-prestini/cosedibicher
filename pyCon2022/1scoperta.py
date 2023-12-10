class Train:
    """
    Definiamo una classe formato f string da utilizzare nel nostro
    codice. La sintassi seguirà le regole standard di uso nelle stringhe
    f-string.

    """

    def __format__(self, spec: str) -> str:
        n = int(spec)
        return f"|{'=' * n}|>>"


t = Train()
print(f"{t:5} andrea")

numbers = list(range(5))
# non crea copia ed è efficiente come un generatore pur non essendolo
for n in reversed(numbers):
    print(n)
print("-" * 30)
