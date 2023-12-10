people = [
    {"name": "andrea", "cognome": "prestini"},
    {"name": "roberto", "cognome": "tanzini"},
    {"name": "giulia", "cognome": "tanzini"},
]


    
people.sort(key=lambda person: person["name"], reverse=True)
print(people)
