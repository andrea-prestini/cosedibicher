l1 = [1, 2, [3, 4], (5, 6)]
l2 = list(l1) # shallow copy
l3 = l1[:] # shallow copy
l11 = [1, 2, [3, 4], (5, 6)]

print("confronto contenuto l2-l1:", l2 == l1)
print("confronto contenuto l3-l1:", l3 == l1)
print("confronto riferimento l2-l1:", l2 is l1)
print("confronto riferimento l3-l1:", l3 is l1)
print()
print("modifico la copia l2")
l2 = l1.copy()
print("ID l1 elemento lista", id(l1[1]))
print("ID l2 elemento lista", id(l2[1]))
l2[2].append("*")
print("l1 ->", l1)
print("l2 ->", l2)

print()
# per ovviare al problema ho bisogno di DEEP copy
import copy
print("Eseguo un DEEP copy lista 22 su lista 11")
l22 = copy.deepcopy(l11)
print("Modifico l22 con append...")
l22[2].append("*")
print("ID l11 elemento lista", id(l11[1]))
print("ID l22 elemento lista", id(l22[1]))
print("l11 ->", l11)
print("l22 ->", l22)
