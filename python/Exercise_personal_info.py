ad = (input("Adınızı Girin: "))
yas = int(input("Yaşınızı Girin: "))
boy = float(input("Boyunuzu Girin: "))
ogrenci_bilgi = (input("Öğrenci Misiniz?(Evet/Hayır): ")).lower() #burada dış kalıpta bool etiketi kullanınca 
#sıkıntı yaşıyorsun dikkat et.
d1 = type(ad).__name__
d2 = type(yas).__name__
d3 = type(boy).__name__
if ogrenci_bilgi == "evet":
    print(f"Ad: {ad} {d1}\n Yaş: {yas} {d2}\n Boy: {boy} {d3}\n Öğrenci: Evet")
elif ogrenci_bilgi == "hayır" or ogrenci_bilgi == "hayir":
    print(f"Ad: {ad} {d1}\n Yaş: {yas} {d2}\n Boy: {boy} {d3}\n Öğrenci: Hayır")
else:
    print(f"Ad: {ad} {d1}\n Yaş: {yas} {d2}\n Boy: {boy} {d3}\n Öğrenci: Geçersiz Öğrenci Bilgisi Girildi.")

