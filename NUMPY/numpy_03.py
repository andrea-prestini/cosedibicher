import time
import numpy as np


valori = np.array([[10, 20, 30], [40, 50, 60]])
print(valori)
print("Divisione per 10 degli elementi array...")
print(valori / 10)

print()
# Alcuni tipi di matrici

print("matrice di 1")
print(np.ones((3, 3)))
print()
print("matrice di 0")
print(np.zeros((3, 3)))
print()
time.sleep(5)

print("Inizializzare una matrice...")
print(np.full((2, 3), 12))
print()
print("Le matrici di identità")
print(np.eye(5))
print()
print(np.diag([11, 12, 13, 14]))
print("-" * 60)
time.sleep(5)

# Arange e np.linspace
print(np.arange(4), "Arange")
print(np.linspace(0, 5, 10), "Linspace")

print("-" * 60)
time.sleep(5)

# Metodi random

print("Random numeri float64")
print(np.random.random((3, 3)))
print()
print("Random numeri interi")
print(np.random.randint(5, 18, (4, 3)))

print("-" * 60)
time.sleep(5)
# Distribuzione Gaussiana

print("Media 0 e deviazione standard 1, 3x3")
print(np.random.normal(0, 1, size=(3, 3)))
