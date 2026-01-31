#Kadirf Sunar
#faktöriyel 

sayi=int(input("Faktöriyelini Hesaplamak İstediğiniz Sayı: "))
fakt=1

for i in range(1,sayi+1):
	fakt*=i
	
print(fakt)

