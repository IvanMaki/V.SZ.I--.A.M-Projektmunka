import random

t = [100, 110, 200, 150, 300, 180, 150, 150, 100, 100]  
n = int(input())

t=[]
valasz=""

while valasz!="12":
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
        print("8 - c feladat")
        print("9 - d feladat")
        print("10 - Kilépés")

    valasz=input("Menüpont száma: ")



    if valasz=="1":
        t=[int(input("Adj meg egy számot: ")) for j in range(int(input("Hány elemet szeretnél? ")))]



    if valasz=="2":
        meret=int(input("Hány véletlenszám legyen a tömbben?? "))
        t=[random.randint(1, 100) for j  in range(meret)]



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


if valasz=="8" and len(t)>0:
    print("c feladat")

összpihenőidő=0
mostaniido=0


for i in range(len(t)):
    mostaniido+=t[i] 
    if (i+1)%5==0:
        maradoido=60-(mostaniido%60) #Mennyi idő kell a következő percig!
        összpihenőidő+=maradoido
        mostaniido+=maradoido

print(f"A teljes futási idő pihenőkkel: {mostaniido} másodperc")