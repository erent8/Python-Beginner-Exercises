import random

# Taş, kağıt ve makas için karakterler
tas = "taş"
kagit = "kağıt"
makas = "makas"

# Taş, kağıt ve makas karakterlerini içeren bir demet
oyun_karakterleri = (tas, kagit, makas)

# Kullanıcıdan seçim al
insan_secim = int(input("Seçim yap. Taş için '0', kağıt için '1', makas için '2' rakamına basın: "))

# Geçerli bir seçim mi kontrol et
if insan_secim > 2 or insan_secim < 0:
    print("Geçersiz seçim")
else:
    # Kullanıcının seçimini ekrana yazdır
    print("Seçiminiz:", oyun_karakterleri[insan_secim])

    # Bilgisayarın rastgele seçimi
    bilgisayar_secimi = random.randint(0, 2)
    print("Bilgisayar seçiyor...")
    print(oyun_karakterleri[bilgisayar_secimi])

    # Sonuçları karşılaştır ve kazananı/başarı durumunu ekrana yazdır
    if insan_secim == 0 and bilgisayar_secimi == 2:
        print("Kazandınız!")
    elif bilgisayar_secimi == 0 and insan_secim == 2:
        print("Kaybettiniz!")
    elif bilgisayar_secimi > insan_secim:
        print("Kaybettiniz")
    elif insan_secim > bilgisayar_secimi:
        print("Kazandınız!")
    else:
        print("Berabere kaldınız!")


# KODUMUZUN ALGORİTMASI ŞU ŞEKİLDEDİR:
# """
# Oyun karakterlerini tanımla: "taş", "kağıt", "makas".
# Oyun karakterlerini içeren bir demet oluştur: oyun_karakterleri = ("taş", "kağıt", "makas").
# Kullanıcıdan 0, 1 veya 2 olmak üzere bir seçim yapmasını iste ve seçimi insan_secim değişkenine ata.
# Eğer kullanıcının seçimi geçerli değilse, "Geçersiz seçim" mesajını ekrana yazdır ve adım 6'ya atla.
# Geçerli bir seçim yapıldıysa, kullanıcının seçimini ekrana yazdır.
# Bilgisayarın seçimini rastgele olarak 0, 1 veya 2 değerlerinden biri olarak belirle ve bilgisayar_secimi değişkenine ata.
# Bilgisayarın seçimini ekrana yazdır.
# Kullanıcının seçimi ile bilgisayarın seçimini karşılaştır:
# Eğer kullanıcı taş seçti (0) ve bilgisayar makas seçti (2) ise "Kazandınız!" mesajını ekrana yazdır.
# Eğer bilgisayar taş seçti (0) ve kullanıcı makas seçti (2) ise "Kaybettiniz!" mesajını ekrana yazdır.
# Eğer bilgisayarın seçimi kullanıcının seçiminden büyükse, yani kullanıcı kağıt (1) seçtiyse ve bilgisayar taş (0) veya makas (2) seçtiyse, "Kaybettiniz" mesajını ekrana yazdır.
# Eğer kullanıcının seçimi bilgisayarın seçiminden büyükse, yani kullanıcı taş (0) veya kağıt (1) seçtiyse ve bilgisayar makas (2) seçtiyse, "Kazandınız!" mesajını ekrana yazdır.
# Eğer kullanıcının seçimi ile bilgisayarın seçimi aynı ise, "Berabere kaldınız!" mesajını ekrana yazdır. 
# """" 
