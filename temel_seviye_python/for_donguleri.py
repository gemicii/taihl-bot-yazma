# öğrenci isimlerinden oluşan liste oluşturalım
ogrenciler = ["Eren", "Mustafa", "Zeynep"]

# her öğrencinin adını ekrana yazdıralım
# ÖRNEK: öğrencinin adı:eren
for ogrenci in ogrenciler:
    print(f"Öğrencinin adı: {ogrenci}")

# içinde ikili sayılardan oluşan tuple verilerinin olduğu bir liste oluşturalım
sayilar = [(1,2),(3,4),(5,6)]
for a,b in sayilar:
    print(f"1.sayı: {a},2. sayı: {b} ")

okul = "Sancaktepe Teknoloji Anadolu İmam Hatip Lisesi"
kelimeler = okul.split()
print(kelimeler)

for kelime in okul.split():
    print(kelime)

# öğrencilerin yer aldığı bir dict tipi oluşturalım
ogrenciler = {
    1: {
        "ad": "Eren",
        "soyad": "Özdal",
        "cinsiyet": True,
        "dersler": ["Türkçe", "Matematik", "Hayat Bilgisi"]
    },
    45: {
        "ad": "Zeynep",
        "soyad": "Özdal",
        "cinsiyet": False,
        "dersler": ["Görsel Sanatlar", "Matematik", "Fen Bilimleri"]
    }
}

# öğrencilerin numaralarını ve adlarını yazdıralım
for no, ogrenci in ogrenciler.items():
    print(f"{no} numaralı örenci: {ogrenci['ad']}")