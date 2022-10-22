# boş bir liste tanımlayalım: []
liste = []
print(type(list))

okul = "Sancaktepe Teknoloji Anadolu İmam Hatip Lisesi"
kelimeler = okul.split()
print(kelimeler)

# belirli sıradaki kelimeleri yazdıralım
print(kelimeler[0])
print(kelimeler[1])
print(kelimeler[2])
print(kelimeler[3])
print(kelimeler[4])
print(kelimeler[5])
print(kelimeler[-2])

ad = "Alperen GEMİCİ"
print(ad[9])

# listeler içerisinde farklı türden veriler olabilir
liste = [1,12.3, "python", True,[1,2,3]]
print(liste[-3])

# iki listeyi birleştirme
liste2 = [1,2,3]
liste3 = [4,5,6]
liste4 = liste2 + liste3
liste5 = liste3 + liste2
print(liste4)
print(liste5)
