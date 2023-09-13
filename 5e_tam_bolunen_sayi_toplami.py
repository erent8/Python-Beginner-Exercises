while True:
    baslangic = int(input("Başlangıç sayısını giriniz:  "))
    bitis = int(input("Bitiş sayısını giriniz:  "))

    # Başlangıç sayısının bitiş sayısından küçük olup olmadığını kontrol edilir.

    if baslangic > bitis:
        print("Başlangıç sayısı daha küçük olmalı, Tekrar bir sayı gir")
    else:
     # Eğer başlangıç sayısı bitiş sayısından küçükse döngüden çıkılır.
        break

# Toplamı hesaplamak için bir değişken başlatılır.

toplam = 0

    # Her sayıyı 5'e tam bölen bir sayı mı kontrol edilir.

# Başlangıç sayısından başlayarak bitiş sayısına kadar olan tüm sayıları kontrol etmek için bir döngü başlatılır.
for i in range(baslangic, bitis):
    # Her sayıyı 5'e tam bölen bir sayı mı kontrol edilir.
    if i % 5 == 0:
        # Eğer sayı 5'e tam bölünüyorsa, toplama eklenir.
        toplam += i

# 5'e tam bölünen sayıların toplamı ekrana yazdırılır.
print(f"5'e tam bölünenlerin toplamı: {toplam}")
# 13.09.23
