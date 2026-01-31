print("Kadirf Sunar")
print("")
print("Hesap Makinesi")
while True:
	
	print("""

a) Toplama
b) Çıkarma
c) Çarpma
d) Bölme
f) Çıkış
""")
	
	islem=input("Bir İşlem Seç: ")
	print("")
	
	if islem=="a":
		m=0
		k=int(input("Lütfen kaç Sayıyı Toplayacağınızı belirtin: "))
		for i in range(1,k+1):
			s=int(input("Bir Sayı girin: "))
			m=m+s
			print(m)
			
		print("")
		
	elif islem=="b":
		sayi1=int(input("Bir sayı gir sayı girin: "))
		sayi2=int(input("Bir sayı daha girin: "))
		print("Sonuç: ", sayi1-sayi2)
		print("")
		
		
	elif islem=="c":
		m2=1
		k2=int(input("Lütfen kaç Sayıyı Çarpacağınızı belirtin: "))
		for i2 in range(1,k2+1):
			s2=int(input("Bir Sayı girin: "))
			m2=m2*s2
			print(m2)
		
		print("")
		
	elif islem=="d":
		sayi3=int(input("Bölünen Sayıyı girin: "))
		sayi4=int(input("Bölen Sayıyı girin: "))
		print("Sonuç: ", sayi3/sayi4)
		print("")
		
		
	elif islem=="f":
		print("Çıkış Yaptın..")
		print("Program sonlandı..")
		
		break
		
		
	
