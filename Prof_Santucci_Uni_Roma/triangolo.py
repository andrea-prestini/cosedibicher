a = input("intero positivo lato a: ")
b = input("intero positivo lato b: ")
c = input("intero positivo lato c: ")

dati_corretti = a.isdecimal() and b.isdecimal() and c.isdecimal()

if not dati_corretti:
    print("i dati inseriti contengono un errore!")
    print(a, b, c)
else:
    a = int(a)
    b = int(b)
    c = int(c)
    
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print("Equilatero")
        elif a == b or a == c or b == c:
            print("Isoscele")
        else:
            print("Scaleno")
    else:
        print("i tre interi non corrispondono ad un triangolo valido")
        
            
