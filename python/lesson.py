print("Karakteri Hexadecimal'e Çevirme Uygulaması")
karakter = input(str("Bir karakter girin: "))
hexadecimal_cikti = (f'{karakter}'.encode("utf-8"))
print(f"Karakterin hexadecimal karşılığı: {hexadecimal_cikti}")