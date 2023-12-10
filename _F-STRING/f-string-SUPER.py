testo = "sarracino"
print(f'{testo:*^{len(testo)+4}}')
print(f'{testo:.<{len(testo)+4}}')

print()

print(f'Numero\t\tArea\t\tCubo')
for x in range(1, 4):
    print(f'{x:2d}\t\t{x*x:3d}\t\t{x*x*x:4d}')


print()
print(f'Numero\t\tArea\t\tCubo')
for x in range(1, 4):
    x = float(x)
    print(f'{x:5.2f}\t\t{x*x:6.2f}\t\t{x*x*x:8.2f}')

print()

APPLES = .50
BREAD = 1.50
CHEESE = 2.25

numApples = 3
numBread = 10
numCheese = 6

prcApples = numApples * APPLES
prcBread = numBread * BREAD
prcCheese = numCheese * CHEESE
total = prcBread + prcApples + prcCheese
strApples = "Apples"
strBread = "Red Bread"
strCheese = "Cheese"

print(f'{"My Grocery List":^30s}')
print(f'{"=" * 30}')
print(f'{strApples:10s}{numApples:10d}\t€ {prcApples:>5.2f}')
print(f'{strBread:10s}{numBread:10d}\t€ {prcBread:>5.2f}')
print(f'{strCheese:10s}{numCheese:10d}\t€ {prcCheese:>5.2f}')
print(f'{"Total:":>20s}\t€ {total:>5.2f}')
testo = "sarracino"
print(f'{testo:*^{len(testo)+4}}')
print(f'{testo:.<{len(testo)+4}}')

print()

print(f'Numero......Area......Cubo')
for x in range(1, 11):
    print(f'{x:2d}        {x*x:3d}        {x*x*x:4d}')
