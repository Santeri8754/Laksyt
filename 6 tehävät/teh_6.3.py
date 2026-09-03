
def bensiini(gallonit):
    laskukaava = galloni * 3.785
    return gallonit*laskukaava


galloni=float(input("Anna gallonien määrä: "))
while galloni>=0:
    print(f"{bensiini(galloni)} on bensiininä")
    galloni = float(input("Anna gallonien määrä: "))

else:
    print("Syötit gallonit negatiivisena,joten ohjelma päättyi")

