# is_prime adında bir fonksiyon tanımlanıyor. Bu fonksiyon, bir sayının asal olup olmadığını kontrol edecek.
def is_prime(number):
    # İlk olarak, sayının 1'den küçük veya eşit olup olmadığı kontrol ediliyor.
    if number <= 1:
        return False
    # Eğer sayı 2 ise, asal olarak kabul ediliyor. (2, tek çift asal sayıdır.)
    elif number == 2:
        return True
    # Eğer sayı çift bir sayı ise, asal olmadığı için False döndürülüyor.
    elif number % 2 == 0:
        return False

    # Bu kısımda, asal olmayan sayıları eleme işlemi yapılacak.
    # Asal olmayan sayılar genellikle kendinden daha küçük bölenlere sahiptir.
    # Bu yüzden 2 ve kök(number)'a kadar olan sayıları kontrol edebiliriz.

    # number'in karekökünü alıyoruz ve bir üst tamsayıya yuvarlıyoruz, böylece kök(number) + 1 kadar bir döngü yaparız.
    for i in range(3, int(number**0.5) + 1, 2):
        # Eğer number, i'ye tam bölünüyorsa, asal olmadığı için False döndürülüyor.
        if number % i == 0:
            return False

    # Eğer yukarıdaki koşulların hiçbiri sağlanmıyorsa, sayı asal olarak kabul ediliyor ve True döndürülüyor.
    return True

# Kullanıcıdan bir sayı alınıyor.
number = int(input("Bir sayı girin: "))

# is_prime fonksiyonu çağrılıyor ve verilen sayının asal olup olmadığı kontrol ediliyor.
if is_prime(number):
    print(f"{number} bir asal sayıdır.")
else:
    print(f"{number} bir asal sayı değildir.")
