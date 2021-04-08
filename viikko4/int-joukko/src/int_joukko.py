class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kasvata_alkioiden_maaraa(self):
        self.alkioiden_lkm = self.alkioiden_lkm + 1

    def vahenna_alkioiden_maaraa(self):
        self.alkioiden_lkm = self.alkioiden_lkm - 1

    def kuuluu(self, numero):
        return numero in self.ljono

    def kasvata_jonoa(self):
        self.ljono.append([0] * (self.kasvatuskoko))

    def lisaa(self, numero):
        if not self.kuuluu(numero):
            self.ljono[self.alkioiden_lkm] = numero
            self.kasvata_alkioiden_maaraa()

            if self.alkioiden_lkm == len(self.ljono):
                self.kasvata_jonoa()

    def poista(self, numero):
        if self.kuuluu(numero):  
            self.ljono.remove(numero)
            self.vahenna_alkioiden_maaraa()

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        alkiot = self.ljono[:self.alkioiden_lkm]
        return alkiot

    @staticmethod
    def yhdiste(taulu_a, taulu_b):
        yhdistetyt_alkiot = taulu_a.to_int_list() + taulu_b.to_int_list()
        yhdistetyt_taulut = IntJoukko()

        for alkio in yhdistetyt_alkiot:
            yhdistetyt_taulut.lisaa(alkio)
        return yhdistetyt_taulut

    @staticmethod
    def leikkaus(taulu_a, taulu_b):
        leikatut_taulut = IntJoukko()
        alkiot_a = taulu_a.to_int_list()
        alkiot_b = taulu_b.to_int_list()
        samanlaiset_alkiot = list(set(alkiot_a).intersection(alkiot_b))

        for alkio in samanlaiset_alkiot:
            leikatut_taulut.lisaa(alkio)
        return leikatut_taulut

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
