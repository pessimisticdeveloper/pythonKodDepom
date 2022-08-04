#Bir dersin ortalaması girilen öğrencinin o dersten geçip geçmediğini gösteren python kodu.
# (50den büyükse geçti değilse kaldı yazdıran kod.)

ortalama = float(input('Ders Ortalamanızı Girin : '))

if (ortalama >= 50):
    print("Dersten Geçtiniz.")
else:
    print("Dersten Kaldınız.")