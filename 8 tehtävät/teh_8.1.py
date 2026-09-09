import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='kissa12',
         autocommit=True,
        use_pure=True

     )
icao_koodi=input("Anna ICAO koodi:")
sql = f"select name,municipality from airport where ident = '{icao_koodi}'"
kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
for rivi in tulos:
    print(rivi)