#Listedeki pozitif sayıların toplamını veren kod
# sayilar = [10, -5, 20, -3, 0, 15]
# toplam = 0
# for eleman in sayilar:
#     if eleman > 0:
#         toplam += eleman
# print(f"Pozitif sayıların toplamı: {toplam}")

#Bir listede en büyük sayıyı bulan kod
# sayilar = [3, 7, 2, 9, 5]
# en_buyuk = None
# for eleman in sayilar:
#     if en_buyuk is None or eleman > en_buyuk:
#         en_buyuk = eleman
# print(f"En büyük sayı: {en_buyuk}")

#Listedeki en büyük ve en küçük sayıyı veren kod
# sayilar = [8, 3, 12, 1, 6]
# en_buyuk = None
# en_kucuk = None
# for eleman in sayilar:
#     if en_buyuk is None or eleman > en_buyuk:
#         en_buyuk = eleman
#     if en_kucuk is None or eleman < en_kucuk:
#         en_kucuk = eleman
# print(f"En küçük: {en_kucuk}\nEn büyük: {en_buyuk}")

#Listedeki çift sayıları toplayan kod
# sayilar = [3, 6, 9, 12, 15, 18]
# cift_toplam = 0
# for eleman in sayilar:
#     if eleman %2 == 0:
#         cift_toplam += eleman
# print(f"Çift sayılar toplamı: {cift_toplam}")

#Listedeki pozitif olarak en büyük olan sayıyı veren kod
# sayilar = [-10, -3, 0, 7, 4, -1]
# pozitif_en_buyuk_sayi = None
# for eleman in sayilar:
#     if eleman > 0:
#         if pozitif_en_buyuk_sayi is None or eleman > pozitif_en_buyuk_sayi:
#             pozitif_en_buyuk_sayi = eleman
# print(f"Pozitif en büyük sayı: {pozitif_en_buyuk_sayi}")

#Listedeki pozitif sayıların min,max olan değerlerini ve pozitif sayıların ortalamasını alan kod
# sayilar = [5, -2, 10, 0, 3, -8, 20]
# en_kucuk = None
# en_buyuk = None
# toplam = 0
# adet = 0
# for eleman in sayilar:
#     if eleman > 0:
#         toplam += eleman
#         adet += 1
#         if en_buyuk is None or eleman > en_buyuk:
#             en_buyuk = eleman
#         if en_kucuk is None or eleman < en_kucuk:
#             en_kucuk = eleman
            
# if adet > 0:
#     ortalama = toplam / adet
#     print(f"En büyük pozitif sayı: {en_buyuk}\nEn küçük pozitif sayı: {en_kucuk}\nPozitif sayıların ortalaması: {ortalama}")
# else:
#     print("Listede pozitif sayı yok.")
