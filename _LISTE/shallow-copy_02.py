import copy

numbers = [[1, 2], [3, 4, 5]]
new_numbers1 = copy.copy(numbers) # shallow copy
new_numbers2 = copy.deepcopy(numbers) # deep copy

new_numbers1[0][0] = 100

print("SHALLOW copy")
print("new_numbers1", new_numbers1)
print("numbers", numbers)
print()

print()
print("DEEP copy")
numbers = [[1, 2], [3, 4, 5]]
new_numbers2 = copy.deepcopy(numbers) # deep copy
new_numbers2[0][0] = 100

print("new_numbers2", new_numbers2)
print("numbers", numbers)

print("-" * 60)

# con le classi
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


p1 = Person("andrea", 52)
p2 = p1 # shallow copy
print("SHALLOW copy")
print("Change age p2 to 45...")
p2.age = 45
print("p1 age ->", p1.age)
print("p2 age ->", p2.age)


print("-" * 60)
p1 = Person("andrea", 52)
p2 = copy.deepcopy(p1) # DEEP copy
print("DEEP copy")
print("Change age p2 to 45...")
p2.age = 45
print("p1 age ->", p1.age)
print("p2 age ->", p2.age)

