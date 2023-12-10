"""°°°
## Virtual Enviroment
°°°"""
# |%%--%%| <W03DQu3QaL|VSfaCnjYvv>



# |%%--%%| <VSfaCnjYvv|P5231gK2aB>



# |%%--%%| <P5231gK2aB|UQ08JA3H1V>
"""°°°
# installare Anaconda
- conda env list  per visualizzare elenco enviroment presenti sulla macchina
- conda create --name Corso python=2.7
- source activate Corso / source deactivate (dall'ìnterno dell'enviroment)
    conda prevede conda activate e source deactivate

°°°"""
# |%%--%%| <UQ08JA3H1V|rsRbSjUCYG>
"""°°°
Conda è un secondo repository rispetto a $\color{red}{pip}$ ergo alcuni pacchetti possono avere un ritardo oppure non essere presenti nel database. In questo caso, dopo aver attivato la $\color{green}{virtualenv~corretta}$ e poi usare **pip**.
°°°"""
# |%%--%%| <rsRbSjUCYG|lyleFCqJwP>
"""°°°
~~~
import  utility.contaparole as conta
import utility.calcolatrice as calcolatrice

...
~~~
Nella directory ci sarà un file **contaparole.py** e **calcolatrice.py**.
L'utilizzo di $\color{red}{as}$ risulta utile quando hanno lo stesso nome.

°°°"""
# |%%--%%| <lyleFCqJwP|2rQMLe6DqU>
"""°°°
# Package

°°°"""
# |%%--%%| <2rQMLe6DqU|iWVPimAzb1>
"""°°°
Se voglio avere una cartella in cui mettere tutte le mie utility basta che al suo interno aggiunga un file chiamato **\__init__.py** anche se vuoto; questo mi permette, come nell'esempio precedente dove ho una cartella utility che contiene i miei moduli, di richiamarli nella forma **utility.contaparole**.
°°°"""
# |%%--%%| <iWVPimAzb1|KrvUnJDru3>
"""°°°
Se non voglio rendere visibili tutti i sorgenti presenti nella cartella scriverò, nel file init che abbiamo visto prima la stringa (dunder all ...)

°°°"""
# |%%--%%| <KrvUnJDru3|PvazpCrOXJ>
"""°°°
**Solo** i sorgenti elencati potranno essere importati e visti!
°°°"""
# |%%--%%| <PvazpCrOXJ|hk2TgCNdE4>
"""°°°
~~~
__all__ = [calcolatrice,]
°°°"""
# |%%--%%| <hk2TgCNdE4|iEGZHAE9RB>
"""°°°
Quando $\color{red}{importiamo}$ un modulo python esegue tutto il codice contenuto; ergo se nel modulo sono presenti dei print vengono "eseguiti" nella fase di importazione!
°°°"""
# |%%--%%| <iEGZHAE9RB|CEl5VnQOij>
"""°°°
~~~ 
print("nome modulo: %s" %(__name__))
°°°"""
# |%%--%%| <CEl5VnQOij|aO1VpNLVsY>
"""°°°
~~~
if __name__ = "__main__":
    calcola()
°°°"""
# |%%--%%| <aO1VpNLVsY|MxLUnp3m6k>
"""°°°
Se lancio direttamente il modulo partirà automaticamente la calcolatrice, diversamente entrerò nel loop di scelta while!
°°°"""
# |%%--%%| <MxLUnp3m6k|QgksG0Tzx6>
"""°°°
~~~
def calcola():
    #chiedo il primo numero
    primo = int(input("immetti un numero: ")

    #chiedo il secondo numero
    secondo = int(input("immetti un altro numero: ")

    operazione == 0
    
    while(operazione == 0):
        operazione = input("che operazione desideri eseguire\n(1. somma...)

        if(operazione == 1):
            risultato = primo + secondo
        elif(operazione == 2):
            risultato = primo - secondo...
        else:
            operazione = 0
            #messaggio di errore
            print("\nSelezionare un'operazione valida\n")
    print("Il risultato è: %d" % (risultato))
°°°"""
# |%%--%%| <QgksG0Tzx6|yI2ShicFVd>



# |%%--%%| <yI2ShicFVd|GJr6zazyK0>
"""°°°
~~~
def conta():
    frase = input("inserire una frase: ")

    parole = frase.split(" ")
    conteggio = len(parole)

    print("nella frase %s ci sono %d parole." % (frase, conteggio))

    numero = 1

    for parola in parole:
        print("%d %s " % (numero, parola))
        numero += 1
°°°"""
# |%%--%%| <GJr6zazyK0|Na8VkZIAcY>

voti = {"luca": 7, "andrea": 9, "silvia": 7, "luigi": 5}
promossi = {chiave:valore for chiave,valore in voti.items() if valore >= 6}
print(promossi)

# |%%--%%| <Na8VkZIAcY|aKfPGh6oDN>

elenco = [7, 4, 12, 45, 55]
validi = [x for x in elenco if x > 30]
print(validi)

# |%%--%%| <aKfPGh6oDN|gFahGzL2Dz>

for numero, valore in enumerate(elenco, start=10):
    print(numero, valore)

# |%%--%%| <gFahGzL2Dz|oOJyeaWa34>

persone = ["mario", "andrea", "franco", "mario", "andrea", "andrea"]
casa = set(x for x in persone)


# |%%--%%| <oOJyeaWa34|XkoT04wR6T>

print(casa)

# |%%--%%| <XkoT04wR6T|JJtqf9NrF1>
"""°°°
## files
°°°"""
# |%%--%%| <JJtqf9NrF1|yVabgpKdOb>

%%writefile persone.txt
andrea
mario
anna
franco
mario
andrea
giovanni

# |%%--%%| <yVabgpKdOb|uqVO6jSe5F>

cat persone.txt

# |%%--%%| <uqVO6jSe5F|9lvNv2fRt4>

univoci = set()

with open("persone.txt") as file_testo:
    for numero_riga, riga in enumerate(file_testo, 1):
        if riga in univoci:
            print("trovato duplicato alla riga", numero_riga)
        else:
            univoci.add(riga.strip())

print([x for x in univoci])

# |%%--%%| <9lvNv2fRt4|ujzIMPysNR>
"""°°°
## Parametri opzionali e valori di default
Vanno messi $\color{red}{dopo}$ i parametri obbligatori
°°°"""
# |%%--%%| <ujzIMPysNR|wriDBCCte1>


def sommatoria(primo, secondo=0, terzo=0):
    return primo + secondo + terzo

# |%%--%%| <wriDBCCte1|OfkbIaYHYK>

print(sommatoria(3, terzo=5)) # salto il secondo parametro, devo dargli un default per evitare ERROR!

# |%%--%%| <OfkbIaYHYK|hwY4RlSvPx>

def sommatoriaINF(*values):
    somma = 0
    for n in values:
        somma += n
    return somma

# |%%--%%| <hwY4RlSvPx|IEDVnkcUw8>

print(sommatoriaINF(2,3,5,12))
print(sommatoriaINF(1,2))

# |%%--%%| <IEDVnkcUw8|ZaRPOsvIkD>

def sommatoria2(*values):
    return sum(values)

# |%%--%%| <ZaRPOsvIkD|Ku5mYOHs88>

print(sommatoria2(1, 3, 5, 7))

# |%%--%%| <Ku5mYOHs88|V5yLsYEbyO>

def popola(**valori): # asterisco singolo DEVE precedere asterisco DOPPIO
    for k, v in valori.items():
        print(k, "=", v)
    print(valori)


# |%%--%%| <V5yLsYEbyO|hVNyeC3eMs>

popola(primo=1, secondo=2, terzo=5)

# |%%--%%| <hVNyeC3eMs|B5T54isand>
"""°°°
# DECORATORI
Sono una stringa che modifica il comportamento di classi, metodi, etc.
°°°"""
# |%%--%%| <B5T54isand|WvZpnqVQA6>

def funzione(a,b):
    return a * b

# |%%--%%| <WvZpnqVQA6|yPjSrwMHQD>

# se metto le parentesi chiamo la funzione, diversamente la uso come OGGETTO!
pippo = funzione
pluto = funzione
print(pippo(3,5))

# |%%--%%| <yPjSrwMHQD|9eJp20u9Fe>
"""°°°
I decoratori usano un oggetto come parametro di un altro oggetto!
°°°"""
# |%%--%%| <9eJp20u9Fe|Jv3ZCckYJL>
"""°°°
## Esempio di $\color{green}{CALLBACK}$
°°°"""
# |%%--%%| <Jv3ZCckYJL|0DFLd3FdUt>

def chiamatore(a, b, operazione):
    return operazione(a, b)

def somma(a, b):
    return a + b

def moltiplicazione(a, b):
    return a * b



# |%%--%%| <0DFLd3FdUt|JGjDt0AmRs>

print(chiamatore(5, 3, somma))


# |%%--%%| <JGjDt0AmRs|3e5tgO7yl0>

def scrittore(function):
    print("prima")
    function()
    print("dopo")


def chiamata():
    print("durante")

# |%%--%%| <3e5tgO7yl0|bC1FwiafJA>

def scrittore(function):
    def function_wrapper():
        print("prima")
        function()
        print("dopo")
    return function_wrapper

@scrittore # prima esegue scrittore passandogli come parametro chiamata
def chiamata():
    print("durante")

# |%%--%%| <bC1FwiafJA|rLceGIGBZM>

chiamata()
