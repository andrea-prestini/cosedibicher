## if - else statement
numero = 5

if numero > 0:
    print ("il numero positivo è pari a: " + str(numero))
# Output:
# il numero positivo è pari a: 5    

numero1 = -4

if numero1 > 0:
    print ("il numero positivo è pari a: " + str(numero1))


## utilizzo dell'else
numero1 = -4

if numero1 > 0:
    print ("il numero positivo è pari a: " + str(numero1))
else:
    print ("il numero negativo è pari a: " + str(numero1))
# Output: 
# il numero negativo è pari a: -4
    
    
## elif statement
numero1 = 0

if numero1 > 0:
    print ("il numero positivo è pari a: " + str(numero1))
elif numero1 == 0:
    print ("il numero è pari a: " + str(numero1))
else:
    print ("il numero negativo è pari a: " + str(numero1))
# Output:
# Il numero è pari a: 0

# if-else annidati
numero1 = 4

if type(numero1) == int:
    if numero1 > 0:
        print ("il numero è un intero positivo, pari a: " + str(numero1))
    elif numero1 < 0:
      print ("il numero relativo è pari a: " + str(numero1)) 
    else:
      print ("il numero è pari a: " + str(numero1))  
else:
    if type(numero1) == float:
        print ("il numero è reale e pari a: " + str(numero1)) 
# Output:
# il numero è un intero positivo, pari a: 4        


numero1 = -2

if type(numero1) == int:
    if numero1 > 0:
        print ("il numero è un intero positivo, pari a: " + str(numero1))
    elif numero1 < 0:
      print ("il numero relativo è pari a: " + str(numero1)) 
    else:
      print ("il numero è pari a: " + str(numero1))  
else:
    if type(numero1) == float:
        print ("il numero è reale e pari a: " + str(numero1)) 
# Output:
# il numero relativo è pari a: -2        
    
    
numero1 = 5.3

if type(numero1) == int:
    if numero1 > 0:
        print ("il numero è un intero positivo, pari a: " + str(numero1))
    elif numero1 < 0:
      print ("il numero relativo è pari a: " + str(numero1)) 
    else:
      print ("il numero è pari a: " + str(numero1))  
else:
    if type(numero1) == float:
        print ("il numero è reale e pari a: " + str(numero1)) 
# Output:
# il numero è reale e pari a: 5.3        

 
numero1 = -4/13

if type(numero1) == int:
    if numero1 > 0:
        print ("il numero è un intero positivo, pari a: " + str(numero1))
    elif numero1 < 0:
      print ("il numero relativo è pari a: " + str(numero1)) 
    else:
      print ("il numero è pari a: " + str(numero1))  
else:
    if type(numero1) == float:
        print ("il numero è reale e pari a: " + str(numero1)) 
# Output:
# il numero è reale e pari a: -0.3076923076923077        
    
    
    
numero1 = 0

if type(numero1) == int:
    if numero1 > 0:
        print ("il numero è un intero positivo, pari a: " + str(numero1))
    elif numero1 < 0:
      print ("il numero relativo è pari a: " + str(numero1)) 
    else:
      print ("il numero è pari a: " + str(numero1))  
else:
    if type(numero1) == float:
        print ("il numero è reale e pari a: " + str(numero1)) 
# Output:
# Il numero è pari a: 0        
      
       
    
    
    
    
    
    
    
    
    
    
    
    