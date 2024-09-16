import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def hesapla_fizik():
    try:
        if var.get() == "speed":
            mesafe = float(mesafe_entry.get())
            zaman = float(zaman_entry.get())
            hiz = mesafe / zaman
            sonuc_label.config(text=f"Hız: {hiz:.2f} m/s")
        elif var.get() == "distance":
            hiz = float(hiz_entry.get())
            zaman = float(zaman_entry.get())
            mesafe = hiz * zaman
            sonuc_label.config(text=f"Mesafe: {mesafe:.2f} metre")
        elif var.get() == "time":
            mesafe = float(mesafe_entry.get())
            hiz = float(hiz_entry.get())
            zaman = mesafe / hiz
            sonuc_label.config(text=f"Zaman: {zaman:.2f} saniye")
    except ValueError:
        messagebox.showerror("Girdi Hatası", "Lütfen geçerli sayılar girin.")

def hesapla_atis():
    try:
        ilk_hiz = float(hiz_atis_entry.get())
        aci_derece = float(aci_atis_entry.get())
        
        aci_radyan = np.radians(aci_derece)
        g = 9.81
        
        ucus_suresi = 2 * ilk_hiz * np.sin(aci_radyan) / g
        maksimum_yukseklik = (ilk_hiz**2 * np.sin(aci_radyan)**2) / (2 * g)
        menzil = (ilk_hiz**2 * np.sin(2 * aci_radyan)) / g
        
        sonuc_label.config(text=f"Uçuş Süresi: {ucus_suresi:.2f} s\n"
                                 f"Maksimum Yükseklik: {maksimum_yukseklik:.2f} metre\n"
                                 f"Menzil: {menzil:.2f} metre")
        
        t = np.linspace(0, ucus_suresi, num=100)
        x = ilk_hiz * np.cos(aci_radyan) * t
        y = ilk_hiz * np.sin(aci_radyan) * t - 0.5 * g * t**2
        
        plt.figure(figsize=(8, 6))
        plt.plot(x, y)
        plt.title('Atış Hareketi')
        plt.xlabel('Mesafe (metre)')
        plt.ylabel('Yükseklik (metre)')
        plt.grid(True)
        plt.show()
        
    except ValueError:
        messagebox.showerror("Girdi Hatası", "Lütfen geçerli sayılar girin.")

# Ana pencere oluşturma
root = tk.Tk()
root.title("Fizik ve Atış Hesap Makinesi")

# Fizik hesap makinesi
frame_fizik = tk.Frame(root)
frame_fizik.pack(pady=10)

var = tk.StringVar(value="speed")
tk.Radiobutton(frame_fizik, text="Hızı Hesapla", variable=var, value="speed").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame_fizik, text="Mesafeyi Hesapla", variable=var, value="distance").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame_fizik, text="Zamanı Hesapla", variable=var, value="time").pack(side=tk.LEFT, padx=10)

tk.Label(root, text="Hız (m/s):").pack(padx=10, pady=5)
hiz_entry = tk.Entry(root)
hiz_entry.pack(padx=10, pady=5)

tk.Label(root, text="Mesafe (metre):").pack(padx=10, pady=5)
mesafe_entry = tk.Entry(root)
mesafe_entry.pack(padx=10, pady=5)

tk.Label(root, text="Zaman (saniye):").pack(padx=10, pady=5)
zaman_entry = tk.Entry(root)
zaman_entry.pack(padx=10, pady=5)

hesapla_fizik_button = tk.Button(root, text="Hesapla", command=hesapla_fizik)
hesapla_fizik_button.pack(pady=10)

# Atış hesap makinesi
frame_atis = tk.Frame(root)
frame_atis.pack(pady=10)

tk.Label(root, text="İlk Hız (m/s):").pack(padx=10, pady=5)
hiz_atis_entry = tk.Entry(root)
hiz_atis_entry.pack(padx=10, pady=5)

tk.Label(root, text="Açı (derece):").pack(padx=10, pady=5)
aci_atis_entry = tk.Entry(root)
aci_atis_entry.pack(padx=10, pady=5)

hesapla_atis_button = tk.Button(root, text="Hesapla", command=hesapla_atis)
hesapla_atis_button.pack(pady=10)

# Sonuç etiketini oluşturma
sonuc_label = tk.Label(root, text="")
sonuc_label.pack(pady=10)

root.mainloop()
