# n = int(input("Quanto grandi i disegni?\n"))
n = 8

# quadrato di asterischi
for i in range(n):
    for k in range(n):
        print("* ", end="")
    print("")

print("_" * 30)

# diagonale principale
for i in range(n):
    for j in range(n):
        if i == j:
            print("* ", end="")
        else:
            print(". ", end="")
    print("")
    
print("_" * 30)

# diagonale principale e diagonale secondaria
for i in range(n):
    for j in range(n):
        if i == j or j == (n -1 -i):
            print("* ", end="")
        else:
            print(". ", end="")
    print("")
    
print("_" * 30)

# Triangolo sinistro
for i in range(n):
    for j in range(n):
        if  i >= j:
            print("* ", end="")
        else:
            print(". ", end="")
    print("")
    
print("_" * 30)

# Cornice
for i in range(n):
    for j in range(n):
        if  (j == 0 or j == n-1) or (i == 0 or i == n-1):
            print("* ", end="")
        else:
            print(". ", end="")
    print("")
    
print("_" * 30)

# Croce centrale
for i in range(n):
    for j in range(n):
        if  n %2 != 0 and i == (n-1)/2 or j == (n-1)/2 or \
            n %2 == 0 and j == (n/2) or i == (n/2) or \
            i == (n/2)-1 or j == (n/2)-1:
            print("* ", end="")
        else:
            print(". ", end="")
    print("")
    
print("_" * 30)
