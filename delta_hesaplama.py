import math 

print('Merhaba, Δ Hesaplama Programına Hoş Geldiniz :)')
     
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

# delta hesaplama
delta = b**2 - 4*a*c
print('Δ =', delta)

if delta > 0:
    kok1 = (-b + math.sqrt(delta)) / (2*a)
    kok2 = (-b - math.sqrt(delta)) / (2*a)
    print('Sistemin iki kökü vardır:', kok1, 've', kok2)

elif delta < 0:
    print('Denklemin Reel Kökü Yoktur.')

elif delta == 0:
    kok = -b / (2*a)
    print('Kökler çakışıktır. İki reel kök vardır ve bunlar aynıdır:', kok)
