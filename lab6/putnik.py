from datetime import datetime
from sys import stderr


class Putnik:

    def __init__(self, ime_prezime, drzava, pasos, cena_karte, COVID_bezbedan=False):
        self.ime = ime_prezime
        self.drzava = drzava
        self.pasos = pasos
        self.COVID_bezbedan = COVID_bezbedan
        self.cena_karte = cena_karte
        self.usluge = []

    @property
    def pasos(self):
        # if not hasattr(self, '_Putnik__pasos'):
        #     self.__pasos = None
        # return self.__pasos
        try:
            return self.__pasos
        except AttributeError:
            self.__pasos = None
            return self.__pasos

    @pasos.setter
    def pasos(self, value):
        if isinstance(value, str) and len(value) == 6 and value.isdigit():
            self.__pasos = value
            return
        if isinstance(value, int) and 100000 <= value <= 999999:
            self.__pasos = str(value)
            return

        stderr.write(f'Pogresno uneta vrednost za pasos => nije izvrsena dodela vrednosti')

    @property
    def cena_karte(self):
        try:
            return self.__cena_karte
        except AttributeError:
            self.__cena_karte = None
            return self.__cena_karte

    @cena_karte.setter
    def cena_karte(self, value):
        if not isinstance(value, (str, float, int)):
            stderr.write("Iz cena_karte.setter: pogresna vrednost ulaznog argumenta\n")
            return
        if isinstance(value, (str, float)):
            try:
                value = int(value)
            except ValueError as err:
                stderr.write(f"Iz cena_karte.setter: {err}\n")
                return
        if value > 0:
            self.__cena_karte = value

    def __str__(self):
        putnik_str = f'Putnik {self.ime}\n\t-drzavljanstvo: {self.drzava}\n\t-broj pasosa: {self.pasos}\n'
        putnik_str += f'\t-COVID bezbedan: {"DA" if self.COVID_bezbedan else "NE"} \n'
        putnik_str += f"\tCena karte: {self.cena_karte if self.cena_karte else 'karta jos nije placena'} \n"

        if len(self.usluge) == 0:
            putnik_str += "\t Nema dodatnih usluga \n"
        else:
            putnik_str += f"\tDodatne usluge: {', '.join([usluga.value for usluga in self.usluge])}"

        return putnik_str

    def __eq__(self, other):
        return isinstance(other, Putnik) and self.pasos == other.pasos and self.drzava == other.drzava

    @classmethod
    def from_string(cls, putnik_string):
        parts = [part.strip() for part in putnik_string.split(';')]
        if len(parts) == 4:
            name, country, passport, covid_status = parts
            return cls(name, country, passport, covid_status)

        stderr.write(f"Greska! Ulazni string nije odgovarajuceg formata -> Putnik objekat nije kreiran!\n")
        return None

    def azuriraj_COVID_bezbedan(self, tip_uverenja, datum_uverenja):
        if not isinstance(tip_uverenja, str) or tip_uverenja.lower() not in ['vakcinacija', 'negativan_test']:
            stderr.write(f"Pogresna vrednost za tip uverenja => promena COVID statusa ne moze biti izvrsena\n")
            return
        if not isinstance(datum_uverenja, (datetime, str)):
            stderr.write(f"Pogresan tip vrednosti za datum uverenja => promena COVID statusa ne moze biti izvrsena\n")
            return
        if isinstance(datum_uverenja, str):
            datum_uverenja = datetime.strptime(datum_uverenja, '%d/%m/%Y')

        time_delta = datetime.now() - datum_uverenja
        # if tip_uverenja == 'vakcinacija' and time_delta < 365:
        #     self.COVID_bezbedan = True
        # if tip_uverenja == 'negativan_test' and time_delta < 3:
        #     self.COVID_bezbedan = True
        self.COVID_bezbedan = ((tip_uverenja.lower() == 'vakcinacija' and time_delta.days < 365) or
                               (tip_uverenja.lower() == 'negativan_test' and time_delta.days < 3))


if __name__ == '__main__':
    bob = Putnik("Bob Smith", "UK", "123456", True)
    john = Putnik("John Smith", "USA", 987656, True)
    anna = Putnik("Anna Smith", "Spain", "987659")
    luis = Putnik.from_string("Luis Bouve; France; 123456; True")

    print("PUTNICI:\n")
    print(bob)
    print(john)
    print(anna)
    print(luis)

    print("\nPUTNICI NAKON UPDATE-a COVID STATUS-a:\n")
    anna.azuriraj_COVID_bezbedan('vakcinacija', '01/02/2024')
    print(anna)

    luis.azuriraj_COVID_bezbedan('negativan_test', '04/11/2024')
    print(luis)
    print()

    print("Provera da li su 'bob' i 'john' reference na istog putnika")
    print("Isti putnik" if bob == john else "Razliciti putnici")
    print()
    print("Provera da li su 'john' i 'johnny' reference na istog putnika")
    johnny = Putnik("Johnny Smith", "USA", 987656, False)
    print("Isti putnik" if john == johnny else "Razliciti putnici")
