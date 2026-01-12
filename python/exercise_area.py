#Girilen string değeri düzelten kod

# text = input("Bir yazı yazın: ")
# result = text.lower()
# result2 = result.strip(" ")
# result3 = result2.replace(" ","_")
# print(result3)

#Mail adresinin doğruluğunu kontrol eden kod

# text = input("Lütfen email giriniz: ")
# x = "@"
# if x in text:
#     if text.endswith(".com") or text.endswith(".net"):
#         print(f"{text} mail adresi geçerli bir mail adresidir.")
#     else:
#         print("Girdiğiniz mail adresi, .com veya .net ile bitmelidir.")
# else:
#     print("Girdiğiniz mail adresi biçimi hatalıdır.")

# İsim, İkinci İsim ve Soyisim Ayırıcı

# text = input("İsim Soyisim Giriniz: ")
# text2 = text.split(" ")
# kelime_adet = 0
# ad = text2[0]
# for eleman in text2:
#     kelime_adet += 1
# if kelime_adet > 3:
#     print("Lütfen en fazla 2 isim giriniz.")
# else:
#     if kelime_adet > 2:
#         ikinci_ad = text2[1]
#         soyad = text2[2]
#         print(f"Ad: {ad}\nİkinci Ad: {ikinci_ad}\nSoyad: {soyad}")
#     if kelime_adet == 2:
#         soyad_fix = text2[1]
#         print(f"Ad: {ad}\nSoyad: {soyad_fix}")
#     if kelime_adet <= 1:
#         print("Lütfen hem isminizi hemde soyadınızı girin.")

#Şifre kontrol eden kod
# sifre = input("Lütfen şifre giriniz: ")
# sifre_uzunluk = len(sifre)
# sifre_alnum_mu = sifre.isalnum()
# sifre_en_az_bir_buyuk_harf = sifre.islower()
# sifre_karakter_listesi = list(sifre)
# sifre_basi_kontrol = sifre_karakter_listesi[0]
# sifre_basi_kontrol2 = sifre_basi_kontrol.isalpha()
# sifre_rakam_kontrol = sifre.isalpha()
# if sifre_uzunluk >= 8:
#     if sifre_alnum_mu:
#         if sifre_basi_kontrol2 == False:
#             print("Lütfen şifreyi bir harf ile başlatın.")
#         else:
#             if sifre_en_az_bir_buyuk_harf:
#                 print("Şifrenizde en az bir adet büyük harf olmalıdır.")
#             else:
#                 if sifre_rakam_kontrol:
#                     print("Şifrenizde en az bir rakam olmalıdır.")
#                 else:
#                     print("Şifre Güçlü")       
#     else:
#         print("Şifreniz geçersiz karakter içermektedir.")
# else:
#     print("Şifre en az 8 karakter içermelidir.")