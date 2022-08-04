#Klavyeden girilen vize ve final notuna göre vizenin %40 ve finalin %60 ını alan ve sonucu ekranda gösteren python kodu.

vize = input("Vize Notunu Giriniz : ")
final = input("Final Notunu Giriniz : ")
ortalama = int(vize)*0.4 + int(final)*0.6
print("Ders Notunuz :{0} ".format(ortalama))