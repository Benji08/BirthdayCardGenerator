import requests
from random import randint
from PIL import Image, ImageFont, ImageDraw


url = 'https://api.genderize.io?name={imie}'
sciezka_do_zyczen = 'zyczenia.txt'
sciezka_meska = 'tla/tlo_meskie{numer}.jpg'
sciezka_damska = 'tla/tlo_damskie{numer}.jpg'
sciezka_font = 'Pushster-Regular.ttf'
przykladowa_sciezka = 'tla/kartka.jpg'


class Kartka():

    def __init__(self, imie, los1=randint(1, 3), los2=randint(1, 3)):
        if imie == '':
            raise ValueError('należy podać imie')
        else:
            self.imie = imie
        if los1 < 0 or los1 > 3:
            raise ValueError("Nie poprawna wartość los1")
        else:
            self.los1 = los1 - 1
        if los2 < 0 or los2 > 3:
            raise ValueError("Nie poprawna wartość los1")
        else:
            self.los2 = los2
        slownik = requests.get(url.format(imie=self.imie)).json()
        if slownik['gender'] is None:
            raise ValueError("Nierprawidłowe imie")
        else:
            self.plec = slownik['gender']

        with open(sciezka_do_zyczen, 'r') as znacznik:
            zyczenia = znacznik.read()
            zyczenia_meskie, zyczenia_damskie = zyczenia.split('>')
            if self.plec == 'male':
                self.zyczenia = zyczenia_meskie.split(';')[self.los1][:-1]
            elif self.plec == 'female':
                self.zyczenia = zyczenia_damskie.split(';')[self.los1][:-1]

        if self.plec == 'male':
            self.tlo = Image.open(sciezka_meska.format(numer=self.los2))
        elif self.plec == 'female':
            self.tlo = Image.open(sciezka_damska.format(numer=self.los2))

    def najdluzsza_linia_zyczen(self):
        longest_line = ' '
        for line in self.zyczenia.split('\n'):
            if len(line) > len(longest_line):
                longest_line = line
        return longest_line

    def wielkosc_zyczen(self):
        wielkosc_font = 1
        font = ImageFont.truetype(sciezka_font, wielkosc_font)
        ilosc_lin = self.zyczenia.count('\n')+1
        longest_line = self.najdluzsza_linia_zyczen()
        while(font.getsize(longest_line)[0] < 0.7*self.tlo.size[0] and
              font.getsize(self.zyczenia)[1]*ilosc_lin < 0.7*self.tlo.size[1]):
            wielkosc_font += 1
            font = ImageFont.truetype(sciezka_font, wielkosc_font)
        return font

    def miejsce_wklejenia(self):
        font = self.wielkosc_zyczen()
        ilosc_lini = self.zyczenia.count('\n')+1
        longest_line = self.najdluzsza_linia_zyczen()
        x = (self.tlo.size[0] - font.getsize(longest_line)[0]) / 2
        y = (self.tlo.size[1] - font.getsize(self.zyczenia)[1] * ilosc_lini)/2
        return (x, y)

    def wklejenie_zyczen(self, sciezka):
        wspolrzedne = self.miejsce_wklejenia()
        font = self.wielkosc_zyczen()
        tlo = self.tlo
        tlo_zmienne = ImageDraw.Draw(tlo)
        tlo_zmienne.text(wspolrzedne, self.zyczenia, (117, 58, 7), font)
        tlo.save(sciezka)


if __name__ == '__main__':
    imie = input('Podaj imie solenizanta/soleniantki:')
    karolina = Kartka(imie)
    karolina.wklejenie_zyczen(przykladowa_sciezka)
