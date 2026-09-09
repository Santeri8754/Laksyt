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
maa_koodi=input("Anna maa koodi:")
sql = f"select type, count(*) from airport where iso_country = '{maa_koodi}' group by type"
kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
for rivi in tulos:
    print(rivi)