'''
marco = Person()
marco.age = 19
marco.name = "Marco"
marco.money = 50

giulia = Person()
giulia.age = 18
giulia.name = "Giulia"
giulia.money = 200
# sconsigliato ma permesso da python
# giulia.capelli = "rossi"
marco.hello()
giulia.hello()

Se modifichiamo il modulo init della classe dovremo necessariamente creare
istanze che passino direttamente gli argomenti richiesti,
name, age, money altrimenti
il codice andrà in ERRORE! La sintassi corretta,
in questo caso, per istanziare la
classe Person sarà quella di franco:
'''


class Person:
    age = 0
    name = ""
    money = 100
    paese = "Esine"

    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

    def hello(self):
        print("Ciao sono:", self.name)

    def change_money(self, qty):
        self.money = self.money + qty

    def __str__(self):
        return (
            f'''
    Ciao sono {self.name}
    ho {self.age} anni
    nel borsellino ho {self.money} soldini
    ''')


# funzione FUORI dalla classe che usa un metodo di classe.
# p1 e p2 devono essere istanze classe Person (naturalmente)
def give_money(p1, p2, qty):
    p1.change_money(qty)
    p2.change_money(-qty)


franco = Person("Franco", 42, 2000)
giovanni = Person("Giovanni", 30, 1000)
silvia = Person("Silvia", 22, 200)
eleonora = Person("Eleonora", 38, 300)
eleonora.paese = "Breno"

franco.hello()
franco.change_money(5)
franco.change_money(-25)
print(f'{franco.name} ha {franco.money} soldini')

print("=" * 40)

give_money(franco, giovanni, 100)
print("i soldini di Franco sono:", franco.money)
print("i soldini di Giovanni sono:", giovanni.money)

print(franco)
print("-" * 40)
print(silvia)
print(f'Il paese di {silvia.name} è {silvia.paese}')
print(f'Il paese di {eleonora.name} è {eleonora.paese}')
