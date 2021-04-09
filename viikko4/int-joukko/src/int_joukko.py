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

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.lukujono

    def kasvata_jonoa(self):
        self.lukujono.append([0] * (self.kasvatuskoko))

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.lukujono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm >= len(self.lukujono):
                self.kasvata_jonoa()

    def poista(self, luku):
        if self.kuuluu(luku):  
            self.lukujono.remove(luku)
            self.alkioiden_lkm = self.alkioiden_lkm - 1

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        luvut = self.lukujono[:self.alkioiden_lkm]
        return luvut

    @staticmethod
    def yhdiste(taulu_a, taulu_b):
        yhdistetyt_luvut = taulu_a.to_int_list() + taulu_b.to_int_list()
        yhdistetyt_taulut = IntJoukko(len(yhdistetyt_luvut))

        for luku in yhdistetyt_luvut:
            yhdistetyt_taulut.lisaa(luku)
        return yhdistetyt_taulut

    @staticmethod
    def leikkaus(taulu_a, taulu_b):
        luvut_a = taulu_a.to_int_list()
        luvut_b = taulu_b.to_int_list()
        samanlaiset_luvut = set(luvut_a).intersection(luvut_b)
        leikatut_taulut = IntJoukko(len(samanlaiset_luvut))

        for luku in samanlaiset_luvut:
            leikatut_taulut.lisaa(luku)
        return leikatut_taulut

    @staticmethod
    def erotus(taulu_a, taulu_b):
        luvut_a = taulu_a.to_int_list()
        luvut_b = taulu_b.to_int_list()
        erotetut_luvut = [alkio for alkio in luvut_a if alkio not in luvut_b ]
        erotetut_taulut = IntJoukko(len(erotetut_luvut))

        for luku in erotetut_luvut:
            erotetut_taulut.lisaa(luku)

        return erotetut_taulut

    def __str__(self):
        luvut_merkkeina = [str(luku) for luku in self.to_int_list()]
        liitetyt_merkit = ", ".join(luvut_merkkeina)
        return f"{{{liitetyt_merkit}}}"