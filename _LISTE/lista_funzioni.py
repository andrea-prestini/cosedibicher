# elenco funzioni disponibili
def f_0(x):
    print("funzione 0", x)
def f_1(x):
    print("funzione 1", x)
def f_2(x):
    print("funzione 2", x)
def f_3(x):
    if x == "andrea":
        print("ciao amico mio...", x.capitalize())
    else:
        print("mi dispiace non ti conosco...", x.capitalize())
def f_4(x):
    print("funzione 4", x)

# lista delle funzioni
lista_funzioni = [f_0, f_1, f_2, f_3, f_4]

# elementi su cui applicare le funzioni
elementi = ["andrea", "mario", "simone"]

# applico funzione 0 -----------------------------------------------------
print("Applico funzione 0".upper())
for val in elementi:
    lista_funzioni[0](val)

# stampo cornice
print("-" * 100)

# applico funzione 1 -----------------------------------------------------
print("Applico funzione 1".upper())
for val in elementi:
    lista_funzioni[1](val)

# stampo cornice
print("-" * 100)

# applico funzione 3 -----------------------------------------------------
print("Applico funzione 3".upper())
for val in elementi:
    lista_funzioni[3](val)
     


