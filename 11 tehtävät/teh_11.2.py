class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus=0
        self.kuljettu_matka=0

    def kiihdyta(self,nopeuden_muutos):
        self.nopeus+=nopeuden_muutos
        if self.nopeus>self.huippunopeus:
            self.nopeus=self.huippunopeus
        elif self.nopeus<0:
            self.nopeus=0

    def kulje(self,tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

class Sähköauto(Auto):
    def __init__(self,rekisteritunnus,huippunopeus,akkukapasiteetti):
        super().__init__(rekisteritunnus,huippunopeus)
        self.akkukapasiteeti=akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self,rekisteritunnus,huippunopeus,bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko=bensatankin_koko

sahkoauto=Sähköauto("ABC-15",180,52.5)
polttomoottoriauto=Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdyta(110)
polttomoottoriauto.kiihdyta(100)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähkoauto {sahkoauto.rekisteritunnus} matkamittarilukema: {sahkoauto.kuljettu_matka} km")
print(f"Polttomootoriauto {polttomoottoriauto.rekisteritunnus} matkamittarilukema: {polttomoottoriauto.kuljettu_matka} km")
