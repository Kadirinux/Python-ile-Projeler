# Kadirf Sunar
# En büyük/küçük sayı tespiti


adet=int(input("Kaç adet sayı Girilecek: "))

liste=[]
sira=1
for i in range(1, adet+1):
	sayi=int(input("{}. sayı: ".format(sira)))
	sira+=1
	liste.append(sayi)
	
print("En büyük sayı: ", max(liste))
print("En küçük sayı: ", min(liste))
