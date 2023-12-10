import time

lista = [1, 2, 3, 4, 5]

nome = input("come ti chiami?\n")
time.sleep(2)
paese = input("dove abiti?\n")
time.sleep(3)

print("ciao amico %s sono felice che tu sia a %s".format(nome, paese))

for val in lista:
    print("nel tuo cassetto ci sono %s".format(val))
    time.sleep(1)
