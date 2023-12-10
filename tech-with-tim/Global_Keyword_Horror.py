x = 0


def foo():
    x = 2

    def bar():
        x = 7
        print("Local bar", x)
    bar()
    print("Local foo", x)


foo()
print("Global scope", x)

print("-" * 50)


def foo1():
    x = 2

    def bar1():
        print("Local bar", x)
    bar1()
    print("Local foo1", x)


foo1()

print("-" * 50)


def foo2():
    global x
    x = 2

    def bar2():
        global x
        x = 7
        print("Bar", x)
    bar2()
    print("Foo", x)


foo2()
print("Global", x)

print("-" * 50)


def foo3():
    global p
    x = 1000
    lista = [2, 3, 4, 5]
    p = [x * val for val in lista]
    print(f"Global only inside funciton {p}")


foo3()
print(f"Global from inside funciton {p}")
