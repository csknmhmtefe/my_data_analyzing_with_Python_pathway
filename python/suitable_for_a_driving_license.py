yas = int(input("Yaşınızı Girin: "))
if 120 > yas >= 18:
    if yas <= 64:
        print(f"Yaş: {yas}\nKategori: Yetişkin\nEhliyet Durumu: Alabilir")
    else:
        print(f"Yaş: {yas}\nKategori: Emekli\nEhliyet Durumu: Alabilir")
elif yas < 0:
    print("Hatalı Yaş")
elif yas >= 120:
    print("Gerçekçi bir yaş giriniz") 
elif 12 < yas < 18:
    print(f"Yaş: {yas}\nKategori: Genç\nEhliyet Durumu: Alamaz")
elif 0 <= yas <= 12:
    print(f"Yaş: {yas}\nKategori: Çocuk\nEhliyet Durumu: Alamaz")
else:
    print("Beklenmeyen bir durum oluştu")