from pathlib import Path
from sys import stderr
import pickle as pkl
import csv
from pprint import pprint

DATA_DIR = Path.cwd() / 'data'

def get_results_dir():
    results_dir = Path.cwd() / 'results'
    if not results_dir.exists():
        results_dir.mkdir()
    return results_dir

# TXT

def ucitaj_iz_txt_fajla(putanja):
    try:
        with open(putanja, 'r') as fobj:
            return [line.rstrip('\n')  for line in fobj.readlines()]
    except FileNotFoundError:
        stderr.write(f"Iz ucitaj_iz_txt_fajla: fajl sa zadatom putanjom {putanja} ne postoji\n")
    except OSError as err:
        stderr.write(f"Iz ucitaj_iz_txt_fajla: greska pri ucitavanju podataka iz fajla {putanja} \n {err}\n")
    return None

def upisi_u_txt_fajl(lista, putanja):
    try:
        with open(putanja, 'w') as fobj:
            for linija in lista:
                fobj.write(f"{linija}\n")
    except OSError as err:
        stderr.write(f"Iz upisi_u_txt_fajla: greska pri upisivanju podataka u fajla {putanja} \n {err}\n")


# Binary
def deserijalizuj_podatke(putanja):
    try:
        with open(putanja, 'rb') as fobj:
            return pkl.load(fobj)
    except pkl.PickleError as err:
        stderr.write(f"Iz deserijalizuj_podatke: Pickle greska pri deserijalizaciji podataka iz {putanja} \n{err}\n")
    except OSError as err:
        stderr.write(f"Iz deserijalizuj_podatke: OS greska pri deserijalizaciji podataka iz {putanja}\n{err}\n")
    return None

def serijalizuj_podatke(podaci, putanja):
    try:
        with open(putanja, 'wb') as fobj:
            pkl.dump(podaci, fobj)
    except pkl.PicklingError as err:
        stderr.write(f"Iz serijalizuj_podatke: Pickling greska pri serijalizaciji podataka\n{err}\n")
    except OSError as err:
        stderr.write(f"Iz serijalizuj_podatke: OS greska pri serijalizaciji podataka\n{err}\n")


# CSV
def ucitaj_iz_csv_fajla(putanja):
    try:
        with open(putanja, 'r') as fobj:
            return list(csv.DictReader(fobj))
    except OSError as err:
        stderr.write(f"Iz ucitaj_iz_csv_fajla: greska pri ucitavanju iz csv fajla {putanja} \n {err}\n")
    return None

def upisi_u_csv(putanja, lista_recnika):
    try:
        with open(putanja, 'w', newline='') as fobj:
            header = tuple(lista_recnika[0].keys())
            csv_writer = csv.DictWriter(fobj, fieldnames=header)
            csv_writer.writeheader()

            for podaci in lista_recnika:
                csv_writer.writerow(podaci)
    except OSError as err:
        stderr.write(f"Greska pri upisu podataka u fajl {putanja} \n {err}\n")


def analiza_fajlova_sa_slikama(putanja):
    from collections import defaultdict
    dict_slika = defaultdict(list)

    fajlovi_sa_slikama = ucitaj_iz_txt_fajla(putanja) #cwd()/data/image_file_for_training.txt
    if not fajlovi_sa_slikama: return

    for linija_teksta in fajlovi_sa_slikama:
        f_putanja, f_naziv = linija_teksta.rsplit('/', maxsplit=1)
        _, _, kategorija = f_putanja.split('/', maxsplit=2)
        kategorija = kategorija.replace('/','_')
        dict_slika[kategorija].append(f_naziv)

    serijalizuj_podatke(dict_slika, get_results_dir() / 'zadatak1_dict.pkl')

    list_frek_slika = []
    for kategorija, lista_slika in dict_slika.items():
        list_frek_slika.append(f"{kategorija}: {len(lista_slika)}")

    upisi_u_txt_fajl(list_frek_slika, get_results_dir() / 'zadatak1_stats.txt')


def unos_podataka_o_timu():
    from operator import itemgetter

    print(""" 
    Potrebno je da unesete podatke o svakom clanu tima u sl obliku:
    ime_prezime, godine_starosti, poeni_na_takmicenju
    Za kraj unosa, unesite 'kraj'
    """)

    clanovi_tima = []
    k = 1

    while True:
        podaci = input(f"Unesite podatke o {k}. clanu tima:\n")
        if podaci.lower() == 'kraj':
            break
        try:
            ime_prezime, godine, poeni = podaci.split(',') # Marko, 19, 55.5
            clanovi_tima.append({
                'ime': ime_prezime,
                'starost': int(godine.strip()),
                'poeni': float(poeni.strip())
            })
        except ValueError as err:
            print(f"Greksa pri unosu podataka (originalna poruka: {err}). Probajte ponovo")
        else:
            k+=1


    clanovi_tima.sort(key = itemgetter('poeni'),reverse=True)
    upisi_u_csv(get_results_dir() / 'zadatak2_clanovi_tima.csv', clanovi_tima)


def zabelezi_presek_brojeva(putanja_1, putanja_2):

    l1 = ucitaj_iz_txt_fajla(putanja_1)
    l2 = ucitaj_iz_txt_fajla(putanja_2)

    if not (l1 and l2):
        raise Exception("GRESKA: Podaci iz bar jednog od zadatih fajlova se ne mogu ucitati!")

    l1 = [int(v) for v in l1 if v.isdigit()]
    l2 = [int(v) for v in l2 if v.isdigit()]

    presek_listi = [broj for broj in l1 if broj in l2]

    recnik = {
        putanja_1.name:l1,
        putanja_2.name:l2,
        'zajednicki_brojevi':presek_listi
    }

    serijalizuj_podatke(recnik, get_results_dir() / 'zadatak3_rezultati.pkl')



if __name__ == '__main__':

    pass
    # Zadatak 1
    # analiza_fajlova_sa_slikama(DATA_DIR / 'image_files_for_training.txt')

    # zad1_recnik = deserijalizuj_podatke(get_results_dir() / 'zadatak1_dict.pkl')
    # if zad1_recnik:
    #     for ent, lista_slika in zad1_recnik.items():
    #         print(f"{ent.upper()}: {', '.join(lista_slika)}")

    # zad1_lista = ucitaj_iz_txt_fajla(get_results_dir() / 'zadatak1_stats.txt')
    # if zad1_lista:
    #     for entity_stat in zad1_lista:
    #         print(entity_stat)
    # #
    #
    # # Zadatak 2
    # unos_podataka_o_timu()

    # podaci_o_timu = ucitaj_iz_csv_fajla(get_results_dir() / 'zadatak2_clanovi_tima.csv')
    # if podaci_o_timu:
    #     for podaci_o_clanu in podaci_o_timu:
    #         # pprint(podaci_o_clanu)
    #         ime, godine, poeni = podaci_o_clanu.values()
    #         print(f"{ime}, {godine} godine, {poeni} poena")
    #
    #
    # # Zadatak 3
    # f1 = DATA_DIR / 'happy_numbers.txt'
    # f2 = DATA_DIR / 'prime_numbers.txt'
    # zabelezi_presek_brojeva(f1, f2)
    #
    zad1_recnik = deserijalizuj_podatke(get_results_dir() / 'zadatak3_rezultati.pkl')
    pprint(zad1_recnik)