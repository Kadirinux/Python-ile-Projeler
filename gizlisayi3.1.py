import random

print("Kadirf Sunar..")

print("____________________")
print("👋 Hoşgeldin.. 😊   <--")
print("-----•-------•-------")

aralik=[""]
soyle=int(input("-->🤔 1 ile kaç arasında oynamak istediğini söyle: "))

for i in range(soyle):
    aralik.append(i)

sectim=random.choice(aralik)
print(f"1 ile {soyle} arasından BİR SAYI TUTTUM.. \n")




print("1) Serbest Mod \n2) Sınırlı Mod \n-->  Oyun mod'unu seç: ", end="")
level=int(input(""))
print("\n")

if level==1:
    adet=0
    print("Serbest Mod Seçildi..")
    print("Sınırsız Can Hakınız Var..\n")

    while True:
        print(adet+1, end=" -> ")
        sensec=int(input("Sayıyı tahmin et: "))
        if sensec==sectim:
            print("👌 Tebrikler..", adet+1, "seferde sayıyı buldun..\n")
            break
        else:
            if sensec<sectim:
                print("Hayır, Seçtiğim sayı daha büyük bir sayı..")
            else:
                print("Hayır, Seçtiğim sayı daha küçük bir sayı..")
            adet+=1


elif level==2:
    print("Sınırlı Mod Seçildi..")
    print("Sınırlı Can Hakkınız Var.. \n")
    print("a) Kolay \nb) Orta \nc) Zor \n-->  Zorluk derecesini seç: ", end="")
    zorluk=input("")
    print("\n")

    if zorluk=="a":
        print("Kolay Mod Seçildi.. ")
        print("30 Can Hakkınız Var..\n")
        adet=30
        can=adet
        while True:
            print(can, end=" -> ")
            sensec=int(input("Sayıyı tahmin et: "))
            if sensec==sectim:
                print("👌 Tebrikler..", (adet-can)+1, "seferde sayıyı buldun..")
                break
            else:
                if sensec<sectim:
                    print("Hayır, Seçtiğim sayı daha büyük bir sayı..")
                else:
                    print("Hayır, Seçtiğim sayı daha küçük bir sayı..")
                can-=1

                if adet==0:
                    print("=>  Game Over..")
                    print(f"Seçtiğim sayı {sectim} idi..")
                    break

    elif zorluk=="b":
        print("Orta Mod Seçildi.. ")
        print("20 Can Hakkınız Var..\n")
        adet=20
        can=adet
        while True:
            print(can, end=" -> ")
            sensec=int(input("Sayıyı tahmin et: "))
            if sensec==sectim:
                print("👌 Tebrikler..", (adet-can)+1, "seferde sayıyı buldun..")
                break
            else:
                if sensec<sectim:
                    print("Hayır, Seçtiğim sayı daha büyük bir sayı..")
                else:
                    print("Hayır, Seçtiğim sayı daha küçük bir sayı..")
                can-=1

                if adet==0:
                    print("=>  Game Over..")
                    print(f"Seçtiğim sayı {sectim} idi..")
                    break

    elif zorluk=="c":
        print("Zor Mod Seçildi.. ")
        print("10 Can Hakkınız Var..\n")
        adet=10
        can=adet
        while True:
            print(can, end="- ")
            sensec=int(input("-->  Sayıyı tahmin et: "))
            if sensec==sectim:
                print("👌 Tebrikler..", (adet-can)+1, "seferde sayıyı buldun..")
                break
            else:
                if sensec<sectim:
                    print("Hayır, Seçtiğim sayı daha büyük bir sayı..")
                else:
                    print("Hayır, Seçtiğim sayı daha küçük bir sayı..")
                can-=1

                if can==0:
                    print("=>😒 Game Over..")
                    print(f"Seçtiğim sayı {sectim} idi..")
                    break

    