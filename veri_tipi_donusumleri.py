# Kullanıcıdan 2 sayı alıp toplama işlemi yapan program

x = birinci_sayi = 18
y = ikinci_sayi = 29
print(x+y)

x = float(input("1._sayiyi_girin"))
y = float(input("2._sayiyi_girin"))
print(x*y)

# TİP DÖNÜŞTÜRME
# int'ten float'a
print(float(x))

# float'tan int'e
print(int(x))
# bool'dan str'ye
print(sinav_basarili_mi) #bool  olarak true
print(type(str(sinav_basarili_mi))) #str olarak "true"

# int'ten str'ye
print(str(x))

# str'den int'e
print(int(ad)) # metin int'e dönüşmez
sayi = "36"
print(int(sayi)) #sayı değeri taşıyan str dönüştürülebilir