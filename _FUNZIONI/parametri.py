def spaghetti(one, two, *other):
    print(one)
    print(two)
    print(other)


spaghetti(1, 2, "uno", "due")


def spaghetti1(one, two, **other):
    print(one)
    print(two)
    print(other)


spaghetti1(1, 2, nome="andrea", cognome="prestini")


def spaghetti3(one, two, **other):
    print(one)
    print(two)
    print(other.get("nome"))


spaghetti3(1, 2, nome="andrea", cognome="prestini")


def generator():
    for x in range(1, 70):
            yield x
        

print("-" * 50)
for value in generator():
    if value < 35:
        print(value)
    else:
        StopIteration()
