class Validator:

    @staticmethod
    def validate_kennzeichen(kennzeichen):
        return len(kennzeichen.strip()) > 0


    @staticmethod
    def validate_fahrzeugtyp(fahrzeugtyp):
        return fahrzeugtyp in ["Motorrad", "PKW", "Transporter"]


    @staticmethod
    def validate_parkdauer(parkdauer):
        try:
            parkdauer = float(parkdauer)
            return 0 < parkdauer <= 72
        except ValueError:
            return False


    @staticmethod
    def validate_tarif(choice, tarife):
        try:
            choice = int(choice)
            return 1 <= choice <= len(tarife)
        except ValueError:
            return False