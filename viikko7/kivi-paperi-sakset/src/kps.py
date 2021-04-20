from tuomari import Tuomari


class KPS:    
    def pelaa(self):
        tuomari = Tuomari()
        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            if self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
                tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
                print(tuomari)
                print('---')
            else:
                print("Kiitos!")
                print(tuomari)
                break

    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ekan_siirto):
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    @staticmethod
    def luo(input):
        from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
        from kps_tekoaly import KPSTekoaly
        from kps_parempi_tekoaly import KPSParempiTekoaly

        pelimoodit = {
            "a": KPSPelaajaVsPelaaja,
            "b": KPSTekoaly,
            "c": KPSParempiTekoaly
        }
        return pelimoodit[input]()
        
