import re # Regular expression module for pattern matching

class Validator:

    @staticmethod
    def validate_email(email):
        # Email pattern: alphanumeric and some symbols, @, domain name, and 2+ letter extension
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}+$"
        return bool(re.match(pattern, email))


    @staticmethod
    def validate_phone(phone):
        # Allows an optional '+' at the start, followed by digits. Total length must be 8 to 20 characters
        pattern = r"^\+[0-9]{8,20}$"
        return bool(re.match(pattern, phone))


    @staticmethod
    def validate_name(name):
        # Allows letters, digits, spaces, hyphens, and periods. Length must be between 1 and 100 characters
        pattern = r"^[a-zA-Z0-9\s\-\.]+$"
        return bool(re.match(pattern, name))


    @staticmethod
    def validate_address(address):
        # Allows letters, digits, spaces, periods, commas, slashes, and hyphens
        pattern = r"^[A-Za-z0-9äöüÄÖÜß\s.,-]+$"
        return bool(re.match(pattern, address))


    @staticmethod
    def validate_birthdate(date):
        # Strict format validation: YYYY-MM-DD (4 digits, 2 digits, 2 digits)
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        return bool(re.match(pattern, date))


    @staticmethod
    def validate_company_id(company_id):
        # Allows letters, digits, and hyphens, with a length between 3 and 20 characters
        pattern = r"^[A-Za-z0-9-]{3,20}$"
        return bool(re.match(pattern, company_id))


    @staticmethod
    def validate_price(price):
        # Only digits allowed, with an optional decimal point and digits after
        pattern = r"^\d+(\.\d+)?$"
        if re.match(pattern, str(price)):
            return float(price) > 0
        return False


    @staticmethod
    def validate_weight(weight):
        # Weight must be a positive number greater than 0 (integers or decimals)
        pattern = r"^(?!(?:0|0\.0+)$)\d+(?:\.\d+)?$"
        return bool(re.match(pattern, str(weight)))


    @staticmethod
    def validate_author(author):
        # Allows letters, spaces, periods, apostrophes, and hyphens
        pattern = r"^[a-zA-Z\s.'-]+$"
        return bool(re.match(pattern, author)) if author else False


    @staticmethod
    def validate_pages(pages):
        # Only digits allowed, and must be a positive integer greater than 0
        pattern = r"^[0-9]+$"
        if re.match(pattern, str(pages)):
            return int(pages) > 0
        return False


    @staticmethod
    def validate_brand(brand):
        # Allows letters and spaces
        pattern = r"^[a-zA-Z\s]+$"
        return bool(re.match(pattern, brand)) if brand else False


    @staticmethod
    def validate_warranty(warranty_years):
        # Only digits allowed, and must be a non-negative integer (0 or greater)
        pattern = r"^[0-9]+$"
        if re.match(pattern, str(warranty_years)):
            return int(warranty_years) >= 0
        return False


    @staticmethod
    def validate_size(size):
        # Allows letters, digits, spaces, and hyphens
        pattern = r"^[a-zA-Z0-9\s-]+$"
        return bool(re.match(pattern, size)) if size else False


    @staticmethod
    def validate_color(color):
        # Only letters allowed
        pattern = r"^[a-zA-Z\s-]+$"
        return bool(re.match(pattern, color)) if color else False


    @staticmethod
    def validate_digits(digits):
        # Digits
        pattern = r"^\d+$"
        return bool(re.match(pattern, digits)) if digits else False