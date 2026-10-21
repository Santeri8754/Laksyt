
lentoasemat = {}
while True:
    toiminto = input("Haluatko syöttää uuden lentoaseman,hakea,lopettaa: ")
    if toiminto=="syöttää":
        lentoasema=input("Anna lentoaseman nimi: ")
        icao=input("Anna  icaokoodi:")
        lentoasemat[icao] =lentoasema
    elif toiminto == "haku":
        icao = input("Anna  icaokoodi:")
        print(lentoasemat[icao])
    elif toiminto == "lopettaa":
        break