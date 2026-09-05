nimet=set()
nimi=input("Syötä nimi: ")

while nimi != "":
    if nimi in nimet:
        print("Nimi on syötetty jo")

    else:
        nimet.add(nimi)
        print("Nimi on uusi")
    nimi = input("Syötä nimi: ")

print(nimet)