import re # Regular expression module for pattern matching

class Validator:

    def validate_email(email):
        # Email pattern: alphanumeric and some symbols, @, domain name, and 2+ letter extension
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}+$"
        return bool(re.match(pattern, email))


    def validate_phone(phone):
        # Allows an optional '+' at the start, followed by digits. Total length must be 8 to 20 characters
        pattern = r"^\+[0-9]{8,20}$"
        return bool(re.match(pattern, phone))


    def validate_name(name):
        # Allows letters, spaces, and hyphens
        pattern = r"^[a-zA-Z\s-]+$"
        return bool(re.match(pattern, name))


    def validate_address(address):
        # Allows letters, digits, spaces, periods, commas, slashes, and hyphens
        pattern = r"^[A-Za-z0-9äöüÄÖÜß\s.,-]+$"
        return bool(re.match(pattern, address))


    def validate_birthdate(date):
        # Strict format validation: YYYY-MM-DD (4 digits, 2 digits, 2 digits)
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        return bool(re.match(pattern, date))


    def validate_company_id(company_id):
        # Only digits allowed, with a strict length constraint of 5 to 15 characters
        pattern = r"^[0-9]{5,15}+$"
        return bool(re.match(pattern, company_id))



    validate_email = staticmethod(validate_email)
    validate_phone = staticmethod(validate_phone)
    validate_name = staticmethod(validate_name)
    validate_address = staticmethod(validate_address)
    validate_birthdate = staticmethod(validate_birthdate)
    validate_company_id = staticmethod(validate_company_id)