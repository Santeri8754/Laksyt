#Kysytään suorakulmion kantaa ja korkeuta
kanta=float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus:"))

#Laskutoimitus, jossa lasketaan piiri ja pintalal suorakulmiolle.
ala= kanta*korkeus
piiri= 2* (kanta + korkeus)

# tulostetaan tulos.
print(f"Suorakulmion pinta-ala on {ala:.2f} ja piiri on {piiri:.2f}")