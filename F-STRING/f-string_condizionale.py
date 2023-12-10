ppl = False
num = 3
string = f' I am {num:.2f}' if ppl else f'{num}'

print(string)

nome = "Andrea"
cognome = "Prestini"

print(f'''
    {nome=} 
    {cognome=}''')


prezzo = 10

print(f'''
     il prezzo nuovo è {prezzo * 10 =}''')


print(f'{nome!r}')