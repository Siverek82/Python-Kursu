print("""************************************
Üç Sayıdan Büyüğünü Ekrana Yazdırma
************************************
""")

a = float(input(" 1. sayıyı giriniz:  "))
b = float(input(" 2. sayıyı giriniz:  "))
c = float(input(" 3. sayıyı giriniz:  "))

if ( a > b and a > c ):
    print(" En büyük sayı", a)
elif ( b > a and b > c ):
    print(" En büyük sayı ", b)
elif ( c > a and c > b ):
    print(" En büyük sayı ", c)