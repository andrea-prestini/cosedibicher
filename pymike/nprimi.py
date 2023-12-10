def is_prime(numero):
    for element in range(2, numero):
        if numero % element == 0:
            return False
    return True

def print_next_prime(numero):
    index = numero
    ciclo = 0
    while  ciclo < 5:
        index += 1
        if is_prime(index):
            print("trovato", index)
            ciclo += 1



numero = 10
print(is_prime(numero))
print_next_prime(numero)

print("questo programmino funziona  casa")
print("vediamo cosa possimo fare per il battery drain")