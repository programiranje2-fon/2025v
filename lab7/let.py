from datetime import datetime
from sys import stderr

from lab6.kategorije_putnika import PutnikEkonomskeKlase, PutnikBiznisKlase
from lab6.lab6_enums import UslugaNaLetu
from lab6.putnik import Putnik


class Let:
    poletanje_dt_format = '%Y-%m-%d %H:%M'

    def __init__(self, let, poletanje, ruta):
        self.broj_leta = let
        self.vreme_poletanja = poletanje
        self.putnici = list()
        self.ruta = ruta

    @classmethod
    def from_dict(cls, d):

        def key_val(kljuc):
            return d[kljuc] if kljuc in d.keys() else None

        try:
            return cls(d['br_leta'], d['vreme_poletanja'], (d['polazna_lokacija'], d['odrediste']))
        except KeyError:
            potrebni_kljucevi = ['br_leta', 'vreme_poletanja', 'polazna_lokacija', 'odrediste']
            validni_kljucevi = [kljuc for kljuc in d.keys if kljuc in potrebni_kljucevi]
            print("Nisu raspolozivi svi podaci o letu -> Let objekat ce biti kreiran na osnovu sledecih podataka: ")
            print(", ".join(validni_kljucevi))
            return cls(key_val('br_leta'), key_val('vreme_poletanja'),
                       (key_val('polazna_lokacija'), key_val('odrediste')))

    def generator_putnika_sa_uslugama(self):
        from collections import defaultdict
        usluge_dict = defaultdict(int)

        for putnik in self.putnici:
            if len(putnik.usluge) > 0:
                for usluga in putnik.usluge:
                    usluge_dict[usluga] += 1
                yield putnik

        print(f"\n Putnici na letu {self.broj_leta} su narucili sldece usluge: ")
        print("; ".join([f"{usluga.value} : {broj}" for usluga, broj in usluge_dict.items()]))

    def generator_kandidata_za_biznis_klasu(self, min_cena_karte):
        kandidati = [putnik for putnik in self.putnici if
                     isinstance(putnik, PutnikEkonomskeKlase) and len(putnik.usluge) > 0 and
                     putnik.cena_karte > min_cena_karte]

        for kandidat in sorted(kandidati, reverse=True, key=lambda k: k.cena_karte):
            yield kandidat


    @property
    def ruta(self):
        try:
            return self.__ruta
        except AttributeError:
            self.__ruta = None
            return self.__ruta

    # (“Beograd, Rim”), crticom (“Beograd - Rim”) ili znakom '>' (“Beograd > Rim”). #false false false ... true false false false  ...
    @ruta.setter
    def ruta(self, value):
        if isinstance(value, (list, tuple)) and len(value) == 2:
            self.__ruta = tuple(value)
            return
        if isinstance(value, str) and sum([ch in ',->' for ch in value]) == 1:
            import re
            value_split = re.split('[,->]', value)
            polazak, destinacija = value_split
            self.__ruta = polazak.strip(), destinacija.strip()
            return
        stderr.write("Iz ruta.setter: ruta leta je zadata u neodgovarajucem obliku\n")

    @property
    def vreme_poletanja(self):
        # if not hasattr(self, '_Let__vreme_poletanja'):
        #     self.__vreme_poletanja = None
        # return self.__vreme_poletanja
        try:
            return self.__vreme_poletanja
        except AttributeError:
            self.__vreme_poletanja = None
            return self.__vreme_poletanja

    @vreme_poletanja.setter
    def vreme_poletanja(self, value):
        if not isinstance(value, (datetime, str)):
            stderr.write(
                f"Iz vreme_poletanja.setter: Ocekivani ulazni argument nije tipa datetime ili str; umesto toga primljena vrednost je tipa {type(value)}\n")
            return
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, Let.poletanje_dt_format)
            except ValueError:
                stderr.write(
                    f"Iz vreme_poletanja.setter: String zapis vremena poletanja ne odgovara ocekivanom formatu {Let.poletanje_dt_format}\n")
                return
        if value > datetime.now():
            self.__vreme_poletanja = value
        else:
            stderr.write("Iz vreme_poletanja.setter: vreme poletanja se mora odnositi na neki trenutak u buducnosti\n")

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
        let_str += f"Ruta leta: {self.ruta_str()}\n"
        if len(self.putnici) > 0:
            let_str += "Putnici na letu:\n" + '\n'.join([str(p) for p in self.putnici])
        else:
            let_str += "Let jos nema prijavljenih putnika"
        return let_str

    def ruta_str(self):
        if not self.ruta:
            return "nepoznata"
        polazna_lok, odredisna_lok = self.ruta
        return f"{polazna_lok} -> {odredisna_lok}"

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
    pass

    lh1411 = Let('LH1411', '2026-06-20 6:50', ('Belgrade', 'Munich'))
    print(lh1411)
    print()

    lh992 = Let('LH992', '2026-06-26 12:20', 'Belgrade > Frankfurt')
    print(lh992)
    print()

    lh1514_dict = {'br_leta': 'lh1514',
                   'vreme_poletanja': '2026-6-21 16:30',
                   'polazna_lokacija': 'Paris',
                   'odrediste': 'Berlin'}

    lh1514 = Let.from_dict(lh1514_dict)
    print(lh1514)
    print()

    bob = PutnikEkonomskeKlase("Bob Smith", "UK", "123456", 250.0, True)
    john = PutnikEkonomskeKlase("John Smith", "USA", 987656, 450, True)
    luis = PutnikBiznisKlase(ime_prezime="Luis Bouve", drzava='France', pasos="123654", cena_karte=225,
                             usluge=[UslugaNaLetu.OBROK, UslugaNaLetu.WIFI], COVID_bezbedan=True)

    anna = PutnikEkonomskeKlase("Anna Smith", "Spain", "987659", 375, True)
    try:
        dodatne_usluge = {UslugaNaLetu.OBROK: 10, UslugaNaLetu.WIFI: 15}
        anna.dodaj_izabrane_usluge(dodatne_usluge)
    except ValueError as err:
        stderr.write(f"Iz dodaj_izabrane_usluge: Greska! {err}")

    print(f"\nDodavanje putnika na let {lh1411.broj_leta}")
    for p in [bob, john, anna, luis]:
        lh1411.dodaj_putnika(p)

    print(f"\nPodaci o letu {lh1411.broj_leta} nakon dodavanja putnika na let:\n")
    print(lh1411)

    print("\nPutnici sa dodatnim uslugama na letu:")
    # Jedan od nacina poziva generatora
    g = lh1411.generator_putnika_sa_uslugama()

    while True:
        try:
            print(next(g))
        except StopIteration:
            print("------- kraj spiska putnika sa dodatnim uslugama --------")
            break
    print()

    # Drugi nacin poziva generatora (tipicno koriscen)
    # for putnik in lh1411.generator_putnika_sa_uslugama():
    #     print(putnik)

    # Dodacemo putnicima usluge na letu radi provere generatorske metode
    try:
        dodatne_usluge_bob = {UslugaNaLetu.SEDISTA: 20, UslugaNaLetu.OSIGURANJE: 35}
        bob.dodaj_izabrane_usluge(dodatne_usluge_bob)
    except ValueError as err:
        stderr.write(f"Iz dodaj_izabrane_usluge: Greska! {err}")

    try:
        dodatne_usluge_john = {UslugaNaLetu.OBROK: 20, UslugaNaLetu.WIFI: 35}
        john.dodaj_izabrane_usluge(dodatne_usluge_john)
    except ValueError as err:
        stderr.write(f"Iz dodaj_izabrane_usluge: Greska! {err}")

    print("\nKandidati za prelazak u biznis klasu:")
    # Jedan od nacina poziva generatora
    g = lh1411.generator_kandidata_za_biznis_klasu(350)
    try:
        while True:
            print(next(g))
    except StopIteration:
        print("--- kraj liste kandidata ---")

    # Drugi nacin poziva generatora (tipicno koriscen)
    # print("\nPutnici kojima je ponudjena mogucnost prelaska u biznis klasu:")
    # for ind, putnik in enumerate(lh1411.generator_kandidata_za_biznis_klasu(350)):
    #     print(f"{ind+1}. {putnik}")
