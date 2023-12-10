from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier

# 0 femmina 1 maschio

giocatori = read_csv("./PitoneProgrammatore/giocatori.csv")

print(giocatori)

#colonne di INPUT X
X = giocatori.drop(columns=["videogame"])
y = giocatori["videogame"]

modello = DecisionTreeClassifier()
# il metodo fit addestra modello usando i dati input
modello.fit(X.values, y.values) 

print("-" * 30)
# previsione femmina anni 31
previsione = modello.predict([[0, 31]])
print("previsione: femmina, anni 31")
print(previsione)

print()
print("previsione: maschio, anni 16")
print(modello.predict([[1,16]]))