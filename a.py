import random

t=[]
valasz=""
##
while valasz!="9":
    print("Válassz egy menüpontot:")
    if len(t)==0:
        print("1 - Tömb feltöltése billentyűzetről")
        print("2 - Tömb feltöltése véletlenszámokkal")
        print("3 - Kilépés")
    else:
        print("1 - Tömb feltöltése egyénileg")
        print("2 - Tömb feltöltése véletlenszámokkal")
        print("3 - Tömb ürítése")
        print("4 - Új elem hozzáadása")
        print("5 - Adott elem módosítása")
        print("6 - Adott elem törlése")
        print("7 - Tömb kiírása")
        print("8 - a feladat")
        print("9 - Kilépés")

    valasz=input("Menüpont száma: ")



    if valasz=="1":
        t=[int(input("Adj meg egy számot: ")) for j in range(int(input("Hány elemet szeretnél? ")))]



    if valasz=="2":
        meret=int(input("Hány véletlenszám legyen a tömbben? "))
        t=[random.randint(1, 100) for j in range(meret)]



    if valasz=="3" and len(t)>0:
        t=[]
        print("A tömb kiürítve.")



    if valasz=="4" and len(t)>0:
        ujelem=int(input("Add meg az új elemet: "))
        t.append(ujelem)



    if valasz=="5" and len(t)>0:
        index=int(input("Add meg a módosítandó elem indexét: "))
        if 0<=index<len(t):
            t[index] = int(input("Add meg az új értéket: "))



    if valasz=="6" and len(t)>0:
        index=int(input("Add meg a törlendő elem indexét: "))
        if 0<=index < len(t):
            t.pop(index)



    if valasz=="7" and len(t)>0:
        print("A tömb elemei:", t)


##########################


    if valasz=="8" and len(t)>0:
        print("a feladat:")
        osszeg=0

        for i in range(len(t)):
            osszeg+=t[i]
        print(f"A) {osszeg} mp = {osszeg//60} perc és {osszeg%60} másodperc")



    if valasz=="9":
        print("Kilépés a programból.")
