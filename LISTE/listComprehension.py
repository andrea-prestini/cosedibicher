n_lst = [2,3,4,5,7]
numeri_lst = [12,33,44,55]

print("la lista è ", [x+5 for x in n_lst])
print("la lista filtrata è ",list(filter(lambda x: x > 3, n_lst)))
print("la lista filtrata è ", [x for x in n_lst if x > 3])
print([i ** 2 for i in range(1, 12)])
print([x for x in n_lst if x >= 4])

nomi_lst = ["andrea", "mario", "anna"]
print(['ciao ' + x  for x in nomi_lst])
print([x for x in nomi_lst if x.startwith("a")])

print([(x,y) for x in n_lst for y in numeri_lst])