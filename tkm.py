import random
import os
print("Kadirf Sunar")

while True:

	c =input("Taş/Kağıt/Makas ?: ")
	
	i="taş","kağıt","makas"
	a=list(i)
	b=random.choice(a)
	
	"taş"<"kağıt"
	"kağıt"<"makas"
	"makas"<"taş"
	
	if c==b:
		print("berabere: ", b, " = ", c)
		
	elif c>b:
		print("Sen kazandın.. :", c, " > ",b)
		
	elif c<b:
		print("Bilgisayar kazandı.. : ", c, " < ", b)
		
	else:
		print("Error..")

