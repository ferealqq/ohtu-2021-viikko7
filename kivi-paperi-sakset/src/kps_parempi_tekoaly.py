from kps_tekoaly import KPSTekoaly
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPSTekoaly):
    def __init__(self):
        super().__init__(TekoalyParannettu(10))