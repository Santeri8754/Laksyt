import random
arpakuutio=int(input("Anna arpakuution määrä: "))
summa=0
for i in range(arpakuutio):
    noppa=random.randint(1,6)
    summa+=noppa
print(summa)

