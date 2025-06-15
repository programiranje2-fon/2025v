
if __name__ == '__main__':

    pass

    # lh1411 = Let('LF1411', '2024-12-10 6:50')
    # lh992 = Let('LH992', '2024-11-25 12:20')
    #
    # print("\nLETOVI:\n")
    # print(lh1411)
    # print()
    # print(lh992)
    # print()
    #
    # bob = Putnik("Bob Smith", "UK", "123456", True)
    # john = Putnik("John Smith", "USA", 987656, True)
    # anna = Putnik("Anna Smith", "Spain", "987659")
    # luis = Putnik.from_string("Luis Bouve; France; 123456; True")
    #
    # print(f"\nDodavanje putnika na let {lh1411.broj_leta}")
    # for p in [bob, john, anna, luis]:
    #     lh1411.dodaj_putnika(p)
    #
    # print(f"\nPokusaj dodavanja putnika koji je vec u listi putnika za let {lh1411.broj_leta}:")
    # lh1411.dodaj_putnika(Putnik("J Smith", "USA", "987656", True))
    # print()
    #
    # print(f"\nPodaci o letu {lh1411.broj_leta} nakon dodavanja putnika na let:\n")
    # print(lh1411)
    #
    # print()
    #
    # do_poletanja = lh1411.vreme_do_poletanja()
    # if do_poletanja:
    #     dani, sati, mins = do_poletanja
    #     print(f"Vreme preostalo do poletanja leta {lh1411.broj_leta}: "
    #           f"{dani} dana, {sati} sati, i {mins} minuta")
    #
    # print()
    #
    # print("\nPUTNICI NA LETU LH1411 (iter / next):")
    # p_iter = iter(lh1411)
    # try:
    #     while True:
    #         print(next(p_iter))
    # except StopIteration:
    #     print("Svi putnici su izlistani")
    #
    # print()
    # print("\nPUTNICI NA LETU LH1411 (FOR petlja):")
    # for p in iter(lh1411):
    #     print(p)


