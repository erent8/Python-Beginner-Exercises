# # kenar_uzunlugu = int(input("Kenar uzunluğu giriniz: "))
# # h = int(input("Yükseklik gir: "))

# # alan = kenar_uzunlugu * h

# # print(f"alan, {alan},")

# p = int(input("Köşe Uzunlugu : "))
# k = int(input("Köşe Uzunlugu : "))
# hipotenus = p**2 + k**2

# print(f"{hipotenus}, sonuc sayının karesidir. ")

import matplotlib.pyplot as plt

# Kullanıcıdan kenar uzunluklarını al
p = int(input("Köşe Uzunluğu 1: "))
k = int(input("Köşe Uzunluğu 2: "))
hipotenus = (p ** 2 + k ** 2) ** 0.5

# Üçgen varlık kontrolü
if p + k > hipotenus and p + hipotenus > k and k + hipotenus > p:
    # Üçgen çizdir
    plt.plot([0, p, 0], [0, 0, k], marker='o', linestyle='-', color='blue')
    plt.plot([0, hipotenus], [0, k], linestyle='--', color='red')

    # Kenar uzunlukları etiketleri
    plt.text(p / 2, -0.5, str(p), ha='center', va='center', color='blue')
    plt.text(hipotenus / 2, k / 2, str(hipotenus), ha='center', va='center', color='red')
    plt.text(-0.5, k / 2, str(k), ha='center', va='center', color='blue')

    # Eksen düzenlemeleri
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5)
    plt.xlim(-1, max(p, hipotenus) + 1)
    plt.ylim(-1, max(k, hipotenus) + 1)
    plt.xlabel('X Ekseni')
    plt.ylabel('Y Ekseni')
    plt.title('Üçgen Çizimi')

    # Grafiği göster
    plt.grid()
    plt.show()
else:
    print("Bu uzunluklar bir üçgen oluşturmuyor.")
