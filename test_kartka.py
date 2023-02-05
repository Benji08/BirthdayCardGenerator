from kartka import Kartka


def test_plec_meska():
    bartosz = Kartka('Bartosz')
    assert bartosz.plec == 'male'


def test_plec_damska():
    karolina = Kartka('Karolina')
    assert karolina.plec == 'female'


def test_zyczenia_meskie():
    maks = Kartka('Maks', 1)
    assert maks.zyczenia == "Marzeń, o które warto walczyć,\n\
radości, którymi warto się dzielić,\n\
przyjaciół, z którymi warto być\n\
i nadziei, bez której nie da się żyć."


def test_zyczenia_damskie():
    julka = Kartka('Julka', 1)
    assert julka.zyczenia == "Z okazji urodzin życzę Ci,\n\
aby jedynymi łzami,\n\
które pojawią się w Twoich oczach,\n\
były kryształowe łzy szczęścia,\n\
aby radosnego uśmiechu na Twej twarzy\n\
nie zakryły ciężkie chmury smutku,\n\
aby płatki róż wyścielały\n\
drogę Twego przeznaczenia,\n\
a szczęście, zdrowie, radość i miłość\n\
były przeznaczeniem Twych dni."


def test_tlo_meskie():
    kacper = Kartka('Kacper', 1, 1)
    assert kacper.tlo.size == (800, 800)


def test_tlo_damskie():
    kamila = Kartka('Kamila', 1, 1)
    assert kamila.tlo.size == (626, 417)


def test_najdluzsza_linia():
    robert = Kartka('Robert', 1)
    linia = "i nadziei, bez której nie da się żyć."
    assert robert.najdluzsza_linia_zyczen() == linia


def test_wielkosc_zyczen():
    kacper = Kartka('Kacper', 1, 1)
    ilosc_lin = kacper.zyczenia.count('\n')+1
    x = kacper.wielkosc_zyczen().getsize(kacper.najdluzsza_linia_zyczen())[0]
    y = kacper.wielkosc_zyczen().getsize('a')[1]*ilosc_lin
    assert x < kacper.tlo.size[0] and y < kacper.tlo.size[1]


def test_miejsce_wklejenia():
    wojtek = Kartka('Wojtek', 1, 1)
    ilosc_lin = wojtek.zyczenia.count('\n')+1
    x = wojtek.wielkosc_zyczen().getsize(wojtek.najdluzsza_linia_zyczen())[0]
    szerokość = 2*wojtek.miejsce_wklejenia()[0] + x
    y = wojtek.wielkosc_zyczen().getsize('a')[1]*ilosc_lin
    dlugosc = 2*wojtek.miejsce_wklejenia()[1] + y
    assert szerokość == wojtek.tlo.size[0] or dlugosc == wojtek.tlo.size[1]
