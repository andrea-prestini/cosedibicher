import math


class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius

    def get_radius(self):
        print("ecco il raggio del cerchio")
        return self._radius

    def set_radius(self, val):
        if val < 0:
            raise ValueError("il raggio deve essere positivo...")
        self._radius = val

    radius = property(
        fget=get_radius,
        fset=set_radius,
        fdel=None,
        doc="Il raggio del cerchio")


c = Circle(10)
print(c.radius)
print("-" * 50)


class Circle1:
    def __init__(self, radius) -> None:
        self._radius = radius

    @property
    def radius(self):
        print("Il raggio del tuo cerchio è")
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def area(self):
        calcolo_area = math.pi * self.radius ** 2
        return f"L'area del cerchio con raggio {self.radius} è {calcolo_area}"


c1 = Circle1(100)
print(c1.radius)
c1.radius = 120
print(c1.radius)
print(c1.area)
