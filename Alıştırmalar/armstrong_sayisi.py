sayı = input("Sayı: ")
basamak_sayısı = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while(gecici_sayı > 0):
    basamak = gecici_sayı % 10
    toplam += basamak ** basamak_sayısı
    gecici_sayı //= 10

if(toplam == sayı):
    print(sayı, ", bir Armstrong Sayısıdır.")
else:
    print(sayı, ", bir Armstrong Sayısı değildir.")