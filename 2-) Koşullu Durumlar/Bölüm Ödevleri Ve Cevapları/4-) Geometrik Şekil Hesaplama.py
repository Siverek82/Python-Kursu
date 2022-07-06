print("""**************************
Geometrik Şekil Hesaplama
**************************
""")
tip = input(" Üçgenin mi yoksa Dörtgenin mi tipini bulmak istiyorsunuz? ")
if tip == "üçgen" and "Üçgen":
    a = int(input("1. kenarı gir: "))
    b = int(input("2. sayıyı gir: "))
    c = int(input("3. sayıyı gir: "))
    if abs(a+b) > c and abs(a+c) > b and abs(b+c) > a:
        if a == b and a == c:
            print(" Eşkenar üçgen ")
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            print(" İkizkenar üçgen ")
        elif a != b and a != c:
            print(" Çeşitkenar Üçgen ")
    else:
        print(" Böyle bir üçgen çizilemez ")
elif tip == "dörtgen" and "Dörtgen":
    print(" Lütfen kenarları sırasıyla giriniz ")
    a = int(input(" Birinci kenarı giriniz "))
    b = int(input(" İkinci kenarı giriniz "))
    c = int(input(" Üçüncü kenarı giriniz "))
    d = int(input(" Dördüncü kenarı giriniz "))
    if a == b == c == d:
        print(" Kare ")
    elif a == c and b == d:
        print(" Dikdörtgen ")
    else:
        print(" Dörtgen ")
else:
    print(" Geçersiz şekil ")