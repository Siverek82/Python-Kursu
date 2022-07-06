print('Hipotenüsü bulma')
dikkenar = float(input('Dik kenarın uzunluğunu yazınız: '))
taban = float(input('Tabanın uzunluğunu yazınız: '))
hipotenüs = (dikkenar**2+taban**2)**0.5
#Normalde dikkenar**2+taban**2 = hipotenüs**2 işte burada bide her tarafın karekökünü alıyoruz. o yüzden
# hipotenüs = (dikkenar**2+taban**2)**0.5 bu formülü kullanıyoruz
print('İşlem başarılı. Hipotenüs: ',hipotenüs)