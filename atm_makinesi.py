print("""****************************
Atm Makinesine Hoşgeldiniz
****************************""")

print("""

****************************
1. Bakiye Sorgulama
2. Para Yatırma
3. Para çekme

Programdan 'q' tuşu ile çıkabilirsiniz.
****************************""")

bakiye = 1000

while True :
    işlem =input("Yapacağnız işlemi Seçin:")

    if  (işlem == "q"):
        print("Yine Bekleriz...")
        break

    elif (işlem == "1") :
        print("Bakiyeniz:{} TL dir.".format(bakiye))

    elif (işlem == "2") :
        miktar =int(input("Kaç TL Yatırmak İstiyorsunuz :"))

        bakiye +=miktar

    elif (işlem == "3") :
        miktar1 = int(input("Kaç TL Çekmek İstiyorsunuz :"))

        if (miktar1 > bakiye) :
            print("Bu Kadar Para Yok !!!")

            continue
        bakiye -= miktar1
        print("Bakiyeniz:{} TL dir.".format(bakiye))
    else:
        print("Lütfen Geçerli Bir İŞlem Giriniz")





