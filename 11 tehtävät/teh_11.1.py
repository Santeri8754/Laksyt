

class Julkaisu:
    def __init__(self,nimi):
      self.nimi=nimi

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi} ")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja,sivumäärä ):
        super().__init__(nimi)
        self.kirjoittaja=kirjoittaja
        self.sivumäärä=sivumäärä

    def tulosta_tiedot(self):
            print(f" kirjoittaja: {self.kirjoittaja}")
            print(f"sivumäärä: {self.sivumäärä}")
            super().tulosta_tiedot()

class Lehti(Julkaisu):
    def __init__(self,nimi,päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja=päätoimittaja


    def tulosta_tiedot(self):
        print(f"päätoimittaja: {self.päätoimittaja}")
        super().tulosta_tiedot()



julkaisut=[]
julkaisut.append(Lehti ("Aku ankka","Aki hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6 ","Rosa Liksom",200))

for j in julkaisut:
    j.tulosta_tiedot()