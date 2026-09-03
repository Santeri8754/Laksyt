import random


def noppa(tahko):
    heitto= random.randint(1,tahko)
    return heitto

lasku=noppa(21)
while lasku != 21:
 print(lasku)
 lasku=noppa(21)


print(lasku)
