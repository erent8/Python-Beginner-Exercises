import random

def yazitura():
    print("Yazı mı, tura mı atmak istersiniz?")
    secim = input("Lütfen 'yazı' veya 'tura' olarak seçim yapın: ").lower()

    if secim == 'yazı' or secim == 'tura':
        rastgele_sayi = random.randint(0, 1)
        sonuc = 'yazı' if rastgele_sayi == 0 else 'tura'

        if secim == sonuc:
            print(f"Tebrikler, kazandınız! Sonuç: {sonuc}")
        else:
            print(f"Üzgünüm, kaybettiniz! Sonuç: {sonuc}")
    else:
        print("Geçersiz seçim. Lütfen 'yazı' veya 'tura' olarak seçin.")

yazitura()
