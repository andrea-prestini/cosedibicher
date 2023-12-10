from mailbox import NotEmptyError


class Guitar:
    '''classe chitarra generale'''

    def __init__(self):
        self.n_string = 6
        self.msg()

    def msg(self):
        '''messaggio creazione chitarra'''
        print(f'hai creato una classe {self.__class__.__name__}')

    @staticmethod
    def play():
        ''' suono della chiatarra'''
        print("pam pam pam")


class ElectricGuitar(Guitar):
    ''' classe child chitarra elettrica'''

    def __init__(self):
        super().__init__()
        self.n_string = 8
        self.colore = "rosso scuro"
        self.__cost = 50
    
    def costo(self, pz):
        return self.__cost * pz


uno = Guitar()
due = ElectricGuitar()
print("chitarra con corde", uno.n_string)
print("chitarra elettrica con corde", due.n_string)
print("la chitarra elettica è di colore", due.colore)
print("-" * 40)
print("la chitarra mi costa", due.costo(10))
