lst_mioElenco = ["andrea", "mario", "anna"]
lst_mioElenco1 = ["red", "blue", "green", "yellow"]



print("-" * 50)    
for x in reversed(lst_mioElenco):
    print(x)

print("-" * 50)    
for x in enumerate(lst_mioElenco):
    print(x)


print("-" * 50)    
for x, y in zip(lst_mioElenco1, lst_mioElenco):
    print(x,y)
    
print("-" * 50)    
print(sorted(lst_mioElenco))

print("-" * 50)    
print(sorted(lst_mioElenco1, key=len))

