import random


def noppa():
    heitto= random.randint(1,6)
    return heitto

lasku=noppa()
while lasku != 6:
 print(lasku)
 lasku=noppa()


print(lasku)
