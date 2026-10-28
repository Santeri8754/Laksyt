class Hissi:
    def __init__(self, alin, ylin):
        self.alin=alin
        self.ylin=ylin
        self.kerros =alin


    def kerros_ylös(self):
        self.kerros+=1
        print(f"Ylös: {self.kerros}")

    def kerros_alas(self):
        self.kerros -=1
        print(f"Alas: {self.kerros}")

    def siirry_kerrokseen(self,kerros):
        while self.kerros<kerros and self.kerros<self.ylin:
            self.kerros_ylös()

        while self.kerros> kerros and self.kerros>self.alin:
            self.kerros_alas()

class Talo:
    def __init__(self, alin, ylin,lkm):
        self.alin=alin
        self.ylin=ylin
        self.hissit=[]
        for i in range(lkm):
            self.hissit.append(Hissi(alin,ylin))

    def aja_hissiä(self, hissin_numero,kohdekerros):
        valittu_hissi=self.hissit[hissin_numero]
        valittu_hissi.siirry_kerrokseen(kohdekerros)
talo=Talo(0,5,3)
talo.aja_hissiä(0,4)