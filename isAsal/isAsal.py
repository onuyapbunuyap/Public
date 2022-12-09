isAsal = input("1'den büyük bir tam sayı giriniz: ")
try:
    isAsal = int(isAsal)
except:
    print("Lütfen bir sayı giriniz.")
else:
    if int(isAsal) <= 1:
        print("Geçersiz sayı!")
    else:
        for x in range(2,int(isAsal)):
            if int(isAsal) % x == 0:
                print(int(isAsal),"asal değildir.")
                break
        else:
            print(int(isAsal),"asaldır.")
