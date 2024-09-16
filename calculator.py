import tkinter as tk
from math import sqrt, pow, log, log10, sin, cos, tan, asin, acos, atan, pi, e, radians, degrees, factorial

# Hesaplama işlemlerini yapacak fonksiyon
def hesapla():
    try:
        # Girilen ifadeyi değerlendir
        sonuc = eval(giris.get() + ')')  # Kapanış parantezini otomatik ekle
        sonuc_label.config(text=f"Sonuç: {sonuc}")
    except Exception as ex:
        sonuc_label.config(text=f"Hata: {str(ex)}")

def temizle():
    giris.delete(0, tk.END)
    sonuc_label.config(text="")

# Tkinter penceresi
root = tk.Tk()
root.title("Gelişmiş Hesap Makinesi")

# Giriş alanı
giris = tk.Entry(root, width=40, borderwidth=5)
giris.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Sonuç etiketi
sonuc_label = tk.Label(root, text="", font=("Helvetica", 12))
sonuc_label.grid(row=1, column=0, columnspan=4)

# Butonlar
buton_metni = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Butonları ekrana yerleştirme
for i, row in enumerate(buton_metni):
    for j, metin in enumerate(row):
        button = tk.Button(root, text=metin, padx=20, pady=20, command=lambda m=metin: buton_tikla(m))
        button.grid(row=i+2, column=j)

# Gelişmiş fonksiyon butonları
gelismis_butonlar = [
    ('√', lambda: giris.insert(tk.END, "sqrt(")),
    ('^', lambda: giris.insert(tk.END, "**")),
    ('mod', lambda: giris.insert(tk.END, "%")),
    ('log', lambda: giris.insert(tk.END, "log10(")),
    ('ln', lambda: giris.insert(tk.END, "log(")),
    ('sin', lambda: giris.insert(tk.END, "sin(radians(")),
    ('cos', lambda: giris.insert(tk.END, "cos(radians(")),
    ('tan', lambda: giris.insert(tk.END, "tan(radians(")),
    ('π', lambda: giris.insert(tk.END, f"{pi}")),
    ('e', lambda: giris.insert(tk.END, f"{e}"))
]

# Gelişmiş butonları ekleme
for i, (metin, komut) in enumerate(gelismis_butonlar):
    button = tk.Button(root, text=metin, padx=20, pady=20, command=komut)
    button.grid(row=i//4+6, column=i%4)

# Fonksiyon butonları
temizle_buton = tk.Button(root, text="C", padx=20, pady=20, command=temizle)
temizle_buton.grid(row=2, column=4)

hesapla_buton = tk.Button(root, text="Hesapla", padx=20, pady=20, command=hesapla)
hesapla_buton.grid(row=3, column=4, rowspan=2)

# Buton tıklama işlemi
def buton_tikla(metin):
    if metin == '=':
        hesapla()
    else:
        giris.insert(tk.END, metin)

root.mainloop()
