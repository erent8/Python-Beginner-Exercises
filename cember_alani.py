





import matplotlib.pyplot as plt  # Grafik kütüphanesi

# Kullanıcıdan yarıçapı al
yaricap = float(input("Yarıçapı giriniz: "))
pi = 3.14159

# Çevre ve alan hesaplama
cevre = 2 * pi * yaricap
alan = pi * (yaricap ** 2)

# Daireyi çizin
daire = plt.Circle((0, 0), yaricap, edgecolor='purple', facecolor='gray', alpha=0.5)
fig, ax = plt.subplots()
ax.add_patch(daire)
ax.set_aspect('equal', adjustable='datalim')

# Grafik özelliklerini ayarla
plt.xlim(-yaricap - 1, yaricap + 1)
plt.ylim(-yaricap - 1, yaricap + 1)
plt.axhline(y=0, color='red')  # X ekseni
plt.axvline(x=0, color='black')   # Y ekseni
plt.title('Daire Grafiği')
plt.xlabel('X Ekseni')
plt.ylabel('Y Ekseni')

# Grafiğin üzerine sonuçları ekle
ax.text(
    0, -yaricap - 0.5,  # Yazının konumu (x, y)
    f"Çevre: {cevre:.2f}\nAlan: {alan:.2f}",  # Gösterilecek metin
    color="blue",       # Yazı rengi
    fontsize=10,        # Yazı boyutu
    ha="center",        # Yatay hizalama
    va="center",        # Dikey hizalama
    bbox=dict(facecolor='white', alpha=0.7)  # Arka plan kutusu
)

# Grafik gösterimi
plt.show()

# Sonuçları konsola da yazdır
print(f"Alan: {alan}, Çevre: {cevre}")
print("\n------------------------------------")
print("Programımı kullandığınız için teşekkür ederim :) <3")
