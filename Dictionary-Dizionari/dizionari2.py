d = {'andrea': 'capo', 'mario': 'CEO', 'anna': 'finanza', 'paolo': 'informatica'}
n = ['pietro', 'franco', 'maria', 'alberto', 'giorgio']
c = ['red', 'green', 'blue', 'yellow']
print(d.keys())
for k in d:
    print(k)

print("-" * 50)    
for k in d.keys():
    if k.startswith('a'):
        print(k)


print("-" * 50)    
for k in list(d.keys()):# d.keys è una tupla e dà errore, devo trasformarlo in lista
    if k.startswith("a"):
        del d[k]
        print(d)
    

print("-" * 50)    
d = {'andrea': 'capo', 'mario': 'CEO', 'anna': 'finanza', 'paolo': 'informatica'}
print("-" * 50)    
for k, v in d.items():
    print(k, v)

print("-" * 50)    
scatola = dict(zip(n,c)) #con 2 liste e zip costruisco un dizionario!
print(scatola)# attenzione giorgio non è stato inserito usa min(n) degli elementi delle liste


print("-" * 50)    
names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']
d_dict = {}
for name in names:
    key = len(name)
    d_dict.setdefault(key, []).append(name)
print(d_dict)


print({k for k in d if k.startswith("a")})# dict comprehention
print({k for k in d.keys() if k.startswith("a")})# dict comprehention
