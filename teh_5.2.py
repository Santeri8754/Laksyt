

lista=[]
tyhja=""
while True:
    luvut = input("Anna luvut: ")
    if  luvut== tyhja:
        break

    lista.append(int(luvut))



lista.sort(reverse=True)

print(lista[:5])