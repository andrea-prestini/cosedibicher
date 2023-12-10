import numpy as np


matrix = np.array([[1, 2, 3], [4, 5, 6], [0, 0, 0]])

print(matrix)
print(type(matrix))
print(np.shape(matrix))
print(matrix.dtype)
print(f'dimensione matrice {matrix.ndim} - totale elementi {matrix.size}')
print("-" * 50)
super_matrice = (np.zeros((2, 4, 5)))
print(super_matrice)
print(np.shape(super_matrice))
print(
    f'dimensione matrice {super_matrice.ndim} - totale elementi {super_matrice.size}')
print("-" * 50)

# le view di array partono dalla base con cui condividono la memoria

base = np.array([1, 2, 3, 4, 5])
bicher = base.view()
copia = base.copy()

print("Stampo array base")
print(base)
print("Stampo array bicher")
print(bicher)
print("-" * 50)
print("la view posizione 0 ->", bicher[0])
print("la base posizione 0 ->", base[0])
print(f'Shared memroy: {np.shares_memory(base, bicher)}')
print("Modifico valori in base, cosa succede a view?")
base[0] = 1000
print(base, "base")
print(bicher, "view")
print()
print("Modifico valore in view, cosa succede a base?")
bicher[1] = 144
print(base, "base")
print(bicher, "view")
print("verifichiamo l'origine delle nostre array...")
print(base.base, "<- base")
print(bicher.base, "<- view")
print(copia.base, "<- copia")
