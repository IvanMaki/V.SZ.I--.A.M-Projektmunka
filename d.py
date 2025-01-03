t = [100, 110, 200, 150, 300, 180, 150, 150, 100, 100]  
n = int(input())
k = 4


ossz_ido_kig = 0
pihi = 0

for i in range(k):
    ossz_ido_kig += t[i]
    if (i + 1) % 5 == 0: 
        maradek_mp = ossz_ido_kig % 60
        pihi += maradek_mp
        ossz_ido_kig += maradek_mp

osszes_ido_pihenessel_egyutt = ossz_ido_kig + pihi


korok = osszes_ido_pihenessel_egyutt // 180
print(f"A {k}. zeneszám alatt a(z) {korok+1}. kört futjuk éppen")