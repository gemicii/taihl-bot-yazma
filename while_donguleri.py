# 0 dan 100 e kadar olan tek ve çift sayıları yazdıralım
# import xlrd
#
# sayi = 0
# while sayi < 100:
#
#     if sayi % 2 == 0:
#         print(f"{sayi} çift sayıdır")
#     else:
#         print(f"{sayi} tek sayıdır")
#     sayi += 1
import xlrd

# worldcupplayers excel dosyasındaki verileri okuyalım
# hangi oyuncuların kaçıncı dakikada gol attıklarına bakalım

# import xlrd
# excel okuma modülünü içeri aktaralım

# excel dosyasını açalım
ck = xlrd.open_workbook("veriler/WorldCupPlayers.xls")

# excel çalışma sayfasını açalım
cs = ck.sheet_by_index(0)

# toplam satır ve sütun sayılarını alalım
satir_sayisi = cs.nrows
sutun_sayisi = cs.ncols
print(f"satır sayısı: {satir_sayisi}")
print(f"sütun sayısı: {satir_sayisi}")

# ilk başlık satırlarını okuyalım
a1 = cs.cell(0, 0)
print(a1)

# tüm futbolcuların isimlerini yazdıralım
satir = 1 #başlıkları es geçmek için 1. indeksten başlıyoruz
while satir < satir_sayisi:
    futbolcu = cs.cell_value(satir,6)

    # if futbolcu.startswith("R"):
    #
    #     print(f"futbolcu: {futbolcu}")



    # bir olay yaşamış futbolcuları yazdıralım
    olay = cs.cell_value(satir,8)
    if olay != "":
        print(f"futbolcu: {futbolcu} - olay: {olay}")
    satir += 1
