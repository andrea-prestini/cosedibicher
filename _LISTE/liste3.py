spam = "la pratica"
eggs = "rende perfetti!"

print(spam + eggs)
print(spam * 3)

a = [1, 2, "tre", 4, 5, 6, "ultimo"]
b = [4, 5, "sei", "sette"]
c = ["primo", "nome", "paese", "alimento"]
print(a + b)
print(len(a))#lunghezza della lista
print(len(spam))#lunghezza della stringa compresi spazi
print("a" in spam) # verificho che ci sia la lettera a nella stringa
print("z" in spam)#stessa cosa per le liste!
print("z" not in spam)#stessa cosa per le liste!
a.append("andrea")
print(a)
a.remove("andrea")
print(a) #le stringhe non hanno append e remove
#convertiamo una stringa in lista:
nuova = list(spam)
print(nuova)
print(a[-1])
print(a[0:2])
print(a[0:3:1])
print(a[-1:-3:-1])
print(a[::-1])# inverte la lista, da ultimo a primo elemento!
print(sorted(c))# solo per liste con stringhe, non modifica originale!
c.sort()
print(c)# in questo caso la lista c è stata modificata, utilizzando sort()

c.sort(key=lambda name: name[-1])
print(c)

print(list(filter(lambda name: name.startswith("p"), c)))
print(list(name.capitalize() for name in c if name.startswith("p")))
for i, name in enumerate(c):
    print("%d: %s" %(i, name))
