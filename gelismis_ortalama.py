def ortalama_hesapla(sayilar):
    toplam = sum(sayilar)
    ortalama = toplam / len(sayilar)
    return ortalama

sayilar = []

while True:
    try:
        sayi = float(input("Bir sayı girin (Çıkmak için 'q' tuşuna basın): "))
        sayilar.append(sayi)
    except ValueError:
        break

ortalama = ortalama_hesapla(sayilar)
print("Girilen sayılar:", sayilar)
print("Toplam:", sum(sayilar))
print("Ortalama:", ortalama)
