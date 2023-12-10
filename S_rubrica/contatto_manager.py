#!/usr/bin/python3

from contatto import Contatto
import pickle


class ContattoManager:
    def __init__(self):
        self.nomi = {}
        self.cognomi = {}
        self.contatti = []

    def add(self, nome, cognome):
        cont = Contatto(nome, cognome)
        self.contatti.append(cont)
        self._add_index(cont)

        return cont

    def _add_index(self, cont):
        self.nomi.setdefault(cont.nome, []).append(cont)
        self.cognomi.setdefault(cont.cognome, []).append(cont)

    def find(self, nome="", cognome=""):
        if nome:
            return self.nomi.get(nome, [])

        return self.cognomi.get(cognome, [])

    def lista(self):
        return self.contatti

    def clear(self):
        self.nomi = {}
        self.cognomi = {}
        self.contatti = []

    def load(self, fname):
        self.clear()
        contatti = pickle.loads(open(fname, "rb").read())
        self.contatti = contatti
        for cont in self.contatti:
            self._add_index(cont)

    def save(self, fname):
        open(fname, "wb").write(pickle.dumps(self.contatti))

# if __name__ == '__main__':
#
#    cm = ContattoManager()
#    cm.save("contatti.txt")
#    cm.load("contatti.txt")
