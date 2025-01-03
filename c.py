t = [100, 110, 200, 150, 300, 180]  
n = int(input())
ossz_masodperc = 0  

for i in range(n):
    ossz_masodperc += t[i]  
    if (i + 1) % 5 == 0:  
        maradek = ossz_masodperc % 60  
        ossz_masodperc += maradek  

minutes = ossz_masodperc // 60
seconds = ossz_masodperc % 60

print(f"Teljes futásidő: {minutes} perc {seconds} másodperc")
