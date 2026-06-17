from models.fahrzeug import Fahrzeug


class PKW(Fahrzeug):

    def get_faktor(self):
        return 1.0


    def get_typ(self):
        return "PKW"