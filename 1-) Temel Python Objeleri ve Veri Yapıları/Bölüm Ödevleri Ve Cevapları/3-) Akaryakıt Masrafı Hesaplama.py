print('Akaryakıt masrafı hesaplama')
pompafiyatı = float(input('1 Litre yakıtın fiyatı ne kadar: '))
tüketim = float(input('1 km de tüketilen yakıt: '))
mesafe = int(input('Kaç km yol gittiniz: '))
masraf = (mesafe*tüketim)*pompafiyatı
print('İşlem başarılı. Şuana kadar {} km yol gittiniz. Ödediğiniz akaryakıt ücreti {}'.format(mesafe, masraf))
