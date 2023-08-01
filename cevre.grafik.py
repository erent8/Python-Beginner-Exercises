# import matplotlib

# r = float(input("Yarıçapı gir: "))
# pi = 3.14
# cevre = 2 * pi*r
# alan = pi * (r*2*2) 
# print(f"alan, {alan} olarak bulundu. çevre, {cevre} olarak bulundu.")


import matplotlib.pyplot as plt

# Kullanıcıdan yarıçap al
r = float(input("Yarıçapı gir: "))
pi = 3.14
cevre = 2 * pi * r
alan = pi * (r ** 2)

# Çemberin grafiğini çiz
circle = plt.Circle((0, 0), r, edgecolor='purple', facecolor='gray')
fig, ax = plt.subplots()
ax.add_patch(circle)
ax.set_aspect('equal', adjustable='datalim')

# Grafik özelliklerini ayarla
plt.xlim(-r - 1, r + 1)
plt.ylim(-r - 1, r + 1)
plt.axhline(y=0, color='red')
plt.axvline(x=0, color='black')
plt.title('Çember')
plt.xlabel('X Ekseni')
plt.ylabel('Y Ekseni')

# Grafiği göster
plt.show()

print(f"Alan: {alan}, Çevre: {cevre}")
