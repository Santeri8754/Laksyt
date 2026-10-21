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

autot=[]
for i in range(1,11):
    tunnus=f"ABC-{i}"
    huippu=random.randint(100,200)
    uusi_auto=Auto(tunnus,huippu)
    autot.append(uusi_auto)
kisa_alkaa=1
while kisa_alkaa==1:
    for auto in autot:
        muutos=random.randint(-10,15)
        auto.kiihdyta(muutos)
        auto.kulje(1)
        if auto.kuljettu_matka>10000:
            kisa_alkaa=0

for auto in autot:
    print(f"Auto: {auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus} km/h, Nopeus: {auto.nopeus} km/h, "
          f"Matka: {auto.kuljettu_matka} km/h"
          )