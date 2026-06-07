from costumers.kunde import Kunde
from validator import Validator

class Firmenkunde(Kunde):


    def __init__(self, name, address, email, phone, password, company_id):

        super().__init__(None, name, address, email, phone, password)

        self.__company_id = None

        self.set_company_id(company_id)


    def get_company_id(self):
        return self.__company_id


    def set_company_id(self, company_id):
        if not Validator.validate_company_id(company_id):
            raise ValueError(f"Ungültiges Firmennummer-Format: '{company_id}'.")
        self.__company_id = company_id