#Kysytään käyttäjän biloginen sukupuoli ja hemoglobiininenarvo

sukupuoli=input("Anna sukupuolesi: ")
hemo=float(input(f"Anna hemolobiininenarvo: "))

#Tässä katsotaa if lauseella  ovatko naisen arvot liian alhaiset vain liian korkeat vai normaalit
if sukupuoli=="nainen":
    print("olet nainen")
    if hemo<117:
        print("arvosi ovat liian alhaiset")
    elif hemo> 175:
        print("Arvosit ovat liian korkeat")
    else:
        print("Arvosit ovat normaalit")

# Tässä sitten taas sama homma miehille.
if sukupuoli=="mies":
    print("olet mies")
    if hemo<134:
        print("arvosi ovat liian alhaiset")
    elif hemo> 195:
        print("Arvosit ovat liian korkeat")
    else:
        print("Arvosit ovat normaalit")
