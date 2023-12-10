"""°°°
# Gli oggetti in python
°°°"""
# |%%--%%| <RxNxXBFiJg|H1G0eYgmow>
"""°°°
Tutto è un oggetto in python. Questi oggetti hanno sempre 3 elementi:
* identità
* tipologia
* valore
°°°"""
# |%%--%%| <H1G0eYgmow|Ilj1nCuFTo>
"""°°°
## Identità
Informazione numerica di tipo immutabile, rimane fino alla morte dell'oggetto.
°°°"""
# |%%--%%| <Ilj1nCuFTo|TbdsDwU3SN>
"""°°°
## Tipologia
Categoria che determina la natura di un oggetto; quali valori possono essere assegnati ad un oggetto, altre caratteristiche dell'oggetto. Gli oggetti che fanno parte di un certo tipo si chiamano ISTANZE di quell'oggetto.
°°°"""
# |%%--%%| <TbdsDwU3SN|82U5DgluOw>
"""°°°
# Valore
Il valore è un dato o un insieme di dati mantenuto all'interno dell'oggetto, quando questi lo prevede. Un oggetto che può modificare il suo valore durante il suo ciclo di vita si dice Mutabile, diversamente si definisce Immutabile. Tale caratteristica è data dal $\color{green}{tipo}$ di oggetto.
°°°"""
# |%%--%%| <82U5DgluOw|L8Hwfv3vuI>
"""°°°
## Literal
Forma $\color{red}{letterale}$ di un oggetto: python possiede una serie di dati che sono predefiniti nel linguaggio e la cui definizione del valore dipende dal modo letterale con cui sono stati inseriti. Se scrivo 20 python lo interpreterà come un integer perchè questo è il modo letterale con cui lo abbiamo inserito; tra apici invece definiremo un oggetto stringa, senza bisogno di dichiararlo!
°°°"""
# |%%--%%| <L8Hwfv3vuI|AK0oQRjf9m>
"""°°°
# Variabili
Per riferirci agli oggetti non useremo mai la sua identità, ma lo assegneremo un $\color{red}{nome}$ ad un oggetto.
°°°"""
# |%%--%%| <AK0oQRjf9m|8I59qcVdzR>
"""°°°
~~~
a = 20
mia_lista = [1, 2, 3]
°°°"""
# |%%--%%| <8I59qcVdzR|V7tm5sZDgo>
"""°°°
Esistono delle regole per definire i nomi validi:
* lettere o numeri o caratteri Unicode o underscore
* NON può iniziare con un numero
* NON può essere una **parola riservata**
°°°"""
# |%%--%%| <V7tm5sZDgo|UIZKuaJMbZ>
"""°°°
I nomi associati agli oggetti vengono definiti *variabili*.
In python una variabile non è una variabile, ma un nome che punta ad una variabile. Non è fortemente tipizzata.
°°°"""
# |%%--%%| <UIZKuaJMbZ|cpgB2k8CS4>
"""°°°
~~~
a = 20
a = "andrea"
°°°"""
# |%%--%%| <cpgB2k8CS4|xGxmF8Lkeh>
"""°°°
Questa cosa implica la **condivisione** dell'ID.
°°°"""
# |%%--%%| <xGxmF8Lkeh|fWYw0WHCzP>
"""°°°
~~~
a = 20
b = a
~~~
In questo caso a e b puntano allo stesso oggetto, ma non sono lo stesso oggetto!
°°°"""
# |%%--%%| <fWYw0WHCzP|fmsBSQzCeA>
"""°°°
Molto importante è il concetto di $\color{red}{reference~count}$.
Tutti gli oggetti in python hanno un contatore di riferimenti: questo implica che l'oggetto venga distrutto SOLO quando il suo reference count è pari a 0. Il *Garbage Collector* ripulisce tutto e libera la memoria (tutto in runtime).
°°°"""
# |%%--%%| <fmsBSQzCeA|sDSflsmkHx>
"""°°°
 Il *Garbage Collector* ripulisce tutto e libera la memoria (tutto in runtime).
°°°"""
# |%%--%%| <sDSflsmkHx|vUhjuDJPE4>
"""°°°
# Callable Objects
Gli oggetti chiamabili sono quelli in cui usiamo argomenti all'interno delle parentesi tonde. Esempio le funzioni!
°°°"""
# |%%--%%| <vUhjuDJPE4|BX6DhqEkmn>
"""°°°
La funzione `print` ne è un esempio!
°°°"""
# |%%--%%| <BX6DhqEkmn|q7M9oweVqQ>
"""°°°
Altre funzioni utili sono `id(oggetto)` oppure `type(oggetto)`.
°°°"""
# |%%--%%| <q7M9oweVqQ|FEmYTRhfZl>
"""°°°
# Gli Attributi
Gli oggetti in python hanno un valore ed una identità; possono avere anche una serie di *attributi*.
°°°"""
# |%%--%%| <FEmYTRhfZl|kLTKQJzto9>
"""°°°
Gli attributi sono degli oggetti riferiti da un oggetto perchè ne specificano ulteriori caratteristiche (possono essere dati o funzioni). Nel caso in cui siano funzioni vengono chiamati metodi.
°°°"""
# |%%--%%| <kLTKQJzto9|cjf1Hxgy4S>
"""°°°
Per richiamarli si una il punto: nome oggetto.nome attributo!
°°°"""
# |%%--%%| <cjf1Hxgy4S|WbmxqYhTex>
"""°°°
Quando l'attributo è una funzione dobbiamo invocarlo essendo un oggetto Callable.
°°°"""
# |%%--%%| <WbmxqYhTex|UayvdYXfyf>

"python".upper()

# |%%--%%| <UayvdYXfyf|uW84WdSJtI>

x = "python"
x.upper()

# |%%--%%| <uW84WdSJtI|nsvnXHaXx0>
"""°°°
# BASIC data types
°°°"""
# |%%--%%| <nsvnXHaXx0|eYXoQRyClB>
"""°°°
* tipi numerici (anche boolean)
* stringhe
* operatori
*espressioni
°°°"""
# |%%--%%| <eYXoQRyClB|eeJHHaaLVw>
"""°°°
>> None è un basic data type che ha una sola istanza... None
°°°"""
# |%%--%%| <eeJHHaaLVw|EUy9CakW5V>
"""°°°
## tipi numerici
* integer
* floating poin
* boolean
Sono tutti Immutabili!
°°°"""
# |%%--%%| <EUy9CakW5V|znFfoUZQgT>
"""°°°
`a = 3` ed `a = 4`
°°°"""
# |%%--%%| <znFfoUZQgT|lSMEFh7Scr>
"""°°°
a non ha modificato l'oggetto, ma punta ad un oggetto diverso, prima il numero 3 e poi il numero 4!
°°°"""
# |%%--%%| <lSMEFh7Scr|rVj483QpDi>
"""°°°
Dalla versione 3.6 possiamo dividere le cifre di un numero attraverso l'underscore: 10_000_000.
°°°"""
# |%%--%%| <rVj483QpDi|Hm0nZDIHtN>
"""°°°
Possiamo usare 3 literal per esprimere un numero:
* Binario -- 0b10011001
* ottale 0o1635
* esadecimale 0x1F8A
°°°"""
# |%%--%%| <Hm0nZDIHtN|qbG62SubLm>
"""°°°
I boolean sono sottoinsiemi di interi che hanno solo 2 valori: True o False; True=1 e False=0.
°°°"""
# |%%--%%| <qbG62SubLm|YgJiB6uFF7>
"""°°°
I Floating point vengono introdotti con un punto decimale di separazione. 
°°°"""
# |%%--%%| <YgJiB6uFF7|dwWoShkYZK>
"""°°°
Possiamo usare anche l'annotazione esponenziale!
°°°"""
# |%%--%%| <dwWoShkYZK|QP24AIt6bF>

2e4

# |%%--%%| <QP24AIt6bF|z1MqBwqeQ1>

2e-4

# |%%--%%| <z1MqBwqeQ1|q4LOQsxgps>
"""°°°
Naturalmente python supporta anche i numeri **immaginari**.
°°°"""
# |%%--%%| <q4LOQsxgps|zg4IAmdJXp>
"""°°°
## Stringhe
°°°"""
# |%%--%%| <zg4IAmdJXp|dCweC8jwMr>
"""°°°
Le STRINGHE sono sequenze di elementi: una sequenza indica un insieme *ordinato* di elementi. Tale caratteristica ci permetterà di intervenire facilmente sugli elementi che compongono la stringa.
°°°"""
# |%%--%%| <dCweC8jwMr|C9NoPjG1IC>
"""°°°
Ogno elemento di una stringa deve appartenere al set UNICODE.
°°°"""
# |%%--%%| <C9NoPjG1IC|hmvisbzL7U>
"""°°°
Le stringhe in python sono oggetti immutabili, possiamo copiare parte di una stringa in un'altra stringa.
°°°"""
# |%%--%%| <hmvisbzL7U|uT2pkMyMPs>
"""°°°
Possiamo usare apici singoli o doppi, purchè siano simmetricamente definiti.
°°°"""
# |%%--%%| <uT2pkMyMPs|srIFrgmU2w>
"""°°°
Una stringa vuota non ha caratteri ma è comunque esistente come oggetto.
°°°"""
# |%%--%%| <srIFrgmU2w|YSYGi8sVaa>
"""°°°
Possiamo definire stringhe su multilinea usando 3 apici singoli o 3 apici doppi. 
°°°"""
# |%%--%%| <YSYGi8sVaa|vRXZUL4x9Z>
"""°°°
>
""" questa può essere una stringa su 
diverse linee"""

°°°"""
# |%%--%%| <vRXZUL4x9Z|Czze82V0nl>

#Abbiamo diverse tipologie di Escape (caratteri non stampabili):
#* \n andare a capo
#* \t tabulare
#* \\ inseriamo la backslash nella stringa
#* \' inseriamo l'apice nella stringa
#* \" inseriamo un doppio apice nella stringa

# |%%--%%| <Czze82V0nl|SDL0vZ4Z3v>
"""°°°
## caso particolare: le F strings
°°°"""
# |%%--%%| <SDL0vZ4Z3v|HlJd1JAGn3>
"""°°°
* modulo formatting (ormai deprecata)
* metodo format associato alle stringhe
* f-string introdotto da python 3
°°°"""
# |%%--%%| <HlJd1JAGn3|DH2YrOKi2S>

titolo = "Isola Misteriosa"
autore = "Giulio Verne"

# |%%--%%| <DH2YrOKi2S|aUsyzLSTo3>

print(f"Titolo: {titolo}, Autore: {autore}")


# |%%--%%| <aUsyzLSTo3|lSkwQRmOMF>
"""°°°
Questa operazione viene detta **String Interpolation**
°°°"""
# |%%--%%| <lSkwQRmOMF|AvYXmf6kcA>

print(f"Titolo: {titolo.upper()}, Autore: {autore}")

# |%%--%%| <AvYXmf6kcA|3Jx8Yhsckj>
"""°°°
PEP 498 -- Literal String Interpolation
°°°"""
# |%%--%%| <3Jx8Yhsckj|1zvE0D7vyF>
"""°°°
# Espressioni ed Operatori
°°°"""
# |%%--%%| <1zvE0D7vyF|IsvCB2887k>
"""°°°
Le operazioni eseguono operazioni su degli elementi; tali elementi possono essere di tipo diverso.
°°°"""
# |%%--%%| <IsvCB2887k|RDvSJilRZx>
"""°°°
I più comuni sono gli operatori aritmetici:
* addizione + 
* sottrazione -
* moltiplicazione \*
* divisione floating point /
* divisione intera // solo parte intera del risultato
* modulo % definisce il resto di una divisione
* esponenziale **
* meno unario -
°°°"""
# |%%--%%| <RDvSJilRZx|3EUGqSylam>
"""°°°
operatori di assegnamento:
* = assegnazione di variabile
* += scorciatoia per a += equivale ad a= a+b
* -=, *=, /=, //=, %=, **=

°°°"""
# |%%--%%| <3EUGqSylam|1BjjNALW6j>
"""°°°
operatori di confronto (ritornano sempre un valore Booleano):
* <
* \>
* ==
* !=
* <=
* \>=
°°°"""
# |%%--%%| <1BjjNALW6j|TAplUJrwvD>
"""°°°
Attenzione alla $\color{red}{precedenza}$: usiamo le parentesi per modificarne il comportamento.
°°°"""
# |%%--%%| <TAplUJrwvD|mnWjEwTD0v>
"""°°°
Operatori logici (restituisco valori Booleani):
* and
* or
* notm
°°°"""
# |%%--%%| <mnWjEwTD0v|8683uFYApV>
"""°°°
|  A    | B    | A AND B|
|:--------|:----:|-------:|
|True| True| True|
|False| False|False|
|True| False|False|
|False| False|False|
°°°"""
# |%%--%%| <8683uFYApV|48tVe28ePv>
"""°°°
|  A    | B    | A OR B|
|:--------|:----:|-------:|
|True| True| True|
|False| False|False|
|True| False|True|
|False| False|True|
°°°"""
# |%%--%%| <48tVe28ePv|ikyXn2E8XJ>
"""°°°
NOT è un operatore UNARIO: ritorna il contrario dell'espressione valutata.
°°°"""
# |%%--%%| <ikyXn2E8XJ|qV4i5xfHOc>
"""°°°
In python *tutti* gli oggetti hanno un valore di verità implicitamente assegnato:
sono tutti FALSE
* None
* False
* Zero
* una sequenza vuota
* un dizionario vuoto
in tutti gli altri casi il valore è TRUE...
°°°"""
# |%%--%%| <qV4i5xfHOc|Ca1pw2xrrk>
"""°°°
Operatori su *Sequenze*
°°°"""
# |%%--%%| <Ca1pw2xrrk|uT72fq0LQM>

s = "python programming"

# |%%--%%| <uT72fq0LQM|aTiDPN9jGv>

s[0]

# |%%--%%| <aTiDPN9jGv|Iaw7cfeFcN>

s[0:6]

# |%%--%%| <Iaw7cfeFcN|PrLbA9GlOb>

s[-1]

# |%%--%%| <PrLbA9GlOb|ib5CBV7q9S>

s[-2:]

# |%%--%%| <ib5CBV7q9S|djAndsyADC>

s[:6]

# |%%--%%| <djAndsyADC|792ekjSHW8>

s[0:6:3]

# |%%--%%| <792ekjSHW8|SgiXWfqjks>
"""°°°
~~~
[start:stop:step]
°°°"""
# |%%--%%| <SgiXWfqjks|1KuZMsVayK>
"""°°°
Concatenazione utilizzando l'operatore $\huge{+}$
°°°"""
# |%%--%%| <1KuZMsVayK|MF5Im3N0Tx>

s = "python"

# |%%--%%| <MF5Im3N0Tx|yGAtN9Tr6o>

len(s)

# |%%--%%| <yGAtN9Tr6o|PSZgJ9LE0o>

min(s)

# |%%--%%| <PSZgJ9LE0o|43f8B6gMDq>

max(s)

# |%%--%%| <43f8B6gMDq|X59r76wm0u>



# |%%--%%| <X59r76wm0u|Hi8IX6QUgN>
"""°°°
# Conversioni di tipo
°°°"""
# |%%--%%| <Hi8IX6QUgN|Xswdz9x8YP>
"""°°°
Interi:
* usiamo la funzione int()
* le stringhe diventano numeri interi (se sono numeri)
°°°"""
# |%%--%%| <Xswdz9x8YP|JYQGatvoLl>
"""°°°
Float:
* usiamo la funzione float()
* stesso discorso per gli interi
°°°"""
# |%%--%%| <JYQGatvoLl|1R6XfHWE7K>
"""°°°
Stringa:
* usiamo la funzione str()
* usata per i numeri che diventano elementi di stringa
°°°"""
# |%%--%%| <1R6XfHWE7K|SZcMK3LudI>
"""°°°
Booleano:
* usiamo la funzione bool()
* lo applichiamo a tutti gli elementi
°°°"""
# |%%--%%| <SZcMK3LudI|lsnv5TL1il>
"""°°°
# Strutture di dati in python
°°°"""
# |%%--%%| <lsnv5TL1il|wduPyZ3R2y>
"""°°°
# Liste, Tuple, Dizionari, Set
°°°"""
# |%%--%%| <wduPyZ3R2y|ItZS1cp3er>
"""°°°
Una sequenza è generalmente definita come un insieme ordinato di elementi indicizzati numericamente attraverso la loro posizione; l'indice parte sempre da $\huge{0}$
°°°"""
# |%%--%%| <ItZS1cp3er|wEOoGSAFbH>
"""°°°
Liste e Tuple caratteristiche:
* elementi di tipo qualunche
* le liste sono mutabili
* le tuple sono immutabili
°°°"""
# |%%--%%| <wEOoGSAFbH|mufKNttTuv>
"""°°°
## Liste
°°°"""
# |%%--%%| <mufKNttTuv|HfWgWzjB6i>
"""°°°
Sequenza di elementi qualunque, mutabili. L'instaza riguarda una classe predefinita che si chiama list.
°°°"""
# |%%--%%| <HfWgWzjB6i|2OiPAsJSN9>

myList1 = []
myList = [10, 20, 30]
lista_vuota = list()

# |%%--%%| <2OiPAsJSN9|RCWRQxcCLo>

myList[-1]

# |%%--%%| <RCWRQxcCLo|0cHwjdwsj4>
"""°°°
Valgono per lo slicing tutti i discorsi visti per le stringhe!
°°°"""
# |%%--%%| <0cHwjdwsj4|Pjl3hHvsPV>

nido = [1, 2, ["primo", "secondo", "terzo"]]

# |%%--%%| <Pjl3hHvsPV|3baJGGuJ6L>

nido[2][1]

# |%%--%%| <3baJGGuJ6L|PrmRe11Ifq>
"""°°°
modifichiamo la lista:
°°°"""
# |%%--%%| <PrmRe11Ifq|PUs2IxobyF>

nido[0] = "andrea"
nido[2][2] = "paese"

# |%%--%%| <PUs2IxobyF|hrEvcWnAij>

nido

# |%%--%%| <hrEvcWnAij|AlZQnTkxdr>

len(nido)

# |%%--%%| <AlZQnTkxdr|lG0yZlI8Wl>

nido.insert(1, "inserito")

# |%%--%%| <lG0yZlI8Wl|HKPYBGqcUA>

nido

# |%%--%%| <HKPYBGqcUA|ltk7HwWTCc>

nido.insert(-1, "ultimo")

# |%%--%%| <ltk7HwWTCc|rOmYKN1PTf>

nido

# |%%--%%| <rOmYKN1PTf|UKjUO4d1no>

nido[-1].append("ancora ultimo")

# |%%--%%| <UKjUO4d1no|CVBEFGyegY>

nido

# |%%--%%| <CVBEFGyegY|NxdPKLJoH7>

del nido[0]

# |%%--%%| <NxdPKLJoH7|uDrkBJJKYn>

nido

# |%%--%%| <uDrkBJJKYn|N5ZzOAnma2>

"ultimo" in nido

# |%%--%%| <N5ZzOAnma2|5kCYVFMGvV>

"paese" in nido[-1]

# |%%--%%| <5kCYVFMGvV|OAUr7fKddb>

"paese" in nido

# |%%--%%| <OAUr7fKddb|wcErPhhXkP>
"""°°°
## Due nomi, una lista
°°°"""
# |%%--%%| <wcErPhhXkP|OlsYx1wA1E>

lista1 = [1, 2, 3]
lista2 = lista1
lista2[1] = 60


# |%%--%%| <OlsYx1wA1E|ZuNDslF4xm>

lista1

# |%%--%%| <ZuNDslF4xm|8nF7fBU0xP>

lista2

# |%%--%%| <8nF7fBU0xP|7wq7oHZkEL>
"""°°°
Puntando alla stessa lista la variazione di una determina la variazione dell'altra... se questo non fosse il comportamento che vogliamo ritorna utile l'attributo COPY...
°°°"""
# |%%--%%| <7wq7oHZkEL|W5UrItl3a8>

lista1 = [1, 2, 3]
lista2 = lista1.copy()

# |%%--%%| <W5UrItl3a8|AEHImLf8iL>

lista2[0] = 60

# |%%--%%| <AEHImLf8iL|yYuL87jAGF>

lista1

# |%%--%%| <yYuL87jAGF|AisOKZ7xqf>

lista2

# |%%--%%| <AisOKZ7xqf|mbcl1dky3V>
"""°°°
## Tuple
°°°"""
# |%%--%%| <mbcl1dky3V|9TZrphVRLw>
"""°°°
La tupla è una sequenza $\huge{immutabile}$
°°°"""
# |%%--%%| <9TZrphVRLw|IryEMbCxBW>
"""°°°
Il tipo è la classe tuple()
°°°"""
# |%%--%%| <IryEMbCxBW|2yI46WpeV5>

medaglie = ()
medaglie = tuple()
elenco = "oro", "argento", "bronzo"

# |%%--%%| <2yI46WpeV5|nKhkNRRYmF>

print(type(elenco))

# |%%--%%| <nKhkNRRYmF|s7POldBaRR>

print(elenco)

# |%%--%%| <s7POldBaRR|bgqpA4QugN>
"""°°°
il Tuple $\huge{UNpacking}$
°°°"""
# |%%--%%| <bgqpA4QugN|D1H2PGAfwF>

primo, secondo, terzo = elenco

# |%%--%%| <D1H2PGAfwF|Q1Z2YIeubs>

primo

# |%%--%%| <Q1Z2YIeubs|AFDF1JBzin>

secondo

# |%%--%%| <AFDF1JBzin|fIVMxpjwE2>

terzo

# |%%--%%| <fIVMxpjwE2|pnDsXoe8BI>
"""°°°
## Dizionario
°°°"""
# |%%--%%| <pnDsXoe8BI|rj6Sctvrqf>
"""°°°
Nei dizionari l'ordine degli elementi non è definito, si usano delle chiavi univoche che vengono associate ai rispettivi valori.
°°°"""
# |%%--%%| <rj6Sctvrqf|keG4Jfoe26>
"""°°°
Le chiavi devono essere univoche. Gli elementi dei dizionari sono mutabili attraverso i metodi appartenenti ai dizionari.
°°°"""
# |%%--%%| <keG4Jfoe26|bdmMj0THDZ>
"""°°°
La classe dei dizionari è la dict().
°°°"""
# |%%--%%| <bdmMj0THDZ|KDQI6U90XA>

mioDizionario = {}
mioDizionario = dict()

# |%%--%%| <KDQI6U90XA|mYkAs94Fxy>

myDict = {
    "primo": 10,
    "secondo": 20,
    "terzo": 30
}

# |%%--%%| <mYkAs94Fxy|Hkko60BZPa>

myDict["quarto"] = 40

# |%%--%%| <Hkko60BZPa|nZX3lcn69w>

myDict

# |%%--%%| <nZX3lcn69w|qJw1fjwJM8>

del myDict["secondo"]

# |%%--%%| <qJw1fjwJM8|tJlRvoMGJw>

myDict


# |%%--%%| <tJlRvoMGJw|qLl6Vnui4A>
"""°°°
~~~
myDict.clear() # vuota il dizionario
°°°"""
# |%%--%%| <qLl6Vnui4A|x4sHxrJvd6>

"terzo" in myDict

# |%%--%%| <x4sHxrJvd6|ZLEKCiUjBi>

myDict2 = myDict.copy()

# |%%--%%| <ZLEKCiUjBi|2tBENw8vin>

myDict2

# |%%--%%| <2tBENw8vin|7lPT1fESeX>

myDict2["quinto"] = 50

# |%%--%%| <7lPT1fESeX|E2oMmdOSJL>

myDict2

# |%%--%%| <E2oMmdOSJL|fgUDFyu6Nf>

myDict

# |%%--%%| <fgUDFyu6Nf|gXAffC8Zep>

d1 = {10: "a"}
d2 = {20: "b"}

# |%%--%%| <gXAffC8Zep|KVwDO4iLcv>

d3 = {}

# |%%--%%| <KVwDO4iLcv|IZyN2piyzP>

d3.update(d1)

# |%%--%%| <IZyN2piyzP|kfpY3loFo2>

d3

# |%%--%%| <kfpY3loFo2|17Ixad3uPc>

d3.update(d2)

# |%%--%%| <17Ixad3uPc|H84gdWVw3q>

d3

# |%%--%%| <H84gdWVw3q|j1cSWkkQxy>
"""°°°
## SET
°°°"""
# |%%--%%| <j1cSWkkQxy|AOgOQ51N08>
"""°°°
Si tratta di insiemi, con tutte le operazioni matematiche che abbiamo per gli insiemi...
°°°"""
# |%%--%%| <AOgOQ51N08|lfA7zb2Uwv>

mySet = set()

# |%%--%%| <lfA7zb2Uwv|siAh3EdO8b>

mySet1 = {1, 2, 3, 4}

# |%%--%%| <siAh3EdO8b|u2WH3r0DUL>
"""°°°
Un set è un oggetto **mutabile**:
°°°"""
# |%%--%%| <u2WH3r0DUL|TU7JKoEkJ1>

mySet1.add(19)
print(mySet1)


# |%%--%%| <TU7JKoEkJ1|GU03ygHkDb>
"""°°°
Esiste anche la possibilità di usare dei Frozen SET...immutabili
°°°"""
# |%%--%%| <GU03ygHkDb|mzmqNEQ0tc>

gelo = frozenset([12, 23, 43])

# |%%--%%| <mzmqNEQ0tc|hZmZX6hC3O>

23 in gelo

# |%%--%%| <hZmZX6hC3O|pnNuYFIlDW>

2 in mySet1

# |%%--%%| <pnNuYFIlDW|SnLqpdwbHs>
"""°°°
Operazioni peculiari sugli insiemi: intersezione ed unione.
°°°"""
# |%%--%%| <SnLqpdwbHs|DAfq6NfAuS>

set1 = {10,20,30,40}
set2 = {30,40,50,60}

# |%%--%%| <DAfq6NfAuS|zeL3dxVYb6>

set1 & set2 # intersezione

# |%%--%%| <zeL3dxVYb6|qOie5LJONt>

set1.union(set2) # unione

# |%%--%%| <qOie5LJONt|RMsXKKswxd>

set1 | set2 # somma logica (unione)

# |%%--%%| <RMsXKKswxd|VPTU7X1Qfo>

set1 - set2 # differenza logica

# |%%--%%| <VPTU7X1Qfo|gcIVZjHJ6i>

set1 ^ set2 # or esclusivo: al primo o al secondo ma non entrambi

# |%%--%%| <gcIVZjHJ6i|iV1fhPMD79>
"""°°°
# Strutture di codice
°°°"""
# |%%--%%| <iV1fhPMD79|aimK4pLUPt>
"""°°°
## linee di codice e blocchi di codice
°°°"""
# |%%--%%| <aimK4pLUPt|8nE91NUTZE>
"""°°°
Abbiamo:
* linee logiche di codice (che vede python)
* linee fisiche (che scriviamo nel listato)
°°°"""
# |%%--%%| <8nE91NUTZE|EQwR4QwJDd>

s = "python \
programming \
language"
print(s) # 4 linee fisiche ma una sola linea logica

# |%%--%%| <EQwR4QwJDd|lehU0TXAus>
"""°°°
Un blocco di codice è un insieme di linee di codice raggruppate!
°°°"""
# |%%--%%| <lehU0TXAus|6RlUs1W6i9>
"""°°°
```
inp = input("inserisci un numero: ")
x = int(inp)
if x < 10:
    s = "numero minore di 10"
    print(s)
°°°"""
# |%%--%%| <6RlUs1W6i9|VRhrBynozb>
"""°°°
## Statement: istruzioni del programma
°°°"""
# |%%--%%| <VRhrBynozb|dA0fNWIU5w>
"""°°°
Operazioni che si richiede al codice python di eseguire:

```s = "andrea"```
°°°"""
# |%%--%%| <dA0fNWIU5w|m1ZI621TrP>
"""°°°
Statement semplici e composti
°°°"""
# |%%--%%| <m1ZI621TrP|9uj4MHZHPt>
"""°°°
```
if x < 10:
    s = "numero minore di 10"
    elif x == 10:
        s = "numero 10"
    else:
        s = "numero maggiore di 10
        print(s)
°°°"""
# |%%--%%| <9uj4MHZHPt|uI1o5Y8AEc>
"""°°°
Struttura di uno statement composto:
* contiene una o più clausole
* ogni clausola contiene una parola chiave di python detta HEADER e termina con il carattere :
* suite che contiene un blocco di codice, indentato rispetto all'HEADER
°°°"""
# |%%--%%| <uI1o5Y8AEc|cKpBHKwLN9>
"""°°°
## Lo statement IF
Viene utilizzato per definire una esecuzione condizionata del codice (azioni differenti rispetto al test di verità). 
°°°"""
# |%%--%%| <cKpBHKwLN9|aOVdMtKuln>
"""°°°
La clausola ELSE viene eseguita solo se tutte le precedenti danno come risultato FALSE; possiamo ometterla per fare in modo che nel caso di tutti FALSE non venga eseguito nulla!
°°°"""
# |%%--%%| <aOVdMtKuln|3ph8Y0DLJH>

x = 10
if x > 11:
    print("il numero è maggiore di 11") # manca la clausola else

# |%%--%%| <3ph8Y0DLJH|dljhV6bXVp>
"""°°°
## Lo statement WHILE
La else è facoltativa ma poco utilizzata
°°°"""
# |%%--%%| <dljhV6bXVp|UBmFIZoDEP>
"""°°°
Se è presente la clausola ELSE si entra nel ciclo sempre: se l'espressione risulterà FALSE ci entreremo direttamente senza passare dal True.
°°°"""
# |%%--%%| <UBmFIZoDEP|Vuyyo7KNr1>
"""°°°
```
x = 0
while x < 3:
    print(x)
    x += 1
°°°"""
# |%%--%%| <Vuyyo7KNr1|tmHCbFw6rx>
"""°°°
Spesso si vuole eseguire un loop senza sapere quando la condizione sarà verificata; in questo caso utilizzeremo $\color{green}{break}$ per uscire dal loop.
°°°"""
# |%%--%%| <tmHCbFw6rx|XwCfZT7Ivz>
"""°°°
Diverso è lo statement $\color{red}{continue}$ il quale non esce dal ciclo ma lo fà ripartire dall'inizio!
°°°"""
# |%%--%%| <XwCfZT7Ivz|AljtPhxaxc>

while True:
    x = input("inserire una stringa ")
    if x == "stop":
        break
    if x < "b":
        continue
    print(x) # tutte le stringhe < b non vengono stampate perchè si ritorna al primo if

# |%%--%%| <AljtPhxaxc|KanNAdZEVr>
"""°°°
## Ciclo FOR
°°°"""
# |%%--%%| <KanNAdZEVr|xUyW9CsxLC>
"""°°°
```
for target in iterator:
    suite
else:
    suite
°°°"""
# |%%--%%| <xUyW9CsxLC|rtLP3s2ewL>
"""°°°
L'iterazione termina quando tutti gli elementi di iterator sono stati processati. La clausola else, poco utilizzata, solo se tutti gli elementi sono stati iterati.
°°°"""
# |%%--%%| <rtLP3s2ewL|3oliOshscB>

myList = [1, 3, 4, 5]
for i in myList:
    if i <= 4:
        print(i)
    else:
        break
else:
    print("ho iterato tutti gli elementi")

# |%%--%%| <3oliOshscB|ibr5H54diH>

for i in myList:
    if i <= 9:
        print(i)
    else:
        break
else:
    print("ho iterato tutti gli elementi")

# |%%--%%| <ibr5H54diH|6OE6fHXWpf>
"""°°°
L'iterazione sui dizionari assegna alla variabile TARGET le KEY.
```
for i in myDict...
°°°"""
# |%%--%%| <6OE6fHXWpf|POaR7Ugqa4>
"""°°°
```
for i in myDict.items()
```
restituisce delle tuple chiave valore.
°°°"""
# |%%--%%| <POaR7Ugqa4|lSFC1jICdY>
"""°°°
CONTINUE nel ciclo for avanza l'iterazione saltando l'elemento indicato:
°°°"""
# |%%--%%| <lSFC1jICdY|XeIHSLvLnp>

for i in [1, 3, 5, 7]:
    if i == 5:
        continue
    print(i)

# |%%--%%| <XeIHSLvLnp|yQF6STEnb7>
"""°°°
## La funzione RANGE
range(start, stop, step)... lo STOP è SEMPRE escluso!
°°°"""
# |%%--%%| <yQF6STEnb7|M9eRxsroEa>
"""°°°
## List comprehension
°°°"""
# |%%--%%| <M9eRxsroEa|MxcOvSDnrH>
"""°°°
Si tratta di un argomento avanzato ma molto importante perchè si tratta di uno strumento molto 
potente!
°°°"""
# |%%--%%| <MxcOvSDnrH|m6F0fLUrt0>
"""°°°
[expression for item in iterable if condition]
°°°"""
# |%%--%%| <m6F0fLUrt0|Evg23zKcaK>

miaLista = [1, 3, 5, 7, 8, 9, 12]

# |%%--%%| <Evg23zKcaK|3oGukEcoAR>

l =[x for x in miaLista if x > 5]
print(l)

# |%%--%%| <3oGukEcoAR|PIy5soUgaR>

s = [x * 10 for x in miaLista]
print(s)

# |%%--%%| <PIy5soUgaR|5vRAFCmSnt>

p = [x*x for x in miaLista if x % 2 == 0]
print(p)

# |%%--%%| <5vRAFCmSnt|3Ql7wJbSCL>
"""°°°
## Dict comprehension
°°°"""
# |%%--%%| <3Ql7wJbSCL|0YbCoBVk8c>

nomi = {10: "andrea", 20: "mario", 30: "anna", 40: "giuseppe"}

# |%%--%%| <0YbCoBVk8c|HITzRpnVCZ>

mioDizionario = {k:v for k,v in nomi.items() if k > 20}
print(mioDizionario)

# |%%--%%| <HITzRpnVCZ|zD6VTnjGAT>

nomiDict = {k:v for k,v in nomi.items() if k <= 20}
print(nomiDict)

# |%%--%%| <zD6VTnjGAT|GfeXB3NyqT>

cambiato= {(k+30):v for k,v in nomi.items()}
print(cambiato)

# |%%--%%| <GfeXB3NyqT|R8Cykvy7C0>
"""°°°
# Set comprehension
Ricordiamo che il set non può contenere elementi DUPLICATI.
°°°"""
# |%%--%%| <R8Cykvy7C0|NtLUZTg0lX>

lista = [ 1, 5, 7, 8, 9]

# |%%--%%| <NtLUZTg0lX|TglZujPSPf>

nuovo = {x for x in lista if x < 7}
print(nuovo)

# |%%--%%| <TglZujPSPf|NbkQf2kGyg>
"""°°°
# le Funzioni
°°°"""
# |%%--%%| <NbkQf2kGyg|vCKA9bL4BX>
"""°°°
Insieme di istruzioni con un nome, eseguita a richiesta in altre parti del programma. Una
funzione è un OGGETTO, Callable Object (oggetti chiamabili).
°°°"""
# |%%--%%| <vCKA9bL4BX|nwmuZClvlR>
"""°°°
Due cose si possono fare con una funzione:
* definirla
* chiamarla
°°°"""
# |%%--%%| <nwmuZClvlR|Cls6DpEbl1>
"""°°°
## Definizione di una funzione
°°°"""
# |%%--%%| <Cls6DpEbl1|9HcYjyljya>
"""°°°
``` 
def function_name(parameters):
            statements
°°°"""
# |%%--%%| <9HcYjyljya|Iepma5wQ60>
"""°°°
Quando passiamo i valori ai parametri, questi si chiamano argomenti!
°°°"""
# |%%--%%| <Iepma5wQ60|iIbQei0YPQ>
"""°°°
## Parametri della funzione
°°°"""
# |%%--%%| <iIbQei0YPQ|rQIihDJ9hj>

def myFunc(a, b):
    print(a, b)  # parametri posizionali, in chiamata sono necessari nell'ordine dato

# |%%--%%| <rQIihDJ9hj|IuZrIgVvjg>

def myFunc(a, b):
    print(a, b) # keyword possiamo passarli nell'ordine che vogliamo...

myFunc(b=10, a=30)

# |%%--%%| <IuZrIgVvjg|5f8fK4N8Nd>

myFunc(10, b=50) # prima i posizionali poi le keyword

# |%%--%%| <5f8fK4N8Nd|rzRFN8e8Ps>

def myFunc(a, b, c=4):
    print(a, b)  #parametri opzionali possono mancare nella chiamata

# |%%--%%| <rzRFN8e8Ps|Zigo55Kf0L>

def myFunc(*args):
    print(args) # il nome è convenzionale, inserisce i valori in una tupla, variabile

# |%%--%%| <Zigo55Kf0L|iB3BfXHmrP>

def myFunc(a, b, *args):
    print(a, b, args) # i posizionali sempre prima

# |%%--%%| <iB3BfXHmrP|jo9U7v1STv>

myFunc(1,5, 6,8,9)

# |%%--%%| <jo9U7v1STv|gau6bNHhlD>

def myFunc(**kwargs):
    print(kwargs)

# |%%--%%| <gau6bNHhlD|YVSrhvX3s4>

myFunc(andrea=1, mario=2)

# |%%--%%| <YVSrhvX3s4|8kRRFQnSTz>
"""°°°
## Lo statement $\color{red}{RETURN}$
°°°"""
# |%%--%%| <8kRRFQnSTz|YXS2ccyg1t>

def sum(a, b):
    return a + b  # return può non essere seguito da una espressione

# |%%--%%| <YXS2ccyg1t|jlJvORxEEb>
"""°°°
Se non indichiamo nessuna espressione, il ritorno sarà None...
°°°"""
# |%%--%%| <jlJvORxEEb|NEY1fH3tVj>

def sum(a, b):
    c = a + b # torna al chiamante il valore None...

# |%%--%%| <NEY1fH3tVj|8fo2psaLm7>

## Chiamare le funzioni

# |%%--%%| <8fo2psaLm7|GDa8Wvqx1G>
"""°°°
```function_name(arguments)```
°°°"""
# |%%--%%| <GDa8Wvqx1G|6mRjxZBrua>
"""°°°
I valori vengono passati come riferimento!
°°°"""
# |%%--%%| <6mRjxZBrua|Vgcp5zA5k7>

def myFunc(x):
    x = 10
    print(x) 

# |%%--%%| <Vgcp5zA5k7|qPeeD9KYR9>

y = 20
myFunc(y)
print(y) # l'oggetto originario è immutabile e non ha modificato il suo contenuto

# |%%--%%| <qPeeD9KYR9|YvrNfQSA8G>

def myFunc(x):
    x["func"] = 10

# |%%--%%| <YvrNfQSA8G|qrkUTXfutm>

d = {"a": 5}
myFunc(d)
print(d) # d è un dizionario, mutabile, ergo è stato effettivamente mutato

# |%%--%%| <qrkUTXfutm|t9oMWsUMUZ>
"""°°°
## Funzioni come OGGETTI
°°°"""
# |%%--%%| <t9oMWsUMUZ|96rsyHO50A>

def sum(x, y):
    print(x + y)

# |%%--%%| <96rsyHO50A|0a5ebLX61s>

sum(10, 5) # invochiamo la funzione

# |%%--%%| <0a5ebLX61s|yt38vHqi1Q>

sum # chiamiamo l'oggetto funzione, istanza della classe function

# |%%--%%| <yt38vHqi1Q|I5uiboHG97>
"""°°°
## Usare gli oggetti funzione
°°°"""
# |%%--%%| <I5uiboHG97|KSlgtX8Y7B>

def outer(x, y):
    def sum(a, b):
        return a + b
    print(sum(x, y))       # funzione nidificata

# |%%--%%| <KSlgtX8Y7B|sjfbYqg5I1>

outer(10,5)

# |%%--%%| <sjfbYqg5I1|q9gQgVYdxd>

sum(19,1)

# |%%--%%| <q9gQgVYdxd|A01f2KsmJL>

def outer():
    def inner(a, b):
        print(a + b)
    return inner

# |%%--%%| <A01f2KsmJL|CW3zgDFP77>

outer()

# |%%--%%| <CW3zgDFP77|xWnR0f6aqo>

f = outer()
f(10, 5)

# |%%--%%| <xWnR0f6aqo|VTWGqYNgac>

def somma(a,b):
    print(a+b)

def sottrai(a,b):
    print(a-b)

def myFunc(f, x, y):
    f(x,y)

# |%%--%%| <VTWGqYNgac|n4BnphZAWy>

myFunc(somma, 10, 5) 
myFunc(sottrai, 10, 5) # ho passato la funzione come argomento oggetto funzione

# |%%--%%| <n4BnphZAWy|kHFFCJdqi6>
"""°°°
## Namespace e Scope
°°°"""
# |%%--%%| <kHFFCJdqi6|oa9E7hI9kv>
"""°°°
Namspace:

1. mappatura di nomi ad oggetti
2. namespace multipli, a Runtime 
3. organizzati in una gerarchia
4. cicli di vita differenti
°°°"""
# |%%--%%| <oa9E7hI9kv|HEQ6jVa6rw>
"""°°°
Scope:

area di codice che determona il namespace da utilizzare per la risoluzione dei nomi.
°°°"""
# |%%--%%| <HEQ6jVa6rw|4AO4vY9B36>
"""°°°
Namespace: gerarchia LEGB:
* local
* enclosed
* global
* built-in
°°°"""
# |%%--%%| <4AO4vY9B36|qhKqelbtMQ>
"""°°°
## local scope
livello interno di una funzione, viene creato una volta chiamata la funzione, rimosso una volta ottenuto il ritorno della funzione stessa.
°°°"""
# |%%--%%| <qhKqelbtMQ|iCCtGCNMfg>
"""°°°
E' il primo punto dove python cerca di risolvere i nomi!
°°°"""
# |%%--%%| <iCCtGCNMfg|rRjfz8i6IS>
"""°°°
## enclosed
nel caso di funzioni nidificate è il secondo punto in cui viene cercata la risoluzione de nomi.m
°°°"""
# |%%--%%| <rRjfz8i6IS|sxssGNUUAj>
"""°°°
```
def outer(x):
    y = 20
    def inner():
        print(x+y)
    
°°°"""
# |%%--%%| <sxssGNUUAj|w8dA670WDr>
"""°°°
## global namespace
Tutti i nomi definiti dal livello del sorgente quando i nomi sono indicati al di fuori di tutte le funzioni.
°°°"""
# |%%--%%| <w8dA670WDr|luTD6SxDi6>
"""°°°
```
x = 20
def miaFunc(y):
    print(x + y)
°°°"""
# |%%--%%| <luTD6SxDi6|0KRo6obF6j>
"""°°°
## Built-In namespace (predefinito)
Definto direttamente dall'ambiente di runtime di python, contiene, ad esempio, la risoluzione print, list, dict, tuple, ...
°°°"""
# |%%--%%| <0KRo6obF6j|EWHQegW8yv>
"""°°°
## Global e Nonlocal
°°°"""
# |%%--%%| <EWHQegW8yv|mor0cNZCCr>
"""°°°
Servono ad alterare la gerarchia standard nella ricerca della risoluzione dei nomi da parte di python.
°°°"""
# |%%--%%| <mor0cNZCCr|aupgIvBDlO>
"""°°°
Variabile Hiding:

se utilizziamo un nome di variabile già presente a livelli di scope più alti, questa avrà la precedenza sulle altre, in un certo senso nascondendole!
°°°"""
# |%%--%%| <aupgIvBDlO|miYxBko2MM>
"""°°°
Per alterare questo comportamento utilizziamo la parola $\color{red}{global}$
°°°"""
# |%%--%%| <miYxBko2MM|iI8odaU5uh>
"""°°°
```
x = 100
def myFunc():
    global x
    x = 20
    print(x)
°°°"""
# |%%--%%| <iI8odaU5uh|eR53sEkDWa>
"""°°°
In questo caso abbiamo alterato la variabile globale!
°°°"""
# |%%--%%| <eR53sEkDWa|VCqbqkJbjc>
"""°°°
Nonlocal cerca la variabile nel namespace della funzione madre (in funzioni nidificate).m
°°°"""
# |%%--%%| <VCqbqkJbjc|XnQgLoc4WQ>

def outer():
    y = 20
    def inner():
        nonlocal y
        y = 50
        print("variabile in inner %s" %(y))
    inner()
    print("variabile in outer %s" %(y))

# |%%--%%| <XnQgLoc4WQ|tufAtIjNxU>

outer()

# |%%--%%| <tufAtIjNxU|B2gicRMeJg>
"""°°°
# Function Decorator (decoratori di funzione)
°°°"""
# |%%--%%| <B2gicRMeJg|WA5eBKdB9Q>
"""°°°
Un decoratore di una funzione è una funzione che prende in input una funzione, la decora con altri contenuti e restituisce il nuovo valore.
°°°"""
# |%%--%%| <WA5eBKdB9Q|1bxVqQqgSn>
"""°°°
Utilizzo: modificare il comportamento di una funzione senza alterarne il codice sorgente!
°°°"""
# |%%--%%| <1bxVqQqgSn|BwI5BBVU8B>

def myDecorator(f):
    def decorator():
        print("ho decorato")
        f()
    return decorator

# |%%--%%| <BwI5BBVU8B|8nZbPoXVGW>

def myFunc():
    print("la funzione myFunc")

# |%%--%%| <8nZbPoXVGW|BPfSLlWAhp>

decorata = myDecorator(myFunc)

# |%%--%%| <BPfSLlWAhp|oBdWhGVcYK>

decorata()

# |%%--%%| <oBdWhGVcYK|9EexlbLJMG>

## con il decoratore...

# |%%--%%| <9EexlbLJMG|xVVXmw1ikr>

def myDecorator(f):
    def decorator():
        print("ho decorato con il decoratore")
        f()
    return decorator

# |%%--%%| <xVVXmw1ikr|TIgnD0goo9>

@myDecorator
def myFunc():
    print("la funzione myFunc")

# |%%--%%| <TIgnD0goo9|fBqBtseUn3>

myFunc()

# |%%--%%| <fBqBtseUn3|SvD08xZnWQ>

def mioDecoratore(func_destinazione):
    def wrapper(*args):
        print("elementi prima della funzione")
        func_destinazione()
        print("elementi dopo la funzione")
    return wrapper

# |%%--%%| <SvD08xZnWQ|rg9BpyrWvk>
"""°°°
> Nel caso in cui volessimo eseguire una funzione decorate SENZA decoratore, dopo aver importato 

```
from undecorated import undecorated (pip install)
```
useremo la sintassi ```undecorated(funzione)(parametri)```
°°°"""
# |%%--%%| <rg9BpyrWvk|Y79odzoyRX>
"""°°°
Quindi se chiameremo la funzione decorata direttamente otterremo la decorazione come previsto, se useremo undecorated... otterremo la funzione NON decorata!
°°°"""
# |%%--%%| <Y79odzoyRX|qU0FKHvrHb>
"""°°°
# Lambda function
°°°"""
# |%%--%%| <qU0FKHvrHb|X4aRwhwUkc>
"""°°°
Un'espressione che genera un oggetto funzione!
°°°"""
# |%%--%%| <X4aRwhwUkc|vZOgMyWfXy>
"""°°°
Lambda ritorna una funzione $\color{green}{anonima}$
°°°"""
# |%%--%%| <vZOgMyWfXy|gx0YVzOVmf>
"""°°°
```lambda arg1, arg2, argN : expression (con gli argomenti)```
°°°"""
# |%%--%%| <gx0YVzOVmf|KBM5T82Iik>

risultato = lambda x,y : x * y


# |%%--%%| <KBM5T82Iik|FTNuHvA1jU>

print("il valore richiesto è ", risultato(2,3))

# |%%--%%| <FTNuHvA1jU|OIoTFznrjh>
"""°°°
# Object-Orientation
°°°"""
# |%%--%%| <OIoTFznrjh|AJwH9S1R00>
"""°°°
* definizione di classi
* creazione istanze di classi
* come strutturare le classi in gerarchie di generalizzazione

°°°"""
# |%%--%%| <AJwH9S1R00|lWKa3eXtvQ>
"""°°°
## Classi ed Istanze
°°°"""
# |%%--%%| <lWKa3eXtvQ|GbigGG09tL>
"""°°°
funzioni --> metodi di classe
°°°"""
# |%%--%%| <GbigGG09tL|g7jB4OHy3Y>
"""°°°
## Lo Statement Class
Un oggetto composto che serve a creare degli oggetti attraverso la sua istanziazione.
°°°"""
# |%%--%%| <g7jB4OHy3Y|iIBKG9Lgjr>
"""°°°
```
class Classname(base-classes): (base-classes sono le superclassi, le classi padre)
    statements
    
°°°"""
# |%%--%%| <iIBKG9Lgjr|4YlN5mq6Ze>
"""°°°
Nello statement ci saranno metodi ed attributi della classe...
°°°"""
# |%%--%%| <4YlN5mq6Ze|UZpFcNf9Mo>

class MyClass: # la convenzione python prevede la lettera maiuscola per le classi
    pass

# |%%--%%| <UZpFcNf9Mo|Jx4CFmueiS>
"""°°°
Non abbiamo usato le parentesi tonde, indicando che la classe di orgine è la object, propria di python...
°°°"""
# |%%--%%| <Jx4CFmueiS|kYmWv0PoBg>
"""°°°
istanza di una classe:

```
myObj = MyClass()
```
°°°"""
# |%%--%%| <kYmWv0PoBg|wh7seYGeKE>
"""°°°
## Attributi di Classe
Gli attributi possono essere di classe o di istanza. 
* attributi di classe: condivisi da tutte le istanze della classe
* attributi di istanza: propri di quella e solo quella istanza, non della classe
°°°"""
# |%%--%%| <wh7seYGeKE|DkWfq2Hcdi>

class MyClass:
    myAttr = 10

# |%%--%%| <DkWfq2Hcdi|HkRljWqvsL>

m1 = MyClass()
m2 = MyClass()

# |%%--%%| <HkRljWqvsL|XPQnLmJLX1>

m1.myAttr

# |%%--%%| <XPQnLmJLX1|gEJPEGE2do>

m2.myAttr = 40
m2.myAttr

# |%%--%%| <gEJPEGE2do|4uMTsHZu2R>

m2.attributo = 555

# |%%--%%| <4uMTsHZu2R|fCsaaMMsoD>

print(m2.myAttr)
print(m2.attributo) # non è presente nella classe, diventa un attributo di istanza!

# |%%--%%| <fCsaaMMsoD|uQVQOJ7v93>
"""°°°
## Metodi di istanza
°°°"""
# |%%--%%| <uQVQOJ7v93|oFjqnZM4HJ>

class MyClass:
    def myMethod(self):
        print(id(self)) # metodo di classe e self che rappresenta l'istanza invocata dal                           metodo

# |%%--%%| <oFjqnZM4HJ|fOJ5Qjihvj>

m1= MyClass()
m2 = MyClass()

# |%%--%%| <fOJ5Qjihvj|IoT6PlN0HJ>

m1.myMethod()

# |%%--%%| <IoT6PlN0HJ|YgcamNqqX3>

m2.myMethod()

# |%%--%%| <YgcamNqqX3|aUtVecOnva>

MyClass.myMethod(m1)

# |%%--%%| <aUtVecOnva|iblcEmRr3C>

MyClass.myMethod(m2)

# |%%--%%| <iblcEmRr3C|L7CNodYpBz>
"""°°°
## Attributi di ISTANZA
°°°"""
# |%%--%%| <L7CNodYpBz|6SBjyhIGN1>

class MyClass:
    def setMessage(self, message):
        self.message = message
    def printMessage(self):
        print(self.message)

# |%%--%%| <6SBjyhIGN1|5Qd2cJIojA>
"""°°°
In questo codice c'è un problema: se chiamiamo in istanza direttamente il metodo printMessage, otterremo un errore in quanto non è stato settato il messaggio; per ovviare a questo problema dovremo definire dei metodi di inizializzazione.
°°°"""
# |%%--%%| <5Qd2cJIojA|2JsEb8qCy8>
"""°°°
## il costruttore __init__
Viene chiamato sempre ed automaticamente ogni volta che una istanza di classe viene attivata.
°°°"""
# |%%--%%| <2JsEb8qCy8|dXd1EwQoQJ>

class MyClass:
    def __init__(self, message):
        self.message = message
    def printMessage(self):
        print(self.message)

# |%%--%%| <dXd1EwQoQJ|YfkdKbXQQa>

m1 = MyClass()

# |%%--%%| <YfkdKbXQQa|NnY78ow8G1>

m1 = MyClass("ciao")

# |%%--%%| <NnY78ow8G1|EPKtLa27A0>

m1.printMessage()

# |%%--%%| <EPKtLa27A0|bjSJq9HhvF>
"""°°°
## Metodi di classe
Eseguiti non sulle istanze ma proprio sull'oggetto classe!
°°°"""
# |%%--%%| <bjSJq9HhvF|RzCjm5mb0p>

class MyClass:
    counter = 0 #attributo della classe
    def __init__(self):
        MyClass.counter += 1
    @classmethod
    def istanze(cls): # cls indica l'oggetto classe
        print(cls.counter)

# |%%--%%| <RzCjm5mb0p|jFeOv9gic0>

m1 = MyClass()
m2 = MyClass()
m3 = MyClass()

# |%%--%%| <jFeOv9gic0|LQsAWBkTAZ>

MyClass.istanze()

# |%%--%%| <LQsAWBkTAZ|wTgUZ7SVIA>



# |%%--%%| <wTgUZ7SVIA|OIBm7Gfpku>
"""°°°
## STATIC Methods
°°°"""
# |%%--%%| <OIBm7Gfpku|VwvznbzJhp>

class MyClass:
    @staticmethod
    def somma(a,b):
        return(a + b)

# |%%--%%| <VwvznbzJhp|oyNqYilYMN>

s = MyClass.somma(10,5)
print(s)

# |%%--%%| <oyNqYilYMN|dcUpnI3oJX>
"""°°°
Non si riferisce alle classi e nemmeno alle istanze!
°°°"""
# |%%--%%| <dcUpnI3oJX|C5y3fKM73m>
"""°°°
# Inheritance (ereditarietà)
°°°"""
# |%%--%%| <C5y3fKM73m|ygoeqEcINB>

class BClass: #superclasse
    pass

class AClass(BClass):
    pass

# |%%--%%| <ygoeqEcINB|K0Y4Ph1x1X>
"""°°°
La funzione isinstance
```
m1 = AClass()
isinstance(m1, AClass) True
isinstance(m1, BClass) True

°°°"""
# |%%--%%| <K0Y4Ph1x1X|RMtF3n6ZWh>

m1 = AClass()

# |%%--%%| <RMtF3n6ZWh|ejvsg3eyJf>

isinstance(m1, BClass)

# |%%--%%| <ejvsg3eyJf|HHZrfuFwWS>
"""°°°
## Override
Possiamo ridefinire un attributo all'ìnterno di una sottoclasse
°°°"""
# |%%--%%| <HHZrfuFwWS|RrszwLFD0s>

class BClass:
    def setMessage(self, message):
        self.message = message
    def printMessage(self):
        print(self.message)

class AClass(BClass):
    def printMessage(self):
        print("AClass " + self.message)

# |%%--%%| <RrszwLFD0s|OUl2bz6ODe>

m1 = AClass()
m1.setMessage("andrea")
m1.printMessage()

# |%%--%%| <OUl2bz6ODe|UzdtbeUJCj>
"""°°°
Questo metodo non è un metodo corretto, vediamo la procedura corretta con il costruttore.
Infatti quando invochiamo la sottoclasse, se questa ha un suo costruttore viene usato ma, nella sintassi utilizzata, non viene considerato il costruttore della superclasse, viene sovrascritto il costruttore!
°°°"""
# |%%--%%| <UzdtbeUJCj|isPAcaRMzg>
"""°°°
# la funzione SUPER
°°°"""
# |%%--%%| <isPAcaRMzg|W2JNbRp1b1>

class BClass:
    def __init__(self, message):
        self.message = message
    def printMessage(self):
        print(self.message)
    def scatola(self):
        scatola = "BICHER"
        return scatola

class AClass(BClass):
    def __init__(self, message, valore):
        super().__init__(message)
        self.valore = valore

# |%%--%%| <W2JNbRp1b1|cchsrAT9nR>

m1 = AClass("andrea", 100)

# |%%--%%| <cchsrAT9nR|KiUisYqAjX>

m1.printMessage()

# |%%--%%| <KiUisYqAjX|yi9kx9rX0Q>

m1.valore

# |%%--%%| <yi9kx9rX0Q|2WkulbqWYk>
"""°°°
non si usa solo per invocare init della superclasse, ma per accedere a tutto il contenuto della stessa:
°°°"""
# |%%--%%| <2WkulbqWYk|MFEPO6agMl>

class CClass(BClass):
    def __init__(self, name):
        self.nome = name
        super().scatola()
    

# |%%--%%| <MFEPO6agMl|40lbtsOVcq>

m2 = CClass("valerio")

# |%%--%%| <40lbtsOVcq|IKuEriydTc>

m2.scatola()

# |%%--%%| <IKuEriydTc|rLtzw2BikY>
"""°°°
## Properties
Information HIDING
possibilità di rendere privati degli attributi che rappresentano dei dati, nascosti all'esterno della classe. i Metodi setter e getter settano e leggono gli attributi privati.

°°°"""
# |%%--%%| <rLtzw2BikY|4zqlBSZOWd>

class MyClass:
    def __init__(self, my_attr):
        self.priv_attr = my_attr
    def get_attr(self):
        return self.priv_attr
    def set_attr(self, attr):
        self.priv_attr = attr
    
    attr = property(get_attr, set_attr) # costruiamo una proprietà che nasconde attr

# |%%--%%| <4zqlBSZOWd|iWq5iILXUx>

obj = MyClass("andrea")
obj.attr

# |%%--%%| <iWq5iILXUx|CSMz6g60c8>
"""°°°
Gli attributi che iniziano con doppio underscore non sono accessibli al di fuori della classe:
°°°"""
# |%%--%%| <CSMz6g60c8|r7WQITLjMt>

class MyClass:
    def __init__(self, my_attr):
        self.__priv_attr = my_attr
    def get_attr(self):
        return self.__priv_attr
    def set_attr(self, attr):
        self.__priv_attr = attr
    
    attr = property(get_attr, set_attr) # costruiamo una proprietà che nasconde attr

# |%%--%%| <r7WQITLjMt|99g7IKRiSO>

obj1 = MyClass("nascosto")
obj1.__private_attr

# |%%--%%| <99g7IKRiSO|W6N2gBWzXA>

obj1._MyClass__priv_attr # accesso diretto al nostro attributo name Mangling

# |%%--%%| <W6N2gBWzXA|KCwrpULOYo>
"""°°°
## Property Decorators
°°°"""
# |%%--%%| <KCwrpULOYo|1nChZd8HNL>
"""°°°
Le proprietà forniscono un modo di personalizzare l’accesso agli attributi dell’istanza. Per crearli, si utilizza il decoratore @property messo prima del metodo. Il loro scopo è quello di definire attributi read-only (non possono essere modificati). 
°°°"""
# |%%--%%| <1nChZd8HNL|Gb1tfxYfDT>
"""°°°
```
@property (decoratore del metodo getter)
@name.setter (decoratore del metodo setter)
°°°"""
# |%%--%%| <Gb1tfxYfDT|TqvsC2GcgO>

class MyClass():
    def __init__(self, my_attr):
        self.__priv_attr = my_attr

    def metodoPrivato(self):
        print("Ciao") #questo metodo non può essere chiamato fuori dalla classe!

    @property
    def attr(self):
        return self.__priv_attr

    @attr.setter
    def attr(self, my_attr):
        self.__priv_attr = my_attr


# |%%--%%| <TqvsC2GcgO|XjC2ayr68G>

obj = MyClass("decorato")
obj.attr

# |%%--%%| <XjC2ayr68G|geNRn2xXr7>


obj.__metodoPrivato()

# |%%--%%| <geNRn2xXr7|CRodbPnisM>



# |%%--%%| <CRodbPnisM|MxObedK4UU>
"""°°°
# Exceptions
°°°"""
# |%%--%%| <MxObedK4UU|pY3RzRkV3t>
"""°°°
Le eccezioni sono degli oggetti che appartengono ad una gerarchia base di python, ma possiamo anche crearne di nuove secondo le nostre necessità!
°°°"""
# |%%--%%| <pY3RzRkV3t|fK8NlKaU3I>

def myFunc(a,b):
    return a // b

# |%%--%%| <fK8NlKaU3I|PGe11nKCEj>

myFunc(10,0)

# |%%--%%| <PGe11nKCEj|aLys7FlA4a>
"""°°°
Viene elevata un'eccezione di divisione per ZERO!
°°°"""
# |%%--%%| <aLys7FlA4a|yJI9o1gLhT>
"""°°°
Nessuno ha detto ha python come gestire questa eccezione e quindi viene invocato il messaggio standard (si tratta di un oggetto). Il runtime prima verifica se noi abbiamo definito un modo per gestire questa eccezione, se non lo trova risale di uno stack alla volta fino ad arrivare alla interruzione del programma mostrando l'errore connesso a questa eccezione.
°°°"""
# |%%--%%| <yJI9o1gLhT|WETCZmtYyN>
"""°°°
Tutte le eccezioni sono istanze di una particolare classe sempre tutte sottoclassi di BaseException!
°°°"""
# |%%--%%| <WETCZmtYyN|R9ujEbWlRV>
"""°°°
ZeroDivisionError ==> ArithmeticError ==> Exception ==> BaseException ==> object
°°°"""
# |%%--%%| <R9ujEbWlRV|BjMlMLUGZx>
"""°°°
## lo Statement try/except (si tratta di uno statement composto)
°°°"""
# |%%--%%| <BjMlMLUGZx|mu9Qhgm9Ep>
"""°°°
```
try:

    suite

except:

    suite

°°°"""
# |%%--%%| <mu9Qhgm9Ep|oJ8Axv2OIu>

def myFunc(a,b):
    try:
        a // b
    except (ZeroDivisionError, ValueError):
        print("non posso dividere per zero")
    except IndexError:
        print("IndexError")

# |%%--%%| <oJ8Axv2OIu|Mf4qQKUe25>

myFunc(120,0)

# |%%--%%| <Mf4qQKUe25|aRg1cJzG47>

def myFunc(a,b):
    try:
        return a // b
    except ZeroDivisionError as e:
        print("Errore della funzione\n",e.args)

# |%%--%%| <aRg1cJzG47|RHLrC7PIfA>

myFunc(10,0)

# |%%--%%| <RHLrC7PIfA|yQniynOcke>
"""°°°
La clausolo FINALLY viene usata per eseguire sempre, a prescindere dall'errore, una serie di istruzioni.
°°°"""
# |%%--%%| <yQniynOcke|VtFoNuHynC>

def myFunc(a,b):
    try:
        a // b
    except ZeroDivisionError:
        print("Errore di divisione")
    finally:
        print("abbiamo provato ad eseguire la tua funzione")

# |%%--%%| <VtFoNuHynC|e4198yJsdc>

myFunc(10,6)

# |%%--%%| <e4198yJsdc|nDJeGrU8Pt>

myFunc(29,0)

# |%%--%%| <nDJeGrU8Pt|h9M1IR6Los>
"""°°°
Dopo tutte le clausole except possiamo eseguire una else (se tutto andrà bene verrà eseguita la clausola else). Potremmo usare anche una finally, ma in questo caso else deve essere posta PRIMA della finally.
°°°"""
# |%%--%%| <h9M1IR6Los|0F5lzAXsW3>

def myFunc(a,b):
    try:
        a // b
        risultato = True
    except ZeroDivisionError:
        print("Errore di divisione")
        risultato = False
    else:
        print("tutto a posto, abbiamo eseguito la funzione")
        
    finally:
        if risultato == True:
            print("siamo giunti alla fine eseguendo la tua funzione")
        else:
            print("non abbiamo potuto finire")
        

# |%%--%%| <0F5lzAXsW3|UFZcf85e9I>

myFunc(28,5)

# |%%--%%| <UFZcf85e9I|ZHoCShEAUW>

myFunc(10,0)

# |%%--%%| <ZHoCShEAUW|Na0hroXokq>
"""°°°
## Gli statement raise ed assert
°°°"""
# |%%--%%| <Na0hroXokq|hKqfHXfoDz>
"""°°°
>> raise si usa per sollevare esplicitamente una eccezione

La classe di eccezione dopo raise può essere omessa.
°°°"""
# |%%--%%| <hKqfHXfoDz|JbyPFVHNYL>

for i in range(10):
    print(i)
    raise IndentationError("Errore nel loop")

# |%%--%%| <JbyPFVHNYL|rnHLysoelv>
"""°°°
raise senza classe risolleva una except che precedentemente era stata intercettata.
°°°"""
# |%%--%%| <rnHLysoelv|AtW13U9ZzZ>

def myFunc(a,b):
    try:
        a // b
    except ZeroDivisionError:
        print("ERRORE")
        raise

# |%%--%%| <AtW13U9ZzZ|2isFnVQkCs>

myFunc(129,0)

# |%%--%%| <2isFnVQkCs|OgxYjxz2xO>
"""°°°
>> assert expression, argument
°°°"""
# |%%--%%| <OgxYjxz2xO|K5F5DJwxKR>
"""°°°
Valutiamo una espressione e se falsa verrà elevata una eccezione con in aggiunta la stringa argument.
°°°"""
# |%%--%%| <K5F5DJwxKR|SamgVE82Yr>

x = 5
assert x == 0, "valore errato"

# |%%--%%| <SamgVE82Yr|OjC7Wh61Kl>

x = 10
y = 20
try:
    if x != y:
        raise # invoco un errore forzando la except!
    else:
        print("sono uguali")

except:
       print("si è verificato un errore")


# |%%--%%| <OjC7Wh61Kl|yJn7Fcxvcg>
"""°°°
# Ereditarietà multipla
°°°"""
# |%%--%%| <yJn7Fcxvcg|aJCNucohbJ>

class BClass:
    def bFunc(self):
        print("sono in bFunc")

class CClass:
    def CFunc(self):
        print("sono in cFunc")

# |%%--%%| <aJCNucohbJ|8mI7BdRzqT>

class AClass(BClass, CClass):
    pass

a = AClass()

# |%%--%%| <8mI7BdRzqT|rbQ7nD8q65>

a.bFunc()

# |%%--%%| <rbQ7nD8q65|YYXKVkHsjj>

a.CFunc()

# |%%--%%| <YYXKVkHsjj|b8oaAEur1F>
"""°°°
```
class Persona:
    def __init__(self, fname, lname):
        self.nome = fname
        self.cognome = lname

class Indirizzo:
    def __init__(self, via, paese):
        self.via = via
        self.paese = paese

class Utente(Persona, Indirizzo):
    def __init__(self, nome, cognome, via, paese):
        Persona.__init__(self, nome, cognome)
        Indirizzo.__init__(self, via, paese)

    def scheda(self):
        return f"""
        nome: {self.nome}
        cognome: {self.cognome}
        via: {self.via}
        paese: {self.paese}"""


io = Utente("andrea", "prestini", "BICHER", "Esine")

print(io.scheda())

```
°°°"""
# |%%--%%| <b8oaAEur1F|HZxSRlL3Vt>
"""°°°
Cosa accade se entrambe le classi hanno lo stesso attributo funzione?

> $\color{red}{MRO~Method~Resolution~Order}$
°°°"""
# |%%--%%| <HZxSRlL3Vt|fQetPmkPKt>
"""°°°
L'attributo viene cercato prima nella sottoclasse stessa, poi nella prima classe presente nella gerarchia, poi la seconda, etc. come presenti nella dichiarazione della sottoclasse.
°°°"""
# |%%--%%| <fQetPmkPKt|9J5Lv6euU7>
"""°°°
In estrema ratio l'ultima classe in cui ricerca sarà Object!
°°°"""
# |%%--%%| <9J5Lv6euU7|aIgXE5P6s2>
"""°°°
# Le classi Object e Type
°°°"""
# |%%--%%| <aIgXE5P6s2|7hYaiwPkXa>
"""°°°
Sono le classi a livello più alto della gerarchia. Classi BASE!
°°°"""
# |%%--%%| <7hYaiwPkXa|KSg4ZnrP9q>

class MyClass:
    pass

# |%%--%%| <KSg4ZnrP9q|Jpr5dlbYmk>
"""°°°
MyClass è un'istanza della classe Object!

Myclass è un'istanza della classe Type
°°°"""
# |%%--%%| <Jpr5dlbYmk|jceUN4o5K3>
"""°°°
myobj è un'instanza della classe object ma NON della classe type!
°°°"""
# |%%--%%| <jceUN4o5K3|1PgEcXCPrG>

myObj = MyClass()

# |%%--%%| <1PgEcXCPrG|p5R06NybDF>

isinstance(myObj, MyClass)

# |%%--%%| <p5R06NybDF|v1kdxxzhig>

isinstance(myObj, object)

# |%%--%%| <v1kdxxzhig|cbdWqZgyF0>

isinstance(MyClass, object)

# |%%--%%| <cbdWqZgyF0|p0VlWLKsTi>

isinstance(MyClass, type)

# |%%--%%| <p0VlWLKsTi|kaOguXbvfW>

isinstance(myObj, type)

# |%%--%%| <kaOguXbvfW|ln2eRwoUAf>

isinstance(object, object)

# |%%--%%| <ln2eRwoUAf|Y1MT1IqhI5>

isinstance(type, type)

# |%%--%%| <Y1MT1IqhI5|QOm1tUh8it>

isinstance(object, type)

# |%%--%%| <QOm1tUh8it|FmUbIf0I1m>

isinstance(type, object)

# |%%--%%| <FmUbIf0I1m|MHLqSEPXdj>
"""°°°
# Il Costruttore \__new\__
°°°"""
# |%%--%%| <MHLqSEPXdj|TiMXu6Qcxp>
"""°°°
Il metodo \__init\__ inizializza un oggetto già creato in precedenza: il costruttore "effettivo" è \__new\__
°°°"""
# |%%--%%| <TiMXu6Qcxp|VkVy78YaAY>
"""°°°
In sintesi:
* init inizializza una istanza di una classe
* new costruisce l'istanza della classe
°°°"""
# |%%--%%| <VkVy78YaAY|dJj90ZHNKi>
"""°°°
Gerarchicamente Prima viene invocato il metodo new (in modo automatico) e solo successivamente viene chiamato il metodo init; questi riceve una istanza già pronta, creata appunto da new.
°°°"""
# |%%--%%| <dJj90ZHNKi|8UeeUfyrdc>
"""°°°
~~~
__new__(cls [,...])
~~~
°°°"""
# |%%--%%| <8UeeUfyrdc|Aw3id1Oc7P>
"""°°°
Gli argomenti, opzionali, saranno passati al metodo init una volta che new avrà generato l'istanza richiesta.
°°°"""
# |%%--%%| <Aw3id1Oc7P|fEmdidwah0>

class MyClass():
    def __new__(cls):
        print("istanza creata")
    def __init__(self):
        print("istanza inizializzata")

# |%%--%%| <fEmdidwah0|JDgG4w3CPQ>

mc = MyClass() # non è stato chiamato il metodo init!

# |%%--%%| <JDgG4w3CPQ|V4TI0L4yup>

class MyClass():
    def __new__(cls):
        istanza = super().__new__(cls)
        print("istanza creata")
        return istanza
    def __init__(self):
        print("istanza inizializzata")

# |%%--%%| <V4TI0L4yup|mcvVAKu4jH>

mc = MyClass()

# |%%--%%| <mcvVAKu4jH|S5DHid4IkM>
"""°°°
# Iterabili ed Iteratori (oggetti)
°°°"""
# |%%--%%| <S5DHid4IkM|z6YME5ha4K>
"""°°°
Un Container è un oggetto particolare che ammette un test particolare, il testo di appartenenza; liste, dizionari, set, tuple, string permetto di verificare se un oggetto appartiene o non appartiene a questi contenitori.
°°°"""
# |%%--%%| <z6YME5ha4K|VVGAbWiMZC>

stringa = [1,2,3,4,5]
3 in stringa

# |%%--%%| <VVGAbWiMZC|hBgYu6KcOe>
"""°°°
Un contenitore è un oggetto iterabile, MA un oggetto iterabile NON è sempre un contenitore (es. un file)
°°°"""
# |%%--%%| <hBgYu6KcOe|4wz0fT9785>
"""°°°
> Un oggetto è iterabile quando è in grado di restituire un oggetto (Iteratore) che consente di scorrere i singoli elementi dell'oggetto iterabile di partenza. Tutti gli oggetti iterabili hanno un metodo \__iter()\__
°°°"""
# |%%--%%| <4wz0fT9785|DKheOrmmJp>
"""°°°
Un Iteratore è un oggetto che produce il prossimo elemento di un iterabile, attraverso il metodo \__next()\__
°°°"""
# |%%--%%| <DKheOrmmJp|kqD75tmy9B>
"""°°°
Ricordiamo che un oggetto può essere sia iterabile che iteratore nel caso in cui contenga entrambi i metodi, \__iter()\__ ed \__next()\__ (es. una lista)
°°°"""
# |%%--%%| <kqD75tmy9B|bFyP87naPC>

myList = ["primo", "secondo", "terzo"]

# |%%--%%| <bFyP87naPC|HiiuFeOSKg>

it1 = iter(myList)

# |%%--%%| <HiiuFeOSKg|ry9yI2wZfn>

type(it1)

# |%%--%%| <ry9yI2wZfn|eiZik5E1EV>

next(it1)

# |%%--%%| <eiZik5E1EV|bEucTmwShI>

next(it1)

# |%%--%%| <bEucTmwShI|ivl7IWR3Yh>

next(it1)

# |%%--%%| <ivl7IWR3Yh|xXMZbzL5n9>

next(it1) # sono finiti gli elementi dell'oggetto iterabile

# |%%--%%| <xXMZbzL5n9|cle20MUIJ6>
"""°°°
## Creazione di un iteratore
°°°"""
# |%%--%%| <cle20MUIJ6|O8bl3Wa0Vl>

class MyIterator:
    def __iter__(self):
        self.myattr = 2
        return self

    def __next__(self):
        if self.myattr < 300:
            n = self.myattr
            self.myattr *= 2
            return n
        else:
            raise StopIteration("fine iterazione")

# |%%--%%| <O8bl3Wa0Vl|naAdjEi7fU>

miaClasse = MyIterator()
mioIter = iter(miaClasse)

# |%%--%%| <naAdjEi7fU|Pi4BgEqwMf>

print(next(mioIter))
print(next(mioIter))
print(next(mioIter))
print(next(mioIter))
print(next(mioIter))
print(next(mioIter))
print(next(mioIter))
print(next(mioIter))
print(next(mioIter))

# |%%--%%| <Pi4BgEqwMf|alCJ4Nljfc>

for i in mioIter:
    print(i)

# |%%--%%| <alCJ4Nljfc|DF0oIWa1wx>
"""°°°
## Funzione generatore (Generator Function)
°°°"""
# |%%--%%| <DF0oIWa1wx|oZeZSTt3Fr>
"""°°°
Se all'interno di una funzione compare la parola $\color{green}{yield}$ tale funzione si ferma, cede il valore al chiamante della funzione e, se richiamata, cede il valore successivo...
°°°"""
# |%%--%%| <oZeZSTt3Fr|jt2Qnm86UO>

def get_doppio_gen():
    e = 2
    while (e < 100):
        yield e
        e *= 2

# |%%--%%| <jt2Qnm86UO|Xbb6Qnk03M>

gen = get_doppio_gen()

# |%%--%%| <Xbb6Qnk03M|SPlvztm5Hv>

type(gen)

# |%%--%%| <SPlvztm5Hv|SKCUZvyryv>

print(next(gen))
print(next(gen))

# |%%--%%| <SKCUZvyryv|C9rAnPrRpy>
"""°°°
## Le Espressioni Generatore (Generator Expressions)
°°°"""
# |%%--%%| <C9rAnPrRpy|4KYPaAHm1t>
"""°°°
Di fatto è come le list comprehension:
```
numeri = [1,2,3,4,5]
n = [n * n for n in numeri if n % 2 == 1]
```
°°°"""
# |%%--%%| <4KYPaAHm1t|GkNvSHMVPF>
"""°°°
Attenzione: il generatore una volta iterato esaurisce il suo compito e NON può essere nuovamente iterato, cosa che invece si può fare con le list comprehension!
°°°"""
# |%%--%%| <GkNvSHMVPF|XmHj4VMF90>

elenco = [1,2,3,4,5]
nelenco = (n * n for n in elenco if n % 2 == 1)

# |%%--%%| <XmHj4VMF90|8KFtUzWf9j>

type(nelenco)

# |%%--%%| <8KFtUzWf9j|gyczhCiXih>

for i in nelenco:
    print(i)

# |%%--%%| <gyczhCiXih|ycpHwip11I>

for i in nelenco:
    print(i) # non otteniamo NULLA, il generatore è VUOTO!

# |%%--%%| <ycpHwip11I|zvJTybPPkm>
"""°°°
Perchè usare le Generato Expression al posto delle list comprehension?
°°°"""
# |%%--%%| <zvJTybPPkm|FDv4w9MKxv>
"""°°°
> la LC produce una lista eseguita subito e tutta in una volta sola; le GE viene eseguita in modo Lazy, un elemento alla volta durante l'iterazione dei suoi elementi!
°°°"""
# |%%--%%| <FDv4w9MKxv|TE65K6st8m>
"""°°°
Se il numero di elementi fosse alto l'utilizzo di GE rispetto a LC allocherebbe moltissima memoria in più, e, in alcuni casi, risulterebbe più veloce ed a volte l'unico strumento utilizzabile.
°°°"""
# |%%--%%| <TE65K6st8m|e3HCr9WA7z>
"""°°°
# Aggiornamento python 3.7 
°°°"""
# |%%--%%| <e3HCr9WA7z|F8sEvXlgV6>
"""°°°
## Dizionario
°°°"""
# |%%--%%| <F8sEvXlgV6|uQq2GyF7Nm>
"""°°°
Adesso garantiscono l'ordinamento delle chiavi secondo l'inserimento effettuato!
°°°"""
# |%%--%%| <uQq2GyF7Nm|igdDUJwEXM>

myDizionario = {
    "primo": 10,
    "secondo": 20,
    "terzo": 30,
}

# |%%--%%| <igdDUJwEXM|D0np8bYw7q>

myDizionario["quarto"] = 40

# |%%--%%| <D0np8bYw7q|o1g3HUFSgN>

print(dict.keys(myDizionario))

# |%%--%%| <o1g3HUFSgN|Ob8RSlMagr>
"""°°°
## Type Annotations
°°°"""
# |%%--%%| <Ob8RSlMagr|QuPmGzWOB6>
"""°°°
PEP python Enhancement Proposal (proposte di miglioramento di python).
°°°"""
# |%%--%%| <QuPmGzWOB6|tqKCKqbbdo>
"""°°°
PEP 3107 Function Annotations
°°°"""
# |%%--%%| <tqKCKqbbdo|1ATQShRGG3>
"""°°°
Introduce la possibilità di annotare i parametri ed i valori di ritorno di una funzione.
°°°"""
# |%%--%%| <1ATQShRGG3|0zm2qwMNyJ>
"""°°°
```
def foo(a: expression, b: expression = 5):
```
°°°"""
# |%%--%%| <0zm2qwMNyJ|acNHGgsvga>
"""°°°
```
def myFunc(x: "paramentro x") -> "ritorno":
    return x
```
°°°"""
# |%%--%%| <acNHGgsvga|NbBYF5kmXn>
"""°°°
PEP 484 Type Hints
°°°"""
# |%%--%%| <NbBYF5kmXn|cgZ7mCnUKG>

def myFunc(x: int, s: str = "python") -> str:
    print(x)
    return s


# |%%--%%| <cgZ7mCnUKG|2ppVnHYcRC>

print(myFunc.__annotations__)

# |%%--%%| <2ppVnHYcRC|40bONgt3qN>
"""°°°
PEP 526 del 2016 Syntax for Variable Annotations
°°°"""
# |%%--%%| <40bONgt3qN|KWrMkrTg3K>

a: int = 10
print(__annotations__)

# |%%--%%| <KWrMkrTg3K|T22gmtGt5G>

class MyClass:
    nome: str
    cognome: str

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

# |%%--%%| <T22gmtGt5G|k1CQXUGxPZ>

print(MyClass.__annotations__)

# |%%--%%| <k1CQXUGxPZ|YhtxkLziJm>
"""°°°
## Le Data Classes
°°°"""
# |%%--%%| <YhtxkLziJm|toN60amy4N>
"""°°°
Servono ad arricchire di significato le definizioni delle classi, soprattutto quando rappresentano dei DATI.
°°°"""
# |%%--%%| <toN60amy4N|f8M4SewpHf>

from dataclasses import dataclass # importiamo il decoratore

# |%%--%%| <f8M4SewpHf|322BvyM0WT>

@dataclass(init=True, repr=True, order=True, frozen=False)
class MiaClasse:
    nome: str
    cognome: str


# |%%--%%| <322BvyM0WT|yViNxDQVxy>

mc = MiaClasse("andrea", "prestini")

# |%%--%%| <yViNxDQVxy|POuEnbsZy7>

print(mc)

# |%%--%%| <POuEnbsZy7|wEYhM9f6ru>
"""°°°
## Assignment Expression (python versione 3.8) Walrus Operator
°°°"""
# |%%--%%| <wEYhM9f6ru|KWa07PAhJp>
"""°°°
Se avessimo un'espressione come questa:
```
if x = somma(5,3) > 6:
    print("x maggiore di 6")
```
otteniamo un ERRORE!
°°°"""
# |%%--%%| <KWa07PAhJp|qKqZmIrz9W>
"""°°°
MA:
```
if x:= somma(5,3) > 6:
    print("x maggiore di 6")
```
FUNZIONA!
°°°"""
# |%%--%%| <qKqZmIrz9W|VZAZIFRStB>
"""°°°
```
mylist = [1,2,3,4,5]
while x := len(mylist) != 0:
    print(x, mylist.pop())
```
°°°"""
# |%%--%%| <VZAZIFRStB|cEh3nJ9gCJ>
"""°°°
## Paremetri Positional-Only PEP 570
°°°"""
# |%%--%%| <cEh3nJ9gCJ|RrN5GMKPyU>
"""°°°
```
def somma(a, /, b, c): # a solo argomenti posizionali, b e c anche keywords
    return a + b + c
°°°"""
# |%%--%%| <RrN5GMKPyU|aptYmEuHaL>
"""°°°
# Applicazioni distribuite con RabbitMQ
°°°"""
# |%%--%%| <aptYmEuHaL|OmURjWVv7E>
"""°°°
## Architetture Client - Server
°°°"""
