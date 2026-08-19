#Kysytään kokonaislukuja
luku1=int(input("Anna kokonaisluku1: "))
luku2=int(input("Anna kokonaisluku2: "))
luku3=int(input("Anna kokonaisluku3: "))

#Laskutoimitukset
summa=luku1+luku2+luku3
tulo=luku1*luku2*luku3
keskiarvo=luku1+luku2+luku3/3

#Tulostetaan summa, tulo ja keskiarvo.
print(f"Lukujen summa on {summa}")
print(f"Lukujen tulo on {tulo}")
print(f"Lukujen keskiarvo on {keskiarvo:.2f}")