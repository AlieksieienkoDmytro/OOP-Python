from models.fahrzeug import Fahrzeug


class Motorrad(Fahrzeug):

    def get_faktor(self):
        return 0.7


    def get_typ(self):
        return "Motorrad"