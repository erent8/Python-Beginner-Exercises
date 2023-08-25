def hesapla_vki(kilo, boy):
    vki = kilo / (boy ** 2)
    return vki

def vki_durumu(vki):
    if vki < 18.5:
        return "zayıfsınız."
    elif vki < 25:
        return "normalsiniz."
    elif vki < 30:
        return "fazla kilolusunuz."
    elif vki < 35:
        return "1. derece obezsiniz."
    elif vki < 40:
        return "2. derece obezsiniz."
    else:
        return "3. derece obezsiniz."

def main():
    try:
        kilo = float(input("Kilonuzu giriniz (örnek: 84.9): "))
        boy = float(input("Boyunuzu metre cinsinden giriniz: "))
        
        vki = hesapla_vki(kilo, boy)
        durum = vki_durumu(vki)
        
        print(f"Vücut kitle indeksiniz: {vki:.2f}, {durum}")
    except ValueError:
        print("Geçersiz değer girdiniz.")

if __name__ == "__main__":
    main()
