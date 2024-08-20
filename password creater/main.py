import os
import base64
import hashlib
from cryptography.fernet import Fernet
from getpass import getpass

# Anahtar üretimi ve saklanması
def generate_key(master_password):
    key = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(key[:32])

# Güçlü bir parola üretici
def generate_password(length=12):
    import string
    import random
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Parolayı şifreli olarak dosyaya kaydet
def save_password(service, password, key):
    encrypted_password = Fernet(key).encrypt(password.encode())
    with open("passwords.txt", "a") as f:
        f.write(f"{service}: {encrypted_password.decode()}\n")

# Şifreyi çöz ve görüntüle
def load_password(service, key):
    with open("passwords.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            stored_service, encrypted_password = line.strip().split(": ")
            if stored_service == service:
                decrypted_password = Fernet(key).decrypt(encrypted_password.encode())
                return decrypted_password.decode()
    return None

def main():
    print("Parola Yöneticisi\n")
    master_password = input("Master Parolanızı Girin: ")  # Burada getpass yerine input kullandık
    key = generate_key(master_password)

    while True:
        print("\n1. Parola Üret")
        print("2. Parola Kaydet")
        print("3. Parola Görüntüle")
        print("4. Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            length = int(input("Parola uzunluğunu girin: "))
            new_password = generate_password(length)
            print(f"Oluşturulan Parola: {new_password}")

        elif choice == "2":
            service = input("Hizmet adını girin: ")
            password = input("Kaydetmek istediğiniz parolayı girin: ")
            save_password(service, password, key)
            print("Parola başarıyla kaydedildi.")

        elif choice == "3":
            service = input("Hizmet adını girin: ")
            password = load_password(service, key)
            if password:
                print(f"{service} için parola: {password}")
            else:
                print("Hizmet bulunamadı veya parola hatalı.")

        elif choice == "4":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
