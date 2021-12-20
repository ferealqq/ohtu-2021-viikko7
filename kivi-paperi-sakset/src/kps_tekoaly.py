from KPS import KPS
from tuomari import Tuomari
from tekoaly import Tekoaly


class KPSTekoaly(KPS):
    def __init__(self, tekoaly = Tekoaly()):
        self.tekoaly = tekoaly

    def _toisen_siirto(self):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto

    def _aseta_siirto(self, siirto):
        self.tekoaly.aseta_siirto(siirto)