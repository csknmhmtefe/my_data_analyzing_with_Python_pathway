# bir string ifadede bulunan kelime sayısını bulan program.
text = input("Lütfen kelime sayısını hesaplamak için yazı yazınız: ")
result = text.split(" ")
myList = result
adet = 0
for eleman in myList:
     if text.isalnum:
      adet += 1
     else:
        print("Lütfen alfanümerik değer girin.")
print(f"Girilen string ifadede {adet} kelime vardır.")
