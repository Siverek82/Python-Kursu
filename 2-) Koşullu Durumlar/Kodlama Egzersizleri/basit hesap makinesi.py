print("""***************************

Hesap Makinası Programı

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi

***************************
""")

işlem = input(" İşlem giriniz: ")

a = int(input(" Birinci Sayı: "))
b = int(input(" İkinci Sayı: "))

if işlem == "1":
    print("{} + {} = {} ".format(a, b, a + b))
elif işlem == "2":
    print("{} - {} = {}".format(a, b, a - b))
elif işlem == "3":
    print("{} - {} = {}".format(a, b, a * b))
elif işlem == "4":
    print("{} - {} = {}".format(a, b, a / b))
else:
    print(""" Hatalı giriş lütfen
    1
    2
    3
    4
    bunlardan birini seçin. """)
