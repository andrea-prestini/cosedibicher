import time


cifre = [4, 3, 1, 2, 8, 5, 9]

for i in cifre[1:]:
    j = cifre.index(i)
    while j > 0 and cifre[j-1] > cifre[j]:
        cifre[j], cifre[j-1] = cifre[j-1], cifre[j]
        j -= 1
        time.sleep(1)

print("abbiamo ordinato la lisa... segue il risultato")
print(cifre)