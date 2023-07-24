yazi = input('bir metin giriniz: ')
 
sesli = ("a, e, ı, i, o, ö, u, ü")
sessiz = ("z, y, v, t, ş, s, r, p, n, r, m, l, k, h, j, ğ, g, d, ç, c, b")
sesli_sayac = 0
for harf in yazi:
    if harf in sesli:
        sesli_sayac +=1

print('sesli harf sayisi : ', sesli_sayac)
print('Sessiz harf sayisi', len(yazi)-(sesli_sayac))
