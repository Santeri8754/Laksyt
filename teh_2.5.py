#Kysytään nauloja,leivisköitä ja luoteja.
leiviskät=float(input("Anna leiviskät: "))
naula=float(input("Anna naulat: "))
luoti=float(input("Anna luodit: "))

#Muutetaan leiviskär grammoiksi
leiviskä_n=leiviskät*20
leiviskä_l=leiviskä_n*32
leiviskä_g=leiviskä_l*13.3

#Muutetaan naulat grammoiksi
naula_l=naula*32
naula_g=naula_l*13.3

#Muutetaan luodit grammoiksi
luoti_g=luoti*13.3

#Lasketaan yhteen.
yhteensä_g=naula_g+luoti_g+leiviskä_g

#Garmmat kilogrammoiksi
kg=yhteensä_g//1000

# Otetaan yli jääneet grammat
g=yhteensä_g % 1000
#Tulos
print(f"{kg:.0f} on kilogrammaaa ja {g:.2f} grammaa.")
