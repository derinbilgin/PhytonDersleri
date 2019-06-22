# Programcı hataları(Error)
# Program Kusurları (Bug)
# Istisnalar        (Exceptiion)
# Mantıksal Hatalar




try:
    telefon_numarasi = input("lütfen telefon numaranizi giriniz : ")
# Telefon numarası veri tabanına kaydedildi
    print("Telefon numaranız :",int(telefon_numaraı))
except ValueError:
    print("İşlem Hatası")
    print("Lütfen geçerli bir sayı giriniz")
except ZeroDivisionError:
    print("işlem hatası")
    print("sıfıra bölünme hatası")


