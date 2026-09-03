def listanluvut(luku):
    karsittu=[]
    for luku in lista:
        if luku % 2==0:
            karsittu.append(luku)
    return karsittu


lista=[3,5,6,78,0]
karsittu_lista=listanluvut(lista)
print(karsittu_lista)
print(lista)