class SuperClass:

    def __init_subclass__(cls, **kwargs):
        cls.default_name = "Inherited Class"


class SubClass(SuperClass):
    default_name = "SubClass"


class MyClass:
    default_name = "MyClass"


uno = SuperClass()
due = SubClass()
tre = MyClass()

print("default_name istanza SubClass")
print(due.default_name)
print("default_name istanza MyClass")
print(tre.default_name)
