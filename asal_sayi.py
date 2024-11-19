def is_prime(number):
    """
    Bir sayının asal olup olmadığını kontrol eder.
    """
    # Negatif sayılar, 0 ve 1 asal değildir.
    if number <= 1:
        return False
    # 2, tek çift asal sayıdır.
    elif number == 2:
        return True
    # Çift sayılar asal değildir.
    elif number % 2 == 0:
        return False

    # Sayının kareköküne kadar olan tek sayılarla bölen kontrolü.
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False

    return True

# Kullanıcı girişi ve hata yönetimi
while True:
    try:
        # Kullanıcıdan sayı al
        number = int(input("Bir sayı girin (çıkmak için 'q'): "))
        # Asallık kontrolü yap
        if is_prime(number):
            print(f"{number} bir asal sayıdır.")
        else:
            print(f"{number} bir asal sayı değildir.")
    except ValueError:
        # Kullanıcı çıkış yapmak istiyorsa
        print("Geçerli bir sayı girin veya çıkmak için 'q' tuşlayın.")
        break







# ------ TKİNKER MODÜLLÜ VERSİYON ------ #


import tkinter as tk
from tkinter import messagebox

def is_prime(number):
    """
    Bir sayının asal olup olmadığını kontrol eder.
    """
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False

    return True

def check_prime():
    """
    Kullanıcının girdiği sayının asal olup olmadığını kontrol eder.
    """
    try:
        # Kullanıcının girdiği değeri al
        number = int(entry.get())
        # Asallık kontrolü yap
        if is_prime(number):
            result_label.config(text=f"{number} bir asal sayıdır.", fg="green")
        else:
            result_label.config(text=f"{number} bir asal sayı değildir.", fg="red")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir tam sayı girin!")

# Tkinter arayüzü
root = tk.Tk()
root.title("Asal Sayı Kontrolü")

# Giriş etiketi
label = tk.Label(root, text="Bir sayı girin:", font=("Arial", 12))
label.pack(pady=10)

# Giriş alanı
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Kontrol butonu
check_button = tk.Button(root, text="Kontrol Et", command=check_prime, font=("Arial", 12), bg="blue", fg="white")
check_button.pack(pady=10)

# Sonuç etiketi
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Uygulama döngüsü
root.mainloop()
