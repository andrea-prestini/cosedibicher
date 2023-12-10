# Lezione 03

Creare per ogni compito e ogni soluzione un file.

## Compito 1

Creare un programma che prenda in input dall'utente una serie di parole o punteggiatura (sono ammessi solo `.` `,` `!` e `?`), una per volta. L'inserzione si deve interrompere quando l'utente inserisce la stringa "stop".

Esempio di inserizioni (una ogni riga):

```python

ciao
come
stai
,
tutto
bene
?
sì 
grazie
stop
```

Finita l'inserzione si stampi la serie di frasi risultante, andando a capo dopo ogni frase (ossia dopo ogni `.`, `!` o `?`). Assicurarsi che non vi siano spazi prima della `,` e che le maiuscole siano corrette.

Riportare poi un po' di statistiche in merito al testo, ed in particolare:

- Numero di parole ricevute (non si contino i segni di interpunzione)
- Numero di segni di interpunzione
- Numero di frasi
- Il carattere più frequente
- Il carattere meno frequente

## Compito 2

Scrivere una funzione `main` che testi un insieme di funzioni:

- Una funzione `rev(list)` che prenda in input una lista e ne restituisca una nuova con i valori invertiti
- Una funzione `is_positive(n)` che controlli se un numero è positivo oppure no (restituisce `True` o `False`), si faccia uso dell'operatore di resto `%`
- Una funzione che prende come parametro una lista e ne restituisca una nuova con gli stessi valori ma priva di duplicati (si preservi l'ordine degli elementi!)
- Una funzione che controlli se una stringa è palindroma oppure no (restituisce `True` o `False`)
- Una funzione che restituisca il fattoriale di un numero intero `n` dato come argomento. Si implementi questa soluzione usando un loop (e se non potessimo usare i loop? *difficile*)

Per testare si intende (qui il test e implementazione della funzione ipotetica `somma`):

```python
def main():
    x = 1
    y = 3
    if somma(x,y) == 4: 
        print("Funzione somma ok")
    else:
        print("Funzione somma non ok")

def somma(x, y):
    return x+y
```
