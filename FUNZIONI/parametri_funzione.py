import time


def mia_funzione(*, a, b):
    print(f'{a=},{b=}')


print("prima funzione")

mia_funzione(a=1, b=2)

print("-" * 60)
time.sleep(2)


def mia_funzione1(a, b, /, *, uno=None, due=None):
    return f'''
            abbiamo:
                a: {a}
                b: {b}
                uno: {uno}
                due: {due}
            '''


print("seconda funzione parametri CORRETTI")

try:

    print(mia_funzione1(12, 23, uno=11, due=10))
except:
    print("ERRORE")

time.sleep(2)
print("-" * 60)

print("seconda funzione parametri NON corretti")

try:
    print(mia_funzione1(12, 23, 100, due=200))
except:
    print("ERRORE")


print("secondo elemento")

fruits = ['apple', 'banana', 'cherry']
