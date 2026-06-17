from models.fahrzeug import Fahrzeug


class Transporter(Fahrzeug):

    def get_faktor(self):
        return 1.5


    def get_typ(self):
        return "Transporter"