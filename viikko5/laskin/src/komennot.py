class Komento:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self.arvo = 0
        Komento.edelliset_arvot = []
    def suorita(self):
        self.arvo = int(self.lue_syote())
        Komento.edelliset_arvot.append(self.sovelluslogiikka.tulos)

class Summa(Komento):
    def suorita(self):
        super().suorita()
        self.sovelluslogiikka.plus(self.arvo)

class Erotus(Komento):
    def suorita(self):
        super().suorita()
        self.sovelluslogiikka.miinus(self.arvo)

class Nollaus(Komento):
    def suorita(self):
        Komento.edelliset_arvot = []
        self.sovelluslogiikka.nollaa()

class Kumoa(Komento):
    def suorita(self):
        self.sovelluslogiikka.aseta_arvo(Komento.edelliset_arvot.pop())