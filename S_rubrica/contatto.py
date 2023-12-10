class Contatto:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.attrs = {}

    def set_attr(self, nome_attr, valore, unique=False):
        nome_attr = nome_attr.lower().strip()

        data = self.attrs.setdefault(nome_attr, [])

        if unique:
            self.attrs[nome_attr] = [valore]
        else:
            data = self.attrs.setdefault(nome_attr, [])
            data.append(valore)
        return self.attrs[nome_attr]

    def get_attr(self, nome_attr):
        nome_attr = nome_attr.lower().strip()

        return self.attrs.get(nome_attr)

    def __str__(self):
        res = [self.nome + " " + self.cognome]

        for k, v in self.attrs.items():
            res.append("%s: %s" % (k, v))

        return "\n".join(res)


if __name__ == "__main__":
    c = Contatto("mario", "rossi")
    c.set_attr("cell.", "+39333454434")
    c.set_attr("cell.", "+3912345678")
    c.set_attr("email", "mario.rossi@libero.it")
    c.set_attr("telefono", "03355446677")
