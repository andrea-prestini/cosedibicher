
class primaclasse:
    '''Ho creato la prima classe'''
    pass

# |%%--%%| <R8eb0CwLj8|ww4M4cJk6R>

class classe2:
	"Questa è la mia seconda classe"
	x = 24
	def fun(self):
		print('Prova')

# |%%--%%| <ww4M4cJk6R|0Ccu4yduf4>

 
print(classe2.x)
# Output:
# 24   

# |%%--%%| <0Ccu4yduf4|EDrSpNsKhp>

print(classe2.fun)
# Output:
# <function classe2.fun at 0x0000027A9456B4C8>    

# |%%--%%| <EDrSpNsKhp|piK31x3YBp>

print(classe2.__doc__)
# Output: 
#'Questa è la mia seconda classe'    

# |%%--%%| <piK31x3YBp|RW1qjaCz8T>
"""°°°
Creare un oggetto della classe2
°°°"""
# |%%--%%| <RW1qjaCz8T|m9pLBPXSTg>

obj = classe2()

# |%%--%%| <m9pLBPXSTg|POYabYnuLn>
"""°°°
Richiamare la funzione fun()
°°°"""
# |%%--%%| <POYabYnuLn|msbO61ZKg8>

obj.fun()

# |%%--%%| <msbO61ZKg8|tigUxGtWuk>
"""°°°
Output<br>
Prova
°°°"""
# |%%--%%| <tigUxGtWuk|WaV7UCSI5t>
"""°°°
classe3
°°°"""
# |%%--%%| <WaV7UCSI5t|5ortdTGsvL>

class cane:
    
    #attributo
    specie = 'mammifero' 
    def __init__(self, nome, età=0):
        self.nome = nome
        self.età = età
    def getData(self):
        print("{} ha {} anni ed è {}".format(self.nome,self.età, self.specie))
    

# |%%--%%| <5ortdTGsvL|VKafmRqtj8>

Pluto = cane('Pluto',8)
Pluto.getData()
# Output:
# Pluto ha 8 anni ed è mammifero

# |%%--%%| <VKafmRqtj8|Yu9QtvAym5>

Pippo = cane('Pippo')
Pippo.attr = '5 mesi'

# |%%--%%| <Yu9QtvAym5|wJl33IoPUu>

print((Pippo.nome, Pippo.età, Pippo.attr))
# Output
# ('Pippo', 0, '5 mesi')

# |%%--%%| <wJl33IoPUu|J6FhIxmaWo>

print(Pluto.attr)
# Output
# 'cane' object has no attribute 'attr'

# |%%--%%| <J6FhIxmaWo|6rQQc2d3yp>
"""°°°
definire nuovi metodi istanza
°°°"""
# |%%--%%| <6rQQc2d3yp|fcu4Ul2TwS>

 
class cane:
    
    #attributo
    specie = 'mammifero' 
    def __init__(self, nome, età=0):
        self.nome = nome
        self.età = età
    def getData(self):
        print("{} ha {} anni ed è {}".format(self.nome,self.età, self.specie))
        
    def speak(self, sound):
        return "{} fa {}".format(self.nome, sound)

# |%%--%%| <fcu4Ul2TwS|V0HiQEP9v8>

Pluto = cane('Pluto', 8)
print(Pluto.speak("Bau Bau"))

# |%%--%%| <V0HiQEP9v8|QWwUWLIgxy>
"""°°°
Risultato<br>
Pluto fa Bau Bau
°°°"""
# |%%--%%| <QWwUWLIgxy|ljerXbFnIf>
"""°°°
 Cancellare oggetti e attributi
°°°"""
# |%%--%%| <ljerXbFnIf|6wljfNA6nu>

del Pippo

# |%%--%%| <6wljfNA6nu|7aC61VY9uF>
"""°°°
Classe Figlia (eredita dalla classe Cane)
°°°"""
# |%%--%%| <7aC61VY9uF|zveWhdo3x7>

class Labrador(cane):
    def run(self, velocità):
        return "{} corre {}".format(self.nome, velocità)

# |%%--%%| <zveWhdo3x7|QPZ2rKQXVB>
"""°°°
Classe Figlia (eredita dalla classe cane)
°°°"""
# |%%--%%| <QPZ2rKQXVB|R0bjUFUatq>

class PastoreTedesco(cane):
    def run(self, velocità):
        return "{} corre {}".format(self.nome, velocità)

# |%%--%%| <R0bjUFUatq|mfYX9puWKn>
"""°°°
Le classi figlie ereditano attributi e <br>
comportamenti dalla classe genitore
°°°"""
# |%%--%%| <mfYX9puWKn|HchA9RrIO8>

Tom = PastoreTedesco("Tom", 4)
Tom.getData()
# Output:
# Tom ha 4 anni ed è mammifero

# |%%--%%| <HchA9RrIO8|j5VlyX47I9>
"""°°°
Le classi figlie hanno attributi <br>
e comportamenti specifici
°°°"""
# |%%--%%| <j5VlyX47I9|beOBtQHDmZ>

print(Tom.run("velocemente"))
# Output:
# Tom corre velocemente

# |%%--%%| <beOBtQHDmZ|XUVgGnvusQ>
"""°°°
 funzione isinstance()
°°°"""
# |%%--%%| <XUVgGnvusQ|4vej7r3EnC>
"""°°°
E' Tom un'istanza di cane()?
°°°"""
# |%%--%%| <4vej7r3EnC|68mwVFjHTr>

print(isinstance(Tom, cane))
# Output:
# True

# |%%--%%| <68mwVFjHTr|gwx3IKMLKr>
"""°°°
E' Jamie un'instanza di cane()?
°°°"""
# |%%--%%| <gwx3IKMLKr|zYQboY39Qo>

Jamie = cane("Jamie", 100)
print(isinstance(Jamie, cane))
# Output:
# True

# |%%--%%| <zYQboY39Qo|yOIVCxLrow>
"""°°°
E' Jonny un'istanza di PastoreTedesco()?
°°°"""
# |%%--%%| <yOIVCxLrow|UtBlXrHRNG>

Jonny = Labrador("Jonny", 6)
print(isinstance(Jonny, PastoreTedesco))
# Output:
# False    

# |%%--%%| <UtBlXrHRNG|NTVhZyLlk1>
"""°°°
E' Jamie un'istanza di Tom?
°°°"""
# |%%--%%| <NTVhZyLlk1|tRMRfDkCZm>

print(isinstance(Jamie, Tom))
# Output:
# isinstance() arg 2 must be a type or tuple of types    

# |%%--%%| <tRMRfDkCZm|SkqBd0c1Qi>
"""°°°
 funzione issubclass()
°°°"""
# |%%--%%| <SkqBd0c1Qi|xHuJSKVmRD>

issubclass(cane,Labrador)
# Output:
# False

# |%%--%%| <xHuJSKVmRD|mbhJBCqmId>

issubclass(Labrador,cane)
# Output:
# True

# |%%--%%| <mbhJBCqmId|9u6KwlVDl6>
"""°°°
 Esempio Override<br>
classe cane genitore
°°°"""
# |%%--%%| <9u6KwlVDl6|OEiQka4cIe>

class cane:
    
    #attributo
    specie = 'mammifero' 
    def __init__(self, nome, età=0):
        self.nome = nome
        self.età = età
    def getData(self):
        print("{} ha {} anni ed è {}".format(self.nome,self.età, self.specie))
        
    def speak(self, sound):
        return "{} fa {}".format(self.nome, sound)

# |%%--%%| <OEiQka4cIe|ssyeANBde1>
"""°°°
classe SiberianHusky figlia
°°°"""
# |%%--%%| <ssyeANBde1|WUvQVFsuDz>

class SiberianHusky(cane):
    def getdata(self):
        return "Mi chiamo {}".format(self.nome)

# |%%--%%| <WUvQVFsuDz|VLmNFdHlu4>

c = SiberianHusky('Rex')
print(c.getdata())

# |%%--%%| <VLmNFdHlu4|LaCwV0oFLV>
"""°°°
Output:<br>
Mi chiamo Rex
°°°"""