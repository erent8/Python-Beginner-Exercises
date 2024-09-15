# Gerekli Kütüphane
from countryinfo import CountryInfo

# Ülke adını gir
country_name = input("Ülke adını gir: ")

try:
    country = CountryInfo(country_name)

    # Ülke bilgilerini yazdır  
    print("Ülke adı: ", country_name)
    print("Başkent Adı: ", country.capital())
    print("Nüfus: ", country.population(),"kişi")
    print("Alan: ", country.area(), "km²")
    print("Bölge: ", country.subregion())
    print("Dil: ", country.demonym())
    print("Para birimi: ", country.currencies())
    print("Dil:", country.languages())
    print("Komşu Ülkeler: ", country.borders())

except KeyError:
    print("Hatalı Şehir adı Girdin, lütfen tekrar dene.")
