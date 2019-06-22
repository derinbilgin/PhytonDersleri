try:
    sayi_bir = int(input("lütfen birinci sayiyi giriniz : "))
    sayi_iki = int(input("lütfen ikinci sayiyy giriniz : "))

    toplam = sayi_bir + sayi_iki
    fark = sayi_bir - sayi_iki
    bolum = sayi_bir / sayi_iki
    carpim = sayi_bir * sayi_iki

    print("sayilarin toplami :",toplam,
          "\nSayıların Farkı :",fark,
          "\nSayıların bolumu :",bolum,
          "\nSayıların carpımı :",carpim )

except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("zero division error hatası")
except FileExistsError:
    print("file exists error")
except:
    print("hata mesajı")

