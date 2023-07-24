while True:
    n = int(input('Başlangıç sayınız: '))
    m = int(input('Bitiş sayınız: '))

    if n > m:
        print('Başlangıç sayısı daha küçük olmalı! Tekrar bir sayı gir')
    else:
        break

toplam = 0

for i in range(n, m):
    if i % 5 == 0:
        toplam += i

print("5'e tam bölünenlerin toplamı:", toplam)
