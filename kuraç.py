
import random
print("Kadirf Sunar")
print("Kura Çekimi ✓\n")


adet=int(input("Kaç kişisiniz: "))
sira=""
siram=0
isimler=[]

for i in range(0, adet):
	sira+=str(i)
	isim=input("{}. kişi: ".format(siram+1))
	isimler.append(isim)
	siram+=1
	
while True:
	input("\n»")
	x=random.choice(sira)
	x=int(x)
	
	print("Talihli kişi: ", isimler[x])
