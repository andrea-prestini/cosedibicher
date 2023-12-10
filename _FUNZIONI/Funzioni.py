# Esempio funzione

def saluta(nome):
    """ Questa funzione saluta la persona che viene
    passata come parametro     """
    print("Ciao, " + nome + ". Buongiorno!")


saluta('Giampiero')
# Output:
# Ciao, Giampiero. Buongiorno!

# Visualizziamo solo il docstring
print(saluta.__doc__)
# Questa funzione saluta la persona che viene
#    passata come parametro


# Visualizziamo l'oggetto restituito None
print(saluta("Giacomo"))


# Esempio Return Statement

def esponenziale(num, exp):
    """Questa funzione restituisce l’esponenziale
    del numero passato con la potenza definita
    dalla variabile exp"""
    return num**exp


# Restituisce la quarta potenza di 2
print(esponenziale(2, 4))
# Risultato: 16

# Restituisce la terza potenza di -5
print(esponenziale(-5, 3))
# Risultato: -125


# Funzioni lambda

def triplo(x): return x * 3


print(triplo(16))

# Risultato: 48


# Lambda con metodo filter

lista = [12, 75, 31, 24, 17, 8, 6, 93, 100]

lista_dispari = list(filter(lambda x: (x % 2 == 1), lista))

print(lista_dispari)

# Risultato:
# [75, 31, 17, 93]


# Lamda con metodo map

lista2 = [11, 4, 6, 17, 13, 22, 7]

lista_triplicata = list(map(lambda x: x * 3, lista2))

print(lista_triplicata)

# Risultato:
# [33, 12, 18, 51, 39, 66, 21]


# Moduli


a = Modulotest.prod(5, 24)
print(a)
# Output: ciao
# 120


# ricercare percorso

sys.path
sys.path.append("nomepercorsodaaggiungere")
sys.path.remove('nomepercorsodarimuovere')


# importare math


print("Il valore di e è pari a", m.e)

# Output:
# il valore di e è pari a 2.718281828459045


# importare moduli specifici


print(sqrt(4))
# Output:
# 2.0

print(floor(3.4))
# Output:
# 3


# Funzione Reload()


imp.reload(Modulotest)

# Output:
# Ciao
# <module 'Modulotest' from 'C:\\Users\\Lorenzo\\Desktop\\Python\\
#    File Python\\Modulotest.py'>
