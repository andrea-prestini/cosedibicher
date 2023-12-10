lista1 = ["uno", "due", "tre"]
lista2 = ["uno", "due", "tre", "quattro", "cinque"]


a, b, c = lista1
print(f'''
        {a=}
        {b=}
        {c=}''')

a, b, *c = lista2
print(f'''
{a=}
{b=}
{c=}''')

*a, b = lista2
print(f'''
{a=}
{b=}''')

*a, b, c = lista2
print(f'''
{a=}
{b=}
{c=}''')

my_dict = {
    "nome": "andrea",
    "cognome": "prestini",
    "paese": "esine",
}


a = [*my_dict.values()]
b = [*my_dict.keys()]
print(a)
print(b)