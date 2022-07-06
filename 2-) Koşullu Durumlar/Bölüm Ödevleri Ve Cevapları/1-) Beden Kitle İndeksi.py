print("""******************************
Beden Kitle İndeksi
******************************
""")
kilo = float(input(" Kilonuzu giriniz ( kg ): "))
boy =  float(input(" Boyunuz  giriniz ( cm ): "))
bki = kilo/((boy/100)**2) # boyu cm cinsinden girdikleri için biz bunu metreye çevirmeliyiz
                          # bunun için 100 e böldük sonra karesini almak için de **2 yaptık

if bki < 18.5:
    print(" Zayıf. ")
elif bki < 25:
    print(" Normal ")
elif bki < 30:
    print(" Fazla Kilolu ")
elif bki > 30:
    print(" Obez ")
