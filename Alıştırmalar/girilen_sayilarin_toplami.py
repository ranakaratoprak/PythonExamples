toplam = 0

while True:
    sayı = input("Sayı: ")
    if(sayı == "q"):
        print("Programdan çıkılıyor...")
        break
    sayı = int(sayı)
    toplam += sayı
    print("Girdiğiniz sayıların toplamı: ", toplam)