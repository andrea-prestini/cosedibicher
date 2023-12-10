import time
import math

lista = [1, 2, 3, 4, 5]

risultato = list(map(lambda x: pow(x, 2), lista))

for val in risultato:
    print(f'''
valore lista: {math.sqrt(val)}
valore risultato: {val}''')
    time.sleep(2)

quadrati = list(map(lambda x: pow(x, 2), lista))
print(quadrati)
print(list(filter(lambda x: x > 15, quadrati)))