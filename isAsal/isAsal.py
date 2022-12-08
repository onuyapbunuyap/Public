isAsal = int(input("1'den büyük bir tam sayı giriniz: "))

if isAsal <= 1:
    print("Geçersiz sayı!")
else:
    for x in range(2,isAsal):
        if isAsal % x == 0:
            print(isAsal,"asal değildir.")
            break
    else:
        print(isAsal,"asaldır.")