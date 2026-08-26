luku=(input("Anna luku: "))
tyhja=""
pienin=int(luku)
suurin=int(luku)
while luku!= tyhja:
    print(f"{luku}")
    luku=(input("Anna luku: "))
    if luku=="":
        break

    uus_luku = int(luku)

    if uus_luku<pienin:
        pienin=uus_luku

    if uus_luku>suurin:
        suurin=uus_luku





print(f"pienin luku on {pienin} ja suurin luku on {suurin}")






