import math
def pizza(halkaisija,hinta):
    r=(halkaisija/100)/2
    pinta_ala=math.pi*(r**2)
    return hinta/pinta_ala


halkaisijat1=float(input("Anna ensimmäisen pizzan halkaisija"))
hinta1=float(input("Anna ensimmäisen pizzan hinta euroina"))
halkaisijat2=float(input("Anna toisen pizzan halkaisija"))
hinta2=float(input("Anna toisen pizzan hinta euroina"))
neliohinta1=pizza(halkaisijat1,hinta1)
neliohinta2=pizza(halkaisijat2,hinta2)

if neliohinta1>neliohinta2:
    print(f"toinen pitsa antaa paremman vastineen {neliohinta1:.2f}")
else:
    print(f"Ensimmäinen pitsa antaa paremman vastineen {neliohinta2:.2f}")
