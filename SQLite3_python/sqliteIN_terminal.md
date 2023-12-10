# SQL comandi nel terminale LINUX

Link: [Sito Ufficiale - sqlite](https://www.sqlite.org/cli.html)

## Collegamento al database

```bash
sqlite3 miodatabase.db 
```

## Pulizia terminale in SQL

```sql
.shell clear
```

## Uscita dal terminale SQL

```sql
.quit
```

per collegarmi al database.

Se già nella console **sqlite3** possiamo utilizzare il comando

```.open```. Ricordiamo che tutti i comandi devono essere terminati con il punto e virgola.

## Creazione della Tabella

Codice SQL con sintazzi standard:

```sql
CREATE TABLE persone(nome text NOT NULL, cognome text, eta REAL);
```

## Ricerca valori nella tabella

```sql
SELECT * FROM persone WHERE nome IS "andrea";
```

```sql
SELECT * FROM persone WHERE nome LIKE "andrea"
```

```sql
SELECT * FROM persone WHERE nome LIKE "andrea%"
```

Il percento sostituisce la wildcard * nel linguaggio comune!

```sql
SELECT * FROM persone WHERE nome LIKE "%andrea"
```

Il percento sostituisce la wildcard * nel linguaggio comune!

```sql
SELECT * FROM persone WHERE nome LIKE "%andrea%"
```

Il percento sostituisce la wildcard * nel linguaggio comune!

## Delete a ROW

```sql
DELETE FROM persone WHERE rowid=2;
```

## ALTER Table

```sql
ALTER TABLE persone ADD COLUMN valore REAL
UPDATE persone SET valore=1000 WHERE fname IS "andrea"
```

Caso di modifica TUTTI i records:
```sql
UPDATE persone SET valore=100;
```

Modifica il campo valore di TUTTI i record a 100.

## Alcuni comandi utili

- .dbinfo
- .databases
- .open
- .output miofile
- .save (salva su file il database in memoria)
- .show
- .header on
- .mode column (migliore rappresentazione grafica in colonne)
- .schema
- .archive ...             Manage SQL archives
- .auth ON|OFF             Show authorizer callbacks
- .archive ...             Manage SQL archives
- .auth ON|OFF             Show authorizer callbacks
- .backup ?DB? FILE        Backup DB (default "main") to FILE
- .bail on|off             Stop after hitting an error.  Default OFF
- .binary on|off           Turn binary output on or off.  Default OFF
- .cd DIRECTORY            Change the working directory to DIRECTORY
- .changes on|off          Show number of rows changed by SQL
- .check GLOB              Fail if output since .testcase does not match
- .clone NEWDB             Clone data into NEWDB from the existing database
- .connection [close] [#]  Open or close an auxiliary database connection
- .databases               List names and files of attached databases
- .dbconfig ?op? ?val?     List or change sqlite3_db_config() options
- .backup ?DB? FILE        Backup DB (default "main") to FILE
- .bail on|off             Stop after hitting an error.  Default OFF
- .binary on|off           Turn binary output on or off.  Default OFF
- .cd DIRECTORY            Change the working directory to DIRECTORY
- .changes on|off          Show number of rows changed by SQL
- .check GLOB              Fail if output since .testcase does not match
- .clone NEWDB             Clone data into NEWDB from the existing database
- .connection [close] [#]  Open or close an auxiliary database connection
- .databases               List names and files of attached databases
- .dbconfig ?op? ?val?     List or change sqlite3_db_config() options
- .dbinfo ?DB?             Show status information about the database
- .dump ?OBJECTS?          Render database content as SQL
- .echo on|off             Turn command echo on or off
- .eqp on|off|full|...     Enable or disable automatic EXPLAIN QUERY PLAN
- .excel                   Display the output of next command in spreadsheet
- .exit ?CODE?             Exit this program with return-code CODE
- .expert                  EXPERIMENTAL. Suggest indexes for queries
- .explain ?on|off|auto?   Change the EXPLAIN formatting mode.  Default: auto
- .filectrl CMD ...        Run various sqlite3_file_control() operations
- .fullschema ?--indent?   Show schema and the content of sqlite_stat tables
- .headers on|off          Turn display of headers on or off
- .help ?-all? ?PATTERN?   Show help text for PATTERN
- .import FILE TABLE       Import data from FILE into TABLE
- .imposter INDEX TABLE    Create imposter table TABLE on index INDEX
- .indexes ?TABLE?         Show names of indexes
- .limit ?LIMIT? ?VAL?     Display or change the value of an SQLITE_LIMIT
- .lint OPTIONS            Report potential schema issues.
- .load FILE ?ENTRY?       Load an extension library
- .log FILE|off            Turn logging on or off.  FILE can be stderr/stdout
- .mode MODE ?OPTIONS?     Set output mode
- .nonce STRING            Suspend safe mode for one command if nonce matches
- .nullvalue STRING        Use STRING in place of NULL values
- .once ?OPTIONS? ?FILE?   Output for the next SQL command only to FILE
- .open ?OPTIONS? ?FILE?   Close existing database and reopen FILE
- .output ?FILE?           Send output to FILE or stdout if FILE is omitted
- .parameter CMD ...       Manage SQL parameter bindings
- .print STRING...         Print literal STRING
- .progress N              Invoke progress handler after every N opcodes
- .prompt MAIN CONTINUE    Replace the standard prompts
- .quit                    Exit this program
- -.read FILE               Read input from FILE or command output
- .recover                 Recover as much data as possible from corrupt db.
- .restore ?DB? FILE       Restore content of DB (default "main") from FILE
- .save ?OPTIONS? FILE     Write database to FILE (an alias for .backup ...)
- .scanstats on|off        Turn sqlite3_stmt_scanstatus() metrics on or off
- .schema ?PATTERN?        Show the CREATE statements matching PATTERN
- .selftest ?OPTIONS?      Run tests defined in the SELFTEST table
- .separator COL ?ROW?     Change the column and row separators
- .sha3sum ...             Compute a SHA3 hash of database content
- .shell CMD ARGS...       Run CMD ARGS... in a system shell
- .show                    Show the current values for various settings
- .stats ?ARG?             Show stats or turn stats on or off
- .system CMD ARGS...      Run CMD ARGS... in a system shell
- .tables ?TABLE?          List names of tables matching LIKE pattern TABLE
- .testcase NAME           Begin redirecting output to 'testcase-out.txt'
- .testctrl CMD ...        Run various sqlite3_test_control() operations
- .timeout MS              Try opening locked tables for MS milliseconds
- .timer on|off            Turn SQL timer on or off
- .trace ?OPTIONS?         Output each SQL statement as it is run
- .vfsinfo ?AUX?           Information about the top-level VFS
- .vfslist                 List all available VFSes
- .vfsname ?AUX?           Print the name of the VFS stack
- .width NUM1 NUM2 ...     Set minimum column widths for columnar output


## Alcuni JOIN

```sql
SELECT nome, cognome, paese FROM persone INNNER JOIN paesi ON persone.id = paesi.id ORDER BY age ASC
```

Chiave di collegamento id in persone ed id in paesi.

## Eliminare tabella o record

```sql
DROP TABLE persone
```

```sql
DELETE FROM people WHERE name="simone"
```