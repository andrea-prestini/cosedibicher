## Operatori aritmetici

x = 2
k = 4

x+k 
# Output: 6

x-k 
# Output: -2

x*k 
# Output: 8

x/k 
# Output: 0.5

x%k 
# Output: 2

k%x 
# Output: 0

x**k 
# Output: 16

x//k 
# Output: 0

k//x 
# Output: 2

-5.0//3 
# Output: -2.0



## Operatori di confronto

z = 5
y = 7
r = 5

r == z  
# Output: True

z == y  
# Output: False

r != z  
# Output: False

z != y  
# Output: True

r > z  
# Output: False

y > z  
# Output: True


r < z  
# Output: False

y < z  
# Output: False

r < y
# Output: True

r >= z 
# Output: True

y >= z 
# Output: True

r >= y 
# Output: False


r <= z 
# Output: True

y <= z 
# Output: False

r <= y 
# Output: True


## Operatori di assegnazione

g = 12
h = 16

f = g + 5
f 
# Output: (17)


f +=2
f
# Output: (19)

f -=9
f
# Output: 10

f *=2
f
# Output: 20


f /= 4
f
# Output: 5.0

f %= 2
f
# Output: 1

g**=2
g
# Output: 144

h//=5
h
# Output: 3


# Operatori Bitwise

a = 20  
# Output: 0001 0100

b = 5
# Output: 0000 0101

a & b 
# Output: 0000 0100 (4)

a | b
# Output: 0001 0101 (21)

a ^ b
# Output: 0001 0001 (17)

~a
# Output: -21

~b
# Output: -6

a << b
# Output: 0010 1000 0000 (640)


a >> b  
# Output: 0000 0000 (0)



## Operatori logici

m = True
n = False

m and n
# Output: False

m or n
# Output: True

not n
# Output: True

not m
# Output: False


## Operatori di affiliazione

c = 'pluto'

'l' in c
# Output: True

'a' in c
# Output: False

'f' not in c
# Output: True

't' not in c
# Output: False


## Operatori identità

r = z = 5
y = 7

r is z
# Output: True

r is y
# Output: False

id(r)

id(y)

id(z)

r is not z
# Output: False

r is not y
# Output: True




