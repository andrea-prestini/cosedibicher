import time
import socket
import sqlite3
from contextlib import contextmanager

@contextmanager
def filestream(path, mode):
    f = open(path, mode)
    print(f'Apro il file {path}')
    time.sleep(2)
    yield f
    print(f"chiudo il file: {path}")
    time.sleep(2)
    f.close()
    print("fine procedura")
    print("il file è chiuso:", f.closed)
    
  

with filestream("file.txt", "w") as file:
    print("Scrivo sul file...")
    time.sleep(1)
    file.write("Another file text...")


@contextmanager
def db_connection(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    print("Apro la connessione con il database...")
    yield cursor
    conn.commit()
    print("Chiudo la connessione con il database...")
    conn.close()

with db_connection("mydb.db") as c:
    c.execute("CREATE TABLE IF NOT EXISTS person("
           "name VARCHAR(255),"
            "age INT);")
