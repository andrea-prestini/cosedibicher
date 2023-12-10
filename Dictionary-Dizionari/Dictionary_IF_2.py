nomi = ["andrea", "eleonora", "roberto", "simone"]
paesi = ["Esine", "Breno", "Gambara"]


scatola = {
nomi[i] : 
    (paesi[0] if nomi[i] == "andrea" else 
     paesi[1] if nomi[i] == "eleonora"  else 
     paesi[1] if nomi[i] == "roberto" else 
     paesi[2] if nomi[i] == "simone" else _)
    for i in range(3)
}

print(scatola)