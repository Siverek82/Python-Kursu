print("""*********************************************
Vize- Final Notuna Göre Harf Notu Hesaplama
*********************************************
""")
vize1 = float(input(" Vize1 Notunu Giriniz:  "))
vize2 = float(input(" Vize2 Notunu Giriniz:  "))
final = float(input(" Final Notunu Giriniz:  "))

toplam_not = ((vize1*30)/100) + ((vize2*30)/100) + ((final*60)/100)

if toplam_not >= 90:
    print(" AA ")
elif toplam_not >= 85:
    print(" BA ")
elif toplam_not >= 80:
    print(" BB ")
elif toplam_not >= 75:
    print(" CB ")
elif toplam_not >= 70:
    print(" CC ")
elif toplam_not >= 65:
    print(" DC ")
elif toplam_not >= 60:
    print(" DD ")
elif toplam_not >= 55:
    print(" FD ")
elif toplam_not >= 50:
    print(" FF ")
else:
    print(" Üzgünüm! Malesef bu dersten kaldınız.  ")