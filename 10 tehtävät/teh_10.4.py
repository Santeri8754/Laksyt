import random
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
class Kilpailu:
    def __init__(self,nimi,pituus_km,autot):
        self.nimi=nimi
        self.pituus_km=pituus_km
        self.autot=autot
    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.autot:
            print(f"Auto: {auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus} km/h, Nopeus: {auto.nopeus} km/h, "
                  f"Matka: {auto.kuljettu_matka} km/h"
                  )
    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka>=self.pituus_km:
                return True
        return False
kilpa_autot=[]
for i in range(1,11):
    tunnus=f"ABC-{i}"
    huippu=random.randint(100,200)
    uusi_auto=Auto(tunnus,huippu)
    kilpa_autot.append(uusi_auto)
romuralli=Kilpailu("Suurin romuralli",8000,kilpa_autot)
tunnit=0
while not romuralli.kilpailu_ohi():
    romuralli.tunti_kuluu()
    tunnit+=1
    if tunnit % 10==0:
        print(f"{tunnit} tuntia on kulunut")
        romuralli.tulosta_tilanne()

print("Kilpailu on päättynyt", f"Aikaa kului noin {tunnit} tuntia")
romuralli.tulosta_tilanne()

