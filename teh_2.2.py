import math
#Luetaan syöte
säde = float(input("Anna ympyrän säde: "))

#Laskutoimitus
ala = math.pi * säde**2;

#Lopputulos
print(f"Pinta-ala on {ala:.2f}")