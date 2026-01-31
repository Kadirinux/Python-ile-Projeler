
import random
print("Kadirf Sunar ")
x=random.randint(1,1000)
m=1

while True:
	
	print("")
	sen=int(input( "{}) Sence x kaçtır?: ".format(m)))
	
	if sen==x:
		print("Doğru, x =", sen)
		print(m, "denemede buldun..")
		
		break
		
	else:
		print("Yanlış, x ≠", sen)
		m=m+1
		if sen<x:
			print("Daha büyük bir sayı..")
		else:
			print("Daha küçük bir sayı..")
	
