t = [100, 110, 200, 150, 300, 180, 150, 150, 100, 100]  
n = int(input())

összpihenőidő=0
mostaniido=0

for i in range(len(t)):
    mostaniido+=t[i]
    if (i+1)%5==0:
        maradoido=60-(mostaniido%60)
        összpihenőidő+=maradoido
        mostaniido+=maradoido

print(f"A teljes futási idő pihenőkkel: {mostaniido} másodperc")