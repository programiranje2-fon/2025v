from putnik import Putnik
from datetime import datetime
from sys import stderr

class Let:

    poletanje_dt_format = '%Y-%m-%d %H:%M'

    def __init__(self, let, poletanje):
        self.broj_leta = let
        self.vreme_poletanja = poletanje
        self.putnici = []


    @property
    def vreme_poletanja(self):
        if not hasattr(self, '_Let__vreme_poletanja'):
            self.__vreme_poletanja = None
        return self.__vreme_poletanja


    @vreme_poletanja.setter
    def vreme_poletanja(self, value):
        if isinstance(value, str):
            value = datetime.strptime(value, Let.poletanje_dt_format)
        if isinstance(value, datetime) and value > datetime.now():
            self.__vreme_poletanja = value
        else:
            stderr.write(f"Greska! Nepoznat format za datum i vreme poletanja -> vrednost nije dodeljenja!\n")


    def dodaj_putnika(self, p):
        if not isinstance(p, Putnik):
            stderr.write(f"Greska! Pogresan tip ulaznog argumenta, ocekivan objekat klase Putnik, "
                         f"primljen objekat klase {type(p)}\n")
            return
        if p in self.putnici:
            stderr.write(f"Putnik {p.ime} ({p.pasos}) je vec u listi putnika\n")
            return
        if not p.COVID_bezbedan:
            stderr.write(f"Putnik {p.ime} ({p.pasos}) nema potvrdu da je COVID bezbedan\n")
            return

        self.putnici.append(p)


    def vreme_poletanja_str(self):
        return datetime.strftime(self.vreme_poletanja, Let.poletanje_dt_format) if self.vreme_poletanja else 'nepoznato'


    def __str__(self):
        let_str = f"Let {self.broj_leta}\n"
        let_str += f"Datum i vreme poletanja: {self.vreme_poletanja_str()}\n"
        if len(self.putnici) > 0:
            let_str += "Putnici na letu:\n" + '\n'.join([str(p) for p in self.putnici])
        else:
            let_str += "Let jos nema prijavljenih putnika"
        return let_str


    def vreme_do_poletanja(self):
        if self.vreme_poletanja:
            dt = self.vreme_poletanja - datetime.now()
            days = dt.days
            hours, sec_remained = divmod(dt.seconds, 3600)
            mins = sec_remained // 60
            return days, hours, mins

        stderr.write("Greska! Vreme poletanja nije poznato!\n")
        return None


    def __iter__(self):
        self.__next_index = 0
        return self


    def __next__(self):
        if self.__next_index == len(self.putnici):
            raise StopIteration

        next = self.putnici[self.__next_index]
        self.__next_index += 1
        return next



if __name__ == '__main__':

    lh1411 = Let('LF1411', '2024-12-10 6:50')
    lh992 = Let('LH992', '2024-11-25 12:20')

    print("\nLETOVI:\n")
    print(lh1411)
    print()
    print(lh992)
    print()

    bob = Putnik("Bob Smith", "UK", "123456", True)
    john = Putnik("John Smith", "USA", 987656, True)
    anna = Putnik("Anna Smith", "Spain", "987659")
    luis = Putnik.from_string("Luis Bouve; France; 123456; True")

    print(f"\nDodavanje putnika na let {lh1411.broj_leta}")
    for p in [bob, john, anna, luis]:
        lh1411.dodaj_putnika(p)

    print(f"\nPokusaj dodavanja putnika koji je vec u listi putnika za let {lh1411.broj_leta}:")
    lh1411.dodaj_putnika(Putnik("J Smith", "USA", "987656", True))
    print()

    print(f"\nPodaci o letu {lh1411.broj_leta} nakon dodavanja putnika na let:\n")
    print(lh1411)

    print()

    do_poletanja = lh1411.vreme_do_poletanja()
    if do_poletanja:
        dani, sati, mins = do_poletanja
        print(f"Vreme preostalo do poletanja leta {lh1411.broj_leta}: "
              f"{dani} dana, {sati} sati, i {mins} minuta")

    print()

    # print("\nPUTNICI NA LETU LH1411 (iter / next):")
    # p_iter = iter(lh1411)
    # try:
    #     while True:
    #         print(next(p_iter))
    # except StopIteration:
    #     print("Svi putnici su izlistani")

    # print()
    print("\nPUTNICI NA LETU LH1411 (FOR petlja):")
    for p in iter(lh1411):
        print(p)

