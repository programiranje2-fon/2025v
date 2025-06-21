from lab6.lab6_enums import UslugaNaLetu
from lab6.putnik import Putnik
from sys import stderr


class PutnikEkonomskeKlase(Putnik):

    # {"WIFI":30, "OBROK":50}
# usluge_dict = {
#     UslugaNaLetu.OBROK: 10,
#     UslugaNaLetu.WIFI: 5,
#     UslugaNaLetu.BRZO_UKRCAVANJE: 7
# }
    def dodaj_izabrane_usluge(self, usluge_dict):
        if not self.cena_karte:
            raise ValueError("Putnik jos nije platio osnovnu cenu karte!\n")

        nove_usluge = []
        tot_cena_usluga = 0

        for usluga, cena in usluge_dict.items():
            nove_usluge.append(usluga)
            tot_cena_usluga += cena

        print(f"Putnik {self.ime} je uplatio sledece dodatne usluge: {', '.join([u.value for u in nove_usluge])}")
        print(f"Ukupna cena ovih usluga je {tot_cena_usluga} ")

        self.usluge.extend(nove_usluge)
        self.cena_karte += tot_cena_usluga


    def __str__(self):
        return "Putnik ekonomske klase: \n " + super().__str__()



class PutnikBiznisKlase(Putnik):

    def __init__(self, usluge = (UslugaNaLetu.BRZO_UKRCAVANJE,), **kwargs):
        super().__init__(**kwargs)

        for usluga in usluge:
            if isinstance(usluga, str) and UslugaNaLetu.valid_service_str(usluga):
                self.usluge.append(UslugaNaLetu.get_service_from_str(usluga))
            elif type(usluga) is UslugaNaLetu:
                self.usluge.append(usluga)


    def __str__(self):
        return "Putnik biznis klase: \n" + super().__str__()




if __name__ == '__main__':

    # pass
    jim = PutnikEkonomskeKlase("Jim Jonas", 'UK', '123456', 450, True)
    print(jim)
    print()
    #
    # Add extra services to Jim
    extra_services = {
        UslugaNaLetu.OBROK: 10,
        UslugaNaLetu.WIFI: 15
    }
    try:
        jim.dodaj_izabrane_usluge(extra_services)
    except ValueError as err:
        stderr.write(f"Iz dodaj_izabrane_usluge: Greska! {err}")
    print()
    print(jim)
    #
    bob = PutnikEkonomskeKlase("Bob Jones", 'Denmark', '987654', 420)
    print(bob)
    print()
    #
    mike = PutnikBiznisKlase(ime_prezime="Mike Stone", drzava="USA",
                             pasos='234567', cena_karte=550, COVID_bezbedan=True, usluge=(UslugaNaLetu.BRZO_UKRCAVANJE, UslugaNaLetu.WIFI))
    print(mike)
    print()
    #
    brian = PutnikBiznisKlase(ime_prezime="Brian Brown", drzava="UK",
                              pasos='546234', cena_karte=670, COVID_bezbedan=True,
                              usluge=("Osiguranje leta", "Uzina", "Izbor sedista"))
    print(brian)
    #
    #
