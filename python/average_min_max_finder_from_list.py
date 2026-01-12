notlar = [15, 10, 30, 20, 51, 40]
toplam = 0
adet = 0
en_buyuk = None
en_kucuk = None
print("Geçerli Sayılar:")
for eleman in notlar:
    if eleman > 50:
        toplam += eleman
        adet += 1
        print(f"{eleman}")
        if en_buyuk is None or eleman > en_buyuk:
            en_buyuk = eleman
        if en_kucuk is None or eleman < en_kucuk:
            en_kucuk = eleman
if adet >0:
    ortalama = toplam / adet
    print(f"Ortalama: {ortalama}")
    print(f"En büyük sayı: {en_buyuk}")
    print(f"En küçük sayı: {en_kucuk}")
else:
    print("Hiçbir geçerli sayı bulunamamıştır \"50 üstü sayı yok\"")
