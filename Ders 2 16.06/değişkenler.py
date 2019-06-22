#print("hello world")
#print(1)

#Deðiþken Tanýmlama kurallari
#1) degisken ismi sayi ile baslayamaz
#2) degisken 2 kelimeden olusamaz (ayrik olamaz)
#3) degisken ismi icerisinde sadece izin verilen ozel karakterler kullanilabilir(_)
#4) degisken tanimlamasi yapilirken, kesinlikle tanimli kelimeler kullanilamaz
#5) degisken ismi icerisinde turkce krakter kullanilmaz

benim_adim = "derin"
firstName = 'derin'


# int, string, float

sayi = 5 # int tam sayi veri tipi
print(sayi)
print(type(sayi))

ondalikli_sayi = 4.6
print(ondalikli_sayi)
print(type(ondalikli_sayi))


isim = "derin"
soyisim = 'bilgin'

print(isim)
print(soyisim)
print(isim + " "+ soyisim)
print(isim, " ", soyisim)

fullname = isim + " " + soyisim

print("kullanici adi : ",fullname)

x = True
y = False

print(x)
print(y)

# \n bir alt satira gecmek
print((fullname +"\n")*5)


print(type(fullname))


##################################################################################


##Convert :  elinizdeki bir veri tipini baska bir veri tipine cevirmek icin kullanilir

#int() tam sayi veri tiplerine cevirlir
#str()string degere ( metinsel) cevirir
#float() ondalikli sayi tipine cevirir
#chr() verdiginiz sayisal degerin, karakter degerini temsil eder.
#ord() verdiginiz karakter degerin asli kod degerini teslim eder

sayi1 = input("lutfen bir sayi giriniz : ")
sayi2 = input("lutfen bir sayi giriniz : ")


sonuc = sayi1 + sayi2
print(sonuc)

result = float(sayi1) + int(sayi2)
print(result)

#print("islem sonucu : " + result)
print("islem sonucu :" , result)
print(type(result))

print("islem sonucu : "+str(result))

print("""
      bilge
      adam
      besiktas""")

print("bilge adam \"besiktas\" istabul\n\
yazilim dersleri\
 phyton ogreniyoruz")


#bilge adam "besiktas" istanbul

#"bilge adam"
#'bilge adam'
#""" bilge adam """

print(chr(65))
print(chr(97))

print(ord("A"))
print(ord("a"))
print(ord("Z"))
print(ord("z"))























