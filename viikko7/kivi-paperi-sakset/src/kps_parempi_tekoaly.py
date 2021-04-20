from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps import KPS

class KPSParempiTekoaly(KPS):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)
    
    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(ekan_siirto)
        return tokan_siirto

