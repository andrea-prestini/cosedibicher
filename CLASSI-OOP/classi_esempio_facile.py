class impiegato():
    azienda = "ALFA beta GAMMA"  # variabile di classe

    def __init__(self, nome, cognome, cittadinanza):
        self.nome = nome
        self.cognome = cognome
        self.cittadinanza = cittadinanza

    def nome_completo(self):
        return (f'''
                {impiegato.azienda}
                Elenco operatori inseriti nell'organico aziendale
                nome: {self.nome}
                cognome: {self.cognome}
                cittadinanza: {self.cittadinanza}
                {self.azienda}''')
        # altro modo per accedere alla variabile di classe!


amministratore = impiegato("andrea", "prestini", "italiana")
contabilità = impiegato("giovanna", "bianchi", "rumena")
centralino = impiegato("patrizia", "pellegrini", "albanese")
operaio = impiegato("giovanni", "ligasacchi", "inglese")
magazzino = impiegato("pietro", "maso", "italiana")


print(impiegato.nome_completo(operaio))  # versione estesa
print(operaio.nome_completo())  # versione con metodo di classe
print(centralino.nome_completo())  # versione con metodo di classe
