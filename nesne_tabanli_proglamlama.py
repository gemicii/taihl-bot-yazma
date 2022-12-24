"""
Nesne tabanlı programlama ile ortak niteliklere ve davranış şekillerine sahip
gruplar tanımlamamızı sağlar. (?)
ÖRNEK:
--------
Öğrenci bilgilerini tutan bir veritabanımız var. Veri tabanındaki her satır bir
öğrenciyi temsil ediyor.
Öğrenci
- Okul
- No
- Ad
- Soyad
- Doğum Yılı
...
Yukarıdaki örnek öğrenci bilgilerine yazılımda karşılık gelen nesne (class)
oluşturalım. Bu öğrenci nesnesinin okul, no, ad, soyad, dogum_yili
özellikleri (attributes) olsun. Ayrıca doğum tarihinden otomatik yaş hesaplayan
bir davranışı (method) olsun.
"""
from datetime import datetime

# Öğrenci nesnesine ait sınıfı tanımlayalım
#   ⚪ Okul her öğrenciye göre değişmeyeceği senaryosu üzerinden; okul
#       değişkenini sınıf özelliği olarak ekleyelim
#   ⚪ No, Ad, Soyad ve Doğum Yılı her öğrenciye göre değişeceği örnek
#       özelliği tanımlayacağız
#   ⚪ Öğrencinin adını ve soyadını birleştirip döndüren metot ekleyelim
#   ⚪ Öğrencinin yaşını hesaplayıp döndüren metot ekleyelim
class Ogrenci:
   okul = "Sancaktepe Teknoloji Anadolu İmam Hatip Lisesi"

   def __init__(self,ad,soyad,no,d_tarih):
       self.name = ad
       self.surname = soyad
       self.number = no
       self.birthday = d_tarih

   def tam_ad(self):
      return f"{self.name} {self.surname}"

   def yas(self):

       bu_yil = datetime.datetime.today().year
       return bu_yil - self.birthday

       yas = bu_yil - self.birthday
       return yas

# ayrı ayrı öğrenci nesneleri oluşturalım
ahmet = Ogrenci("Ahmet","Yılmaz",94,2052)
mehmet =Ogrenci("Mehmet","Demir",87,1992)
print(type(ahmet))
print(ahmet.okul)
print(ahmet.name)
print(mehmet.okul)
print(mehmet.name)
print(ahmet.tam_ad())
print(mehmet.tam_ad())
print(ahmet.yas())
print(mehmet.yas())