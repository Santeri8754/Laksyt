# Lisätään syöte
kuhan_pituus = float(input("Anna kuhan pituus"))

#Tarkistetaan onko kuha alle 37 senttimetriä pienenmpi
if kuhan_pituus < 37:
    #Lasku toimitus lasketaan kuinka paljon kuha on alamittainen
    alamitta = 37 - kuhan_pituus
    print(f"kuhasi on {alamitta} cm liian lyhyt!")
    print("Laske kuha takaisin järveen")

else:
    print("Kuhasi on täydellinen")