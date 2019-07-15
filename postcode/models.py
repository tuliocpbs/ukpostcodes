import re

from .exceptions import InvalidPostCode


class UKPostcode:

    def __init__(self, postcode):
        self.postcode = postcode.replace(" ", "") # Cleanning postcode from spaces

        if not self.__valid_postcode():
            raise InvalidPostCode()

    def __valid_postcode(self):
        # TODO: Add British Overseas Territories validations
        regex_string = r"^([A-Za-z][A-Ha-hK-Yk-y]?[0-9][A-Za-z0-9]? ?[0-9][A-Za-z]{2}|[Gg][Ii][Rr] ?0[Aa]{2})$"
        return bool(re.match(regex_string, self.postcode))

    def __repr__(self):
        return (self.postcode[:-3] + " " + self.postcode[-3:]).upper()
    