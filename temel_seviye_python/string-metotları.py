okul = "Sancaktepe teknoloji anadolu imam hatip lisesi"

# Tüm karakterleri büyük harf yapalım: upper()
print(okul.upper())

# Tüm karakterleri küçük harf yapalım: lower()
print(okul.lower())

# tüm kelimenin ilk harfini büyük yapalım: title()
print(okul.title())

# karakter dizisinin ilk karakterini büyük,
# diğer karakterlerini küçük harf yapalım: capitalize()
print(okul.capitalize())

# belirli bir ifadenin kaç defa yer aldığını bulalım: count()
print(okul.count("a"))

makale = "Teknoloji sayesinde bilgi alışverişi kolaylaştı. Dünyanın öteki ucunda gerçekleşen bir olaydan anında haberimiz oluyor"
"Hayatı kolaylaştırır ve pratikleştirir. Evinizde internetten alışveriş"
"yapabilirsiniz, kilometrelerce uzaklıktaki bir olayı anlık olarak izleyebilirsiniz, 2 dakikada apartmanın 10. katına çıkabilirsiniz."

print(makale.count("e"))

# soldaki ve sağdaki boşluk karakterlerini temizleyelim: strip()
ad = input("Adınız: ")
print(ad + "|")
print(ad.strip() + "|")

# soldaki ve sağdaki belirli karakterleri temizleyelim: strip("ifade")
urun_kodu = "HEP20221022"
print(urun_kodu.strip("HEP"))

# soldaki boşluk veya belirli ifadeyi temizleyelim: rstrip()
print(ad + "|") # adı boşlukla gönderelim
print(ad.rstrip()+ "|")
print(urun_kodu.rstrip("HEP"))

# karakter dizisini bölelim: split()
print(okul.split())
print(makale.split())

# böldüğümüz ve listeye dönüşen ifadeleri birleştirelim: join()
kelimeler = okul.split()
print(kelimeler)
print("---".join(kelimeler))

# ortalayaıp çıktı verme: center()
print("Alperen".center(25,"-"))