from sys import stderr
from datetime import datetime

class Putnik:

    def __init__(self, ime_prezime, drzava, pasos, COVID_bezbedan=False):
        self.ime = ime_prezime
        self.drzava = drzava
        self.pasos = pasos
        self.COVID_bezbedan = COVID_bezbedan

    @property
    def pasos(self):
        if not hasattr(self, '_Putnik__pasos'):
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


    def __str__(self):
        putnik_str = f'Putnik {self.ime}\n\t-drzavljanstvo: {self.drzava}\n\t-broj pasosa: {self.pasos}\n'
        putnik_str += f'\t-COVID bezbedan: {"DA" if self.COVID_bezbedan else "NE"}'
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