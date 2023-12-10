import time
import os


class Casa:
    """
    class: Casa
    methods: agg_stanza, scheda_casa, composizione_casa
    """

    # composizione casa -> stanze, persone nelle stanze
    stanza_persona = dict()

    # stanze presenti nella casa
    stanze = []

    @staticmethod
    def agg_stanza():
        """
        add stanza alla casa,
        richiamata in agg Persona se la stanza non presente
        """

        while True:
            risposta = input("Quale stanza vuoi inserire? (no to escape)\n")
            if risposta != "no":
                Casa.stanze.append(risposta)
            else:
                break

    @staticmethod
    def scheda_casa():
        """
        stampa la scheda della casa che elenca le stanze,
        richiamata al bisogno per visualizzare le \
        stanze memorizzate nella casa
        """
        os.system("clear")
        print("La casa è composta dalle seguenti stanze:")
        for i, val in enumerate(Casa.stanze, 1):
            print(i, val)
            time.sleep(1)

    @staticmethod
    def composizione_casa():
        "stampa la composizione stanze-persone della casa"
        print(f"""
Nella casa ci sono {len(Casa.stanze)} stanza/e
occupate in questo modo:""")
        for k, v in Casa.stanza_persona.items():
            print(k)
            time.sleep(2)
            for i in range(len(v)):
                print(v[i])
                time.sleep(1)


class Persona:
    """
    class: Persona
    methods: scheda_persona
    """

    def __init__(self) -> None:
        self.nome = input("Nome: ")
        self.cognome = input("Cognome: ")
        self.paese = input("Paese: ")
        Casa.scheda_casa()
        indice = input("In quale stanza? ")

        if not indice.isalpha():
            indice = int(indice)

            if indice > len(Casa.stanze):
                print("Stanza non presente, prima aggiungerla alla casa...")
                Casa.agg_stanza()
            else:
                self.stanza = Casa.stanze[indice - 1]
                Casa.stanza_persona.setdefault(self.stanza, [])
                Casa.stanza_persona[self.stanza].append(
                    [self.nome,
                     self.cognome,
                     self.paese])
        else:
            print("Devi inserire un numero!")

    def scheda_persona(self):
        "scheda personale della persona"
        print(f"""
              Nome: {self.nome}
              Cognome: {self.cognome}
              Paese: {self.paese}
              """)


while True:
    actions = {
        "1": ("Aggiungi Persona", Persona),
        "2": ("Aggiungi stanza", Casa.agg_stanza),
        "3": ("Stampa scheda casa", Casa.scheda_casa),
        "4": ("Stampa composizione casa", Casa.composizione_casa),
        "5": ("EXIT", exit)
    }

    print()
    for i in sorted(actions):
        print("Scegli {} per {}".format(i, actions[i][0]))
    print("-" * 40)
    entry = input("Command: ")
    if entry in actions.keys():
        actions[entry][1]()
    else:
        print("No such command...")
