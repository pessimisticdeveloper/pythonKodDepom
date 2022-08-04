#Klavyeden kısa kenar uzunluğu ve uzun kenar uzunluğu girilen dikdörtgenin alan ve çevresini hesaplayan kod.

kisa_kenar = input('Kısa Kenar Uzunluğunu Girin : ')
uzun_kenar = input('Uzun Kenar Uzunluğunu Girin: ')
alan = int(kisa_kenar)*int(uzun_kenar)
cevre = 2*(int(kisa_kenar)+int(uzun_kenar))
print("Dikdörtgenin Alanı : {0}".format(alan))
print("Dikdörtgenin Çevresi : {0}".format(cevre))