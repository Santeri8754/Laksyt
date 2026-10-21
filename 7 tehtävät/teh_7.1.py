kuukauden_nr=input("Anna kuukauden numero: ")
vuodenajat=("kevät", "kesä", "syksy", "talvi")
talvi=("1","12","2")
kevät=("3","4","5")
kesä=("6","7","8")
syksy=("9","10","11")
if kuukauden_nr in talvi:
    print(vuodenajat[3])
elif kuukauden_nr in kevät:
    print(vuodenajat[0])
elif kuukauden_nr in kesä:
    print(vuodenajat[1])
elif kuukauden_nr in syksy:
    print(vuodenajat[2])
