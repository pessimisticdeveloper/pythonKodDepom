#Klavyeden girilen bir metnin harflerini alt alta yazdıran kod

metin = input("Metni Giriniz: ")
sayac = 0
while sayac < len(metin):
  print(metin[sayac])
  sayac += 1