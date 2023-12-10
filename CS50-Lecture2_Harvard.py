# corso Harvard generico sul linguaggio python

squadra = {
    "operatore1": {"nome": "andrea", "cognome": "prestini"},
    "operatore2": {"nome": "eleonora", "cognome": "favagrossa"},
    "operatore3": {"nome": "roberto", "cognome": "tanzini"},
}


print(squadra.get("operatore9", "chiave non presente!"))
print(squadra.setdefault("operatore5", {"nome": "pietro", "cognome": "rossi"}))
