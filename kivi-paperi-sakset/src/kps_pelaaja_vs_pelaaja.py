from KPS import KPS
from tuomari import Tuomari


class KPSPelaajaVsPelaaja(KPS):
    def _toisen_siirto(self):
        return input("Toisen pelaajan siirto: ")