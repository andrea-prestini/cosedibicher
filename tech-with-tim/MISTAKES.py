"""
1- Non usare nomi parametri uguali a funzioni build IN
2- NON usare oggetti mutable come parametri
3- Modificare un oggetto mentre lo si itera
4- Name Clashing nome nostro modulo uguale ad uno presente in libreria: es. pygame.py
è già un modulo python
5- Naked Except 
6- Wrong Data Structure
7- Global Variables
"""


# 2 Mutable object as parameter
def mutable_parameter(lst=[]):
    lst.append(1)
    lst.append(2)
    return lst


print(mutable_parameter())
print(mutable_parameter())


def mutable_parameter1(lst=None):
    if lst == None:
        lst = []
    lst.append(1)
    lst.append(2)
    return lst


print(mutable_parameter1())
print(mutable_parameter1())

print("-" * 50)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i, val in enumerate(lista):
    if i % 2 == 0:
        lista.pop(i)

print(lista)
print("-" * 50)

# 5 non sappiamo quale errore abbia generato la exception!
try:
    x = 1 / 0
except:
    print("I crashed!")


try:
    x = 1 / 0
except ZeroDivisionError as e:
    print("I crashed!", e)

try:
    f = open("miofile", "r")
except FileNotFoundError as e:
    print(e)
print("-" * 50)

# 6 Wrong Data Structure
'''
list -> []
set -> set()
dict -> {}

list quando conta frequenza e ordine degli elementi
set se un elemento è presente o meno in un elenco (molto più veloce)
dict chiavi e valori
---> from collections import deque

'''

# 7 Global Variables
global_var = 10


def bar(x):
    global global_var
    print(global_var)
    global_var = x
    print(global_var)


bar(100)
print("la variabile originale è stata cambiata:", global_var)


def foo(x):
    print(global_var)
    global_var = x
    print(global_var)


def foo1(x):
    global_var = x
    print(global_var)
