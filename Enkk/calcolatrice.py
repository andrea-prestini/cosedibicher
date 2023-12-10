print("="* 40)
print("Benvenuto nella calcolatrice morente di Enkk")
print("="* 40)

# loop richiesta dati...
continua = True
while continua:
    # richiesta dei dati
    x = input("primo numero: ")
    y = input("secondo numero: ")
    op = input("Che operazione vuoi [+, -]\n")
    
    # validazione dei dati
    if not(x.isdigit() and y.isdigit() and (op == "+" or op == "-")):
        print("Dati ERRATI!")
        continue
        
   # Cast
    x = int(x)
    y = int(y)
    risultato = 0
    if op == "+":
        risultato = x + y
    else:
        risultato = x - y
    
    print("il risultato è: ", risultato)
    print("-"*40)

    cont_risp = input("Vuoi continuare?(y=si)\n" )
    
    # Metodo efficiente che sostituisce IF
    continua = cont_risp == "y"
print("Esco dalla calcolatrice...") 
# continua = input("vuoi continuare? ") == "y"
# versione super contratta della variabile continua! ! !