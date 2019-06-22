# Hata Mesajı

try:
    sayi = input("Lütfen sadece sayisal veri giriniz : ")
    print("gelen sayı",sayi)
    sayi = sayi / 0
    print("işlem sonu")

except ValueError as ex:
    print("ValueError")
    print("sistem hata mesajı",ex)
except ZeroDivisionError as ex:
    print("ZeroDivisionError")
    print("sistem hata mesajı",ex)
except Exception as ex:
    print("except")
    print("sistem hata mesajı",ex)
