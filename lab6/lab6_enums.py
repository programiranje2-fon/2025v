from enum import Enum
from sys import stderr

class UslugaNaLetu(Enum):

    SEDISTA = 'Izbor sedista'
    OBROK = 'Obrok'
    WIFI = 'Wifi'
    OSIGURANJE = 'Osiguranje leta'
    BRZO_UKRCAVANJE = 'Prioritetno ukrcavanje'

    @staticmethod
    def valid_service_str(value):
        return isinstance(value, str) and  any([value.lower() in [usluga.name.lower(), usluga.value.lower()] for usluga in UslugaNaLetu])

    @staticmethod
    def get_service_from_str(value):
        if not isinstance(value, str):
            stderr.write("Iz get_servic_from_str: pogresan ulazni argument, potrebno je uneti string \n")
            return None
        for usluga in UslugaNaLetu:
            if value.lower() in [usluga.name.lower(), usluga.value.lower()]:
                return usluga
        return None