
uno = input("Come ti chiami?\n")
if uno != "andrea":
    print("Allora non sei il mio amico...")
    
due = input("sei della valle camonica?\n")
if due != "si":
    print("sei della bassa...")
    
tre = input("Abiti ad Esine?\n")
if tre != "si":
    print("non abiti nel paese giusto")

if uno == "andrea" and due == "si" and tre == "si":
    print("Allora sei andrea")


print("fine procedura...")