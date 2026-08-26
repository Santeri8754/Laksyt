import random
koneen_luku= random.randint(1,10)

while True:
    luku=int(input("Arvaa luku: "))
    if luku==koneen_luku:
        print(f"Arvasit oikein  tietokoneen luvun {luku}")
        break
    elif luku>koneen_luku:
        print("Liian suuri arvaus")
    elif luku<koneen_luku:
        print("liian pieni arvaus")