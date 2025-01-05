t = [100, 110, 200, 150, 300, 180, 150, 150, 100, 100]  
n = int(input())

hanyadik=4
köridő=180
jelenlegiidő= 0
teljesítettkörök= 0

for i in range(hanyadik):
    jelenlegiidő+=t[i]
    while jelenlegiidő>=köridő:
        teljesítettkörök+=1
        jelenlegiidő-=köridő

print(f"A(z) {hanyadik}-edik/-adik zeneszám alatt a(z) {teljesítettkörök+1}. körünket futjuk.")