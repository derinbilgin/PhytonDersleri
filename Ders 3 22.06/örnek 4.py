try:
    sayi_bir = int(input("lütfen bölünecek olan sayıyı giriniz : "))
    sayi_iki = int(input("lütfen bölecek olan sayıyı griniz : "))
except ValueError as exp:
    print("İşlem Hatası :",exp)
else:
    try:
        print(sayi_bir/sayi_iki)
    except ZeroDivisionError:
        print("Sayı sıfır değerine bölünemez!")