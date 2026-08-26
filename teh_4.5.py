kayttis=input("Anna käyttäjätunnus: ")
salasana=input("Anna salasana: ")
laskuri=0
while kayttis!="python" or salasana!="rules":
    laskuri += 1
    print("Pääsy evätty")
    print(f"olet arvannut jo kerran {laskuri}")
    if laskuri >=5:
        print("Pääsysi on lopullisesti evätty")
        break
    kayttis=input("Anna kayttis uudestaan: ")
    salasana=input("Anna salasana uudestaan: ")



if kayttis=="python" or salasana=="rules":
        print("tervetuloa")

