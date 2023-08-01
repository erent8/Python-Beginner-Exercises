from tabulate import tabulate

def ders_ortalama(ders_sayisi):
    toplam_puan = 0
    dersler = []

    for i in range(1, ders_sayisi + 1):
        ders_adi = input(f"{i}. ders adını giriniz: ")
        vize = int(input(f"{ders_adi} ders vize notunuzu giriniz: "))
        proje = int(input(f"{ders_adi} ders proje notunuzu giriniz: "))
        final = int(input(f"{ders_adi} ders final notunuzu giriniz: "))

        # Dersin yılsonu puanını hesapla (vize %30, proje %30, final %40)
        yilsonu_puan = vize * 0.3 + proje * 0.3 + final * 0.4

        toplam_puan += yilsonu_puan

        # Ders bilgilerini dersler listesine ekle
        dersler.append([ders_adi, vize, proje, final, yilsonu_puan])

    # Dönem ortalamasını hesapla
    ortalama = toplam_puan / ders_sayisi

    return ortalama, dersler


ders_sayisi = int(input("Kaç dersiniz var?:  "))
ortalama, dersler = ders_ortalama(ders_sayisi)

# Ders bilgilerini tabloya dönüştürerek yazdır
tablo = tabulate(dersler, headers=["Ders Adı", "Vize", "Proje", "Final", "Yılsonu Puanı"])
print(tablo)

print(f"Dönem ortalaması: {ortalama:.2f}")

if ortalama >= 90:
    print("Harf Notu: AA")
elif ortalama >= 85:
    print("Harf Notu: BA")
elif ortalama >= 80:
    print("Harf Notu: BB")
elif ortalama >= 75:
    print("Harf Notu: CB")
elif ortalama >= 70:
    print("Harf Notu: CC")
elif ortalama >= 65:
    print("Harf Notu: DC")
elif ortalama >= 60:
    print("Harf Notu: DD")
elif ortalama >= 50:
    print("Harf Notu: FD")
else:
    print("Harf Notu: FF")
