
#Kadirf Sunar 

print("İyi günler..")

while True:
	print('''
a) Kaydol
b) Giriş Yap
f) Çıkış 
	''')
	islem1=input("Lütfen bir işlem seçiniz..: ")
	
	
	if islem1=="a":
		
		
		user=input("Kullanıcı Adı belirleyin.: ")
		password=input("Şifre belirleyin.: ")
		
		with open("defter2.csv", "r+") as dosya1:
			if user in dosya1.read():
				print("")
				print("Kullanıcı zaten Mevcut..")
				print("Dilerseniz Giriş yapabilirsiniz..\n Ya da Farklı bir kullanıcı adıyla kayıt olabilirsiniz..")
				continue
		
		
			else:
				dosya1.write(user + ";" + password + "\n")
				print("Kayıt Başarılı..")
				
		
		
	
	elif islem1=="b":
		
		sozluk={}
		
		with open("defter2.csv", "r") as dosya2:
			for bilgiler in dosya2:
				liste=bilgiler.strip().split(";")
				if len(liste)==2:
					sozluk[liste[0]]=liste[1]
					
					
		kname=input("Kullanıcı Adınızı girin: ")
		kpassw=input("Şifrenizi girin: ")
		
		if kname not in sozluk:
			print("Kullanıcı Mevcut degil?")
			print("Dilerseniz Kayıt olabilirsiniz..")
			
		elif kpassw!=sozluk[kname]:
			print("Kullanıcı bulundu, \n Şifre Yanlış..")
			
		else:
		
		
			print("\n Giriş Başarılı..")
			print("Hoş Geldiniz..")
			print("")
			
			print('''
			
KadirBANK atm
			
1) Bakiye Sorma
2) Para Çekme
3) Para Yatırma
q) Geri Dön
			
			''')
			
			bakiye=1000
			
			while True:
				print("İyi Günler", kname, "\n")
				
				islem2=input("Lütfen İşlem Giriniz..: ")
				
				if islem2=="q":
					print("")
					break
					
				elif islem2=="1":
					print("Mevcut Bakiye: ", bakiye, "TL")
					
				elif islem2=="2":
					tutar1=int(input("Çekmek İstediğiniz Tutar: "))
					if tutar1>bakiye:
						print("Yetersiz Bakiye..")
						break
					else:
						print("Çekilen Miktar: {} TL \n Kalan Bakiye: {} TL".format(tutar1, bakiye-tutar1))
						
				elif islem2=="3":
					tutar2=int(input("Yatırmak İstediğiniz Tutar: "))
					print("\n Yatırılan Tutar: {} TL \n Toplam Bakiye: {} TL".format(tutar2, bakiye+tutar2))
					
				else:
					print("Geçersiz Tuşlama.. Lütfen Tekrar Deneyiniz.. ")
					break
					
			
	elif islem1=="f":
		print("Çıkış Yapıldı..")
		print("Program Sonlandı..")
		break
		
	else:
		print("Hatalı Tuşlama.. Lütfen Tekrar Deneyin.. ")
		
		
