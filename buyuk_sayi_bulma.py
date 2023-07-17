a = int(input('A sayısı: '))
b = int(input('B sayısı: '))
c = int(input('C sayısı: '))

if a > b and a > c:
    print('A, en büyük sayıdır.')

elif b > a and b > c:
    print('B, en büyük sayıdır.')

elif c > a and c > b:
    print('C, en büyük sayıdır.')    

else:
    print('Tüm sayılar eşittir.')
    
