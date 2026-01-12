ad = input("Lütfen Adınızı Girin: ")
vize_notu = float(input("Lütfen Vize Notunuzu Girin: "))
if 0 <= vize_notu <= 100:
    final_notu = float(input("Lütfen Final Notunuzu Girin: "))
    if 50 <= final_notu <= 100:
        ortalama = vize_notu * 0.4 + final_notu * 0.6
        if 60 <= ortalama <= 100:
            print(f"Tebrikler {ad}, geçtiniz. Ortalamanız: {ortalama:.2f}")
        else:
            print(f"Maalesef kaldınız. Ortalamanız: {ortalama:.2f}")
    elif 0 <= final_notu < 50:
        print("Ortalamanızın hesaplanması için Final Notunuzun 50 veya üstü olması gerekmektedir.")
    else:
        print("Geçersiz Final Notu.")
else:
  print("Geçersiz Vize Notu.")