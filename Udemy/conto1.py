class Conto:
   def __init__(self, nome, conto):
       self.nome = nome
       self.conto = conto


class ContoCorrente(Conto):
    def __init__(self, nome, conto, importo):
        super().__init__(nome, conto)
        self.__saldo = importo
        
    def preleva(self, prelievo):
        self.__saldo -= prelievo
    
    def deposita(self, versamento):
        self.__saldo += versamento
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.__saldo)
        self.deposita(importo)
        
        
    #def descrizione(self):
        #print(f"""
    #nome: {self.nome}
    #conto: {self.conto}
    #importo: {self.__saldo}""")

    
class GestoreContiCorrenti:
    @staticmethod
    def bonifico(sorgente, destinazione, importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)
    @staticmethod
    def descrizione(posizione):
        print(f"""
nome: {posizione.nome}
conto: {posizione.conto}
importo: {posizione.saldo}""")

        
    
               
        
c1 = ContoCorrente("Andrea", "10", 2000)
c2 = ContoCorrente("Susanna", "20", 5000)

GestoreContiCorrenti.bonifico(c2,c1,1000)

GestoreContiCorrenti.descrizione(c1)
GestoreContiCorrenti.descrizione(c2)