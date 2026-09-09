import mysql.connector
from geopy.distance import geodesic
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='kissa12',
         autocommit=True,
        use_pure=True

     )
icao1=input("Anna icao koodi:")
icao2=input("Anna icao koodi:")
sql1 = f"select latitude_deg,longitude_deg  from airport where ident = '{icao1}' "
kursori1 = yhteys.cursor()
kursori1.execute(sql1)
kentta1=kursori1.fetchone()
sql2 = f"select latitude_deg,longitude_deg  from airport where ident = '{icao2}' "
kursori2 = yhteys.cursor()
kursori2.execute(sql2)
kentta2=kursori2.fetchone()

etaisyys= geodesic (kentta1,kentta2).km
print(f"Etäisyys on kilometreinä noin {etaisyys:.2f}")