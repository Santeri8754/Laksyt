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


auto=Auto("ABC-123",142)
auto.kuljettu_matka=2000
auto.kiihdyta(60)
auto.kulje(1.5)
print(f"Auton kuljettu matka on {auto.kuljettu_matka} km")
