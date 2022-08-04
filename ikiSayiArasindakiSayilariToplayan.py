#Klavyeden girilen iki sayı arasındaki sayıları toplayan kod.

toplam = 0
sayi1 = int(input('1. Sayıyı Giriniz: '))
sayi2 = int(input('2. Sayıyı Giriniz: '))
for i in range(sayi1+1,sayi2):
      toplam += i
print("{0} ile {1} arasındaki sayıların toplamı : {2}".format(sayi1,sayi2,toplam))