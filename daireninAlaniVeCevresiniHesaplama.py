#Klavyeden yarıçapı girilen dairenin çevresini ve alanını hesaplayan kod

yaricap = input('Yarıçapı Girin : ')
cevre = (2*3.14*float(yaricap))
alan = 3.14*float(yaricap)*float(yaricap)
print("Alan :{0} ".format(alan))
print("Çevre :{0} ".format(cevre))