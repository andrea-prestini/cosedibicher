def print3volte():
    print("ciao amico mio...\n"*3)

print3volte()

def sommatrice(a,b):
    return("il risultato della somma è " + str(a+b))

print(sommatrice(1,5))
    
def sommatrice1(a,b):
    print("risultato è " + str(a+b))

sommatrice1(10,12)

def parametro_incidentale(a,b,c=0):
    return(a+b+c)

print("il parametro non assegnato " + str(parametro_incidentale(1,2)))
print("il paramentro assegnato " + str(parametro_incidentale(1,2,3)))