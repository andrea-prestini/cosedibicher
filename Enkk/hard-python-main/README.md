# Hard Python

File e dettagli in merito al corso "Hard Python", presentato su Twitch da [Enkk](https://twitch.tv/Enkk) e [StudyTme](https://twitch.tv/StudyTme). Le lezioni sono ricaricate su [questa playlist Youtube](https://www.youtube.com/playlist?list=PLMP9hIwoX2DtrBeIDXggVbo49Uxr6ymxT).

Il corso si divide in due parti. La prima è una introduzione rapida al linguaggio Python, mentre la seconda costituisce il progetto vero e proprio e si andranno ad introdurre i primi rudimenti di NLP analizzando una grande collezione di Tweet.

In particolare si vuole analizzare titoli e descrizioni di articoli di giornale pubblicati su Twitter da parte delle maggiori testate giornalistiche italiane in un periodo di tre anni. Le testate considerate sono:

- [@fattoquotidiano](https://twitter.com/fattoquotidiano)
- [@repubblica](https://twitter.com/repubblica)
- [@ilgiornale](https://twitter.com/ilgiornale)
- [@lastampa](https://twitter.com/lastampa)
- [@corriere](https://twitter.com/corriere)
- [@open_gol](https://twitter.com/open_gol)
- [@avvenire_nei](https://twitter.com/avvenire_nei)
- [@ilmessaggeroit](https://twitter.com/ilmessaggeroit)
- [@libero_official](https://twitter.com/libero_official)

Periodo considerato: dal 1 Giugno 2019 al 1 Giugno 2022.

Ecco un esempio di Tweet:

```json
"created_at": "2022-06-18 19:25:33",
"description": "Giornata storica per l'Italia nella rassegna di Antalya. A completare il trionfo, il secondo e terzo gradino del podio per Rossella Fiamingo e Mara Navarri…",
"hashtags": [],
"id": 1538241525116567552,
"text": "Europei di scherma, tripletta maschile nel fioretto: Garozzo oro, Marini argento, Avola bronzo https://t.co/QWeIhyhVvo",
"title": "Europei di scherma, tripletta maschile nel fioretto: Garozzo oro, Marini argento, Avola bronzo",
"user": "repubblica"
```

## File di supporto

Ogni lezione è contenuta in una cartella di questo github e contiene vari file numerati, uno per ogni argomento. Inoltre c'è una cartella `compiti` che contiene la consegna e le varie soluzioni implementate da Giulia (in live, durante la settimana). I compiti vengono sempre corretti nel video della lezione successiva.

## Sulla lingua

Le lezioni sono in italiano, così come i compiti e i commenti che guidano le varie lezioni. Il codice invece è tendenzialmente in inglese dato che programmare in qualunque altra lingua è una pratica poco suggerita (il codice deve essere potenzialmente comprensibile da tutti).

## Riassunto lezioni

### Lezione #1 (26/06/2022)

- Installazione di python e pip e Visual Studio Code.
- Stampa
- Variabili
- Tipi di variabili (`int`, `float`, `string`, `boolean`)
- Operatori e operandi artimetici
- Variabili boolean e espressioni booleane
- Il costrutto `if`
- Prendere dati dall'utente: funzione `input`

### Lezione #2 (03/07/2022)

- Correzione dei compiti
- I cicli: while
- Strutture dati: le liste
- I cicli: il for
- Strutture dati: i dizionari
