'''
Interrogazione in diretta su Discort con Enkk
'''

with open("filetestuale.txt", "r") as f:
    for line in f:
        if line.strip().isdigit():
            print(line.strip())
            
print("=" * 30)

with open("filetestuale.txt", "r") as f:
    for line in f:
        if not line.strip().isdigit():
            print(line.strip())

s = 0
n = 0
with open("filetestuale.txt", "r") as f:
    for line in f:
        if line.strip().isdigit():
            n += 1
        else:
            s +=1

print("le stringhe sono:", s)
print("i numeri sono:", n)