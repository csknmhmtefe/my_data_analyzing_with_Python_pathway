                                                            # STRING VERİ TÜRÜ

# TIRNAK SORUNU
# string bir değişkene atadığımız değer için, çift tırnak veya tek tırnaklar arasına yazdığımız metinde, farklı
#tırnak işaret kullanmamız gerekir. örneğin "Hello it's efe" yazarken içeride tek tırnak kullandım. çift tırnak
#kullansaydım syntax hatası alacaktım. hata almak istemiyorsam, 'Hello it\'s Efe' bu şekilde tüm tırnakları
#tek tırnak olarak kullanmak istiyorsam, içeride kullandığım tek tırnak veya tırnakların önüne kaçış karakteri
#yani "\" koymam gerekir.
#text = "onun lakabı ¨\"koca oğlan\"."

# BİRDEN FAZLA SATIR
# string bir değeri yazarken birden fazla satır kullanmak istersek, üç tırnak """ ile başlayıp üç tırnak """
#ile kapatarak yapabiliriz. 
# 
#***Alternatif olarak 3 tane tek tırnakta kullanılabilir.***
# 
#print ("""Merhaba bu bir deneme yazısı.
#benim adım efe
#23 yaşındayım
#boyum 1.86
#kilom 102 """)

# INDEX NEDİR?
# listelerde index her bir string değer için ayrı olurken, direkt bir string değerde her karakter bir indekse tekabul
#eder. index sayımı 0'dan başlar.
#liste örneği:
#cars = ["bmw","skoda","nissan","toyota"]
#print(cars[0]) # bu kod 4 araç ismi yazan listeden 0 indeksli olan yani "bmw" olanı çıktı yazar.
#string değer örneği:
#text = "merhaba dünya"
#print(text[5]) # bu kod 0'dan başlayarak saydığımızda 5. indexte olan b harfini çıktı verecektir.

# STRING İFADELERDE LEN METODU
# bir string ifadenin uzunluğunu öğrenmek için len metodunu kullanabiliriz.
#örneği:
#text = "Mehmet Efe Coşkun"
#print(len(text)) 
#bu kod çıktıda 17 rakamını getirecektir. index sırasına göre değil normal sayıma göre sonuç verir.

# IN METODU İLE BİR STRING DEĞERDE BELİRLİ BİR DEĞERİ ARAMAK
# in metodunu kullanarak bir string değerin içinde bir string arayabiliriz.
#örneği:
#text = "Fenerbahçe 2026 senesinde şampiyon!"
#search = input("İçinde aramak istediğiniz harf'i/rakam'ı girin: ")
#print(search in text)
#if search in text:
#print("Evet, aradığınız /harf/kelime/rakam/sayı cümlede mevcut.")
#else:
#print("Hayır,maalesef aradığınız kelime cümlede mevcut değil.")
#eğer string ifade, sorguladığımız değerin içinde varsa True çıktısı alacağız. Yok ise False çıktısı alacağız.

#NOT IN METODU
# in metodunun zıttı olan bu metod, bir string değerde, bir string değerin olmadığını ifade etmek için kullanılabilir.
#örneği
#text = "Süper Lig Takımları"
#print("         GOOGLE")
#search = input("Arama yapabilirsiniz: ")
#if search not in text:
#print ("\"Süper Lig Takımları\" yazarak aratma yapabilirsiniz.")
#else:
#print ("Alanyaspor\nAntalyaspor\nBaşakşehir\nBeşiktaş\nEyüpspor\nFenerbahçe\nGalatasaray\nGaziantep\nGençlerbirliği\nGöztepe\nFatih Karagümrük\nKasımpaşa\nKayserispor\nKocaelispor\nKonyaspor\nRizespor\nSamsunspor\nTrabzonspor")

#BİR STRING DEĞERİ DİLİMLEMEK
 #bir string değeri dilimlemek için [:] kullanılabilir.
#örneği
#text = "Deneme yazısı"
#print(text[1:5]) #bu kod çıktıda bize index numarası olarak 1 ve 5 arasında ki(5 hariç) string değeri verecektir.
##bu kodda vereceği yazı: "enem"dir. ilk değer girilmezse, varsayılan olarak 0 sayılır. ikinci değer girilmezse,
#ilk değerden başlayıp string değerin sonuna kadar dilimle demiş oluruz.

 #STRING İFADELERİ BİRLEŞTİRME
# direkt + operatörü ile string ifadeleri toplama işlemi.
#örneği:
#text1 = "yazı1"
#text2 = "yazı2"
#result = text1 + text2
#print(result)

#MODIFY STRİNGS / STRINGLERDE DEĞİŞİM
# Metodlar:
#örneklerle:
#text = "Python is going well"

#print(text.upper()) #upper case - verilen string değerdeki tüm harfleri büyük yapar.

#print(text.lower()) #lower case - verilen string değerdeki tüm harfleri küçük yapar.

#print(text.strip()) #strip - verilen string değerin başındaki ve sonundaki whitespace(boşluk karakterleri) temizler.
#EK BİLGİ** strip metoduna istediğimiz parametreyi vererek, silinmesini istediğimiz karakteri belirleriz.

#print(text.replace("P","T")) #replace - belirtilen string değer için, ilk parametredeki string değeri, ikinci
#parametredeki string değer ile değiştirir. Örnekteki kodda, "P" harfi yerine "T" yazılır.

#text = "Hello, Python"
#result = text.split(",")
#print(result) # split - belirtilen string ifadeyi tespit edince string ifadeyi böler. Örnekte ['Hello', 'Python']
#çıktısı alınacaktır.

# STRING KAÇIŞ KARAKTERLERİ
# çift tırnaklar içinde çift tırnak veya tek tırnaklar içinde tek tırnak kullanmak istersek, çift veya tek
#tırnağın öncesine \ koyarak kullanabiliriz. Örnek: "Hello \"Python\"."

# BACKSLASHI kaçış karakteri görevi olmadan normal şekilde kullanmak istersek \\ çift kullanmamız gerekir.

# ALT SATIRA GEÇİRME KAÇIŞ KARAKTERİ \n
# \n kullanarak kodun çıktıda bir alt satıra geçmesini sağlayabiliriz.

# İMLECİ BAŞA ALDIRIP YAZDIRMA KAÇIŞ KARAKTERİ \r "reset"
# \r kullandığımız zaman kod imleci başa alıp yazmaya başlar. Örnek: "Hello\rpy" yazdığımız zaman, pyllo çıktısı gelir.

# BİR TAB BOŞLUK BIRAKMA KAÇIŞ KARAKTERİ \t "TAB"
# \t kullanarak çıktımızda bir tab boşluk bırakılmasını sağlayabiliriz. "Hello,\tPython" çıktıda "Hello,    Python".

# İMLECİ BİR KARAKTER GERİ ALIP YAZDIRMA KAÇIŞ KARAKTERİ \b "backspace"
# \b kullandığımızda string ifadede imleci bir sola alıp yazmaya devam eder."Hello\bPython" bize "HellPython" çıktısı verir.

# OCTAL VE HEXADECIMAL SAYI SİSTEMİ İLE YAZDIRMA KAÇIŞ KARAKTERLERİ 
# sadece \ kullanarak ardından ASCII tablosundan bir karaktere karşılık oktal veya hexadecimal sayı yazarak,
#istediğimiz string ifadeye ulaşabiliriz. Octal olarak: "\120\171\164\150\157\156" çıktıda "Python" yazdırır.
#istersek Python yazısını, her bir harfinin Hexadecimal sayısal karşılığını \x ile yazarakta elde edebiliriz.
#EK BİLGİ ** octal sayılar 0-8 arası direkt gösterilirken, hexadecimal 9'dan sonra A B C D E F olarak 15'e kadar ifade edilir.
#örneğin decimal karşılığı 111 olan o harfini 16ya bölüp bulduğumuz 615 sayısı hexadecimal olarak
#6 + 15 yani 6f olarak ifade edilir.
#UNUTMA! Hexadecimal olarak \ kullanmak istediğimizde \xsayı şeklinde kullanmamız gerek.

#STRING FORMATLAMA "format metodu"
# format metodunu kullanarak, bir string içinde {} şeklinde belirttiğimiz alanlara, değişkenler atayabiliriz.
#örnek:
#age = 23
#name = "Mehmet Efe"
#print("Benim adım {} ve ben {} yaşındayım.".format(name,age))
#EK BİLGİ* süslü parantez içine index numarası yazarak istediğimiz değerin getirilmesini sağlayabiliriz.
#örnek 
#age = 23
#name = "Efe"
#text = "Benim adım {1}, ben {0} yaşındayım.".format(age,name)
#print(text)
#**ÖNEMLİ KISIM**
# PLACEHOLDER'I YÖNETMEK İÇİN KOMUTLAR.
# format metodunda placeholder kısmını istediğimiz şekilde şekillendirebiliriz.
#{:<10} örneğin bu kullanımda placeholder bulunduğu konuma 10 karakter boşluk bırakılır. bu placheolder için,
#format metodundan tanımlanan parametre ise, 10 karakterin en solda olanına yerleştirilir. 
#text = "We do not have {} children."
#print(text.format(7)) #burada çıktı We do not have 7         children. olacaktır.
#{:<10} bu ifadede ":<" sola hizalanacağını, "10" ise 10 karakter boşluk bırakıkacağını belirtir.
#{:>10} burada ise format metoduna tanımlanan parametreyi sağa hizala ve 10 karakter boşluk bırak deniyor.
#{:^10} burada ise 10 birimlik bıraktığı boş alanda, format metoduna atanan parametreyi ortaya hizala demiş olur.
#{:=10} burada ise 10 birimlik bıraktığı boş alanda, format metoduna atanan parametrede matematiksel olan ifadeyi,
#en sol kısma hizalar. Örneğin parametrede text.format(-7) var ise "-" yi en sola hizalar araya 10 karakter boşluk
#koyar ve 7 yi yazar. Ek bilgi: aynı işlem parametrede + olunca gösterilmez. +7 olsaydı, sadece 10 karakter ve 7 yazardı.
#{:+} burada ise {:=10}'dan farklı olarak, özellikle - ve + değerleri belirtir. yani parametre olarak 7 atandı
#ise +7, -7 atandı ise -7 olarak çıktıya yazar.
#{:-} burada ise sadece - var ise gösterir + yı ekstra olarak göstermez text.format(-7,7) çıktısı -7 ve 7 olarak çıkar
#{: } bu kullanımda parametre olarak - değer verilen placeholderlarda değişim olmaz iken, + olan değerler önüne
#bir adet boşluk alır.
#{:,} bu kullanım aldığımı parametreyi her binlikte , atar. örneğin parametre 1000000000 ise çıktı 1,000,000,000 olur.
#{:_} bu kullanımda ise binlik ayırmayı , değil _ kullanarak ayırırız.
#{:b} bu kullanım format metoduna verilen parametrenin binary biçimini verir.
#{:c} bu kullanım format metoduna verilen parametrenin unicode biçimini verir.
#{:d} bu kullanım format metoduna verilen parametrenin decimal biçimini verir.
#{:e} bu kullanım format metoduna verilen parametrenin "e" bilimsel biçimini verir.
#{:E} bu kullanım format metoduna verilen parametrenin "E" bilimsel biçimini verir.
#{:.f} bu kullanımda format metoduna verilen parametrenin ondalıklı gösterilmesini sağlarız. f önüne verilen
#değer ondalık sayının ne kadarını göstereceğini belirler.varsayılan olarak 6 basamak gösterir.
#{:.F} x=float('nan') ve x=float('inf') gibi kullanımlarda nan ve inf'in büyük yazılmasını sağlar. inf "infinity"
#yani sonsuz, nan ise "not a number" yani bir sayı değil demektir.
#{:o} bu kullanım format metoduna verilen parametrenin octal biçimini verir.  
#{:x} bu kullanım format metoduna verilen parametrenin hexadecimal biçimini verir.
#{:X} bu kullanım format metoduna verilen parametrenin hexadecimal biçimini büyük harfler ile verir.
#{:n} bu kullanım format metoduna verilen parametrenin sayısal biçimini verir.
#{:%} bu kullanım format metoduna verilen parametrenin yüzdelik biçimini verir.

#F STRING KULLANARAK BİR STRING DEĞERDE FARKLI VERİ TİPLERİ DEPOLAMAK
# f string metodu kullanılarak string bir değerin içinde farklı veri tipleri kullanabiliriz.
#örnek:
#name = "efe"
#age = 23
#boy = 1.87
#kilo = 102
#print(f"İsmim {name}, yaşım {age}, boyum {boy}, ve kilom {kilo}.")
#EK BİLGİ** f string kullanırken süslü parantez içine eklediğimiz değer örneğin bir float ise, : 1f veya benzeri
#kullanım yaparak ondalıktan sonra ki rakamların ne kadar gösterileceğini belirleyebiliriz.
#örnek:
#price = 3.15678
#print(f"Price is {price:.2f} turkish lira.") #burada {price} içinde : ve .xf kullanımı ondalıktan sonra kaç rakam 
#gösterilmesini istediğimizi belirtiyor. bu kodda yuvarlayarak 3.16 gösterilecektir.

#   **STRING METODLARI**
#   -CAPITALIZE
# capitalize metodu bir string değerin ilk karakterinin büyük olmasını sağlar. örnek:
#text = "fenerbahçe bindokuzyüzyedide kuruldu."
#result = text.capitalize
#print(result) # bu kod string değerin içindeki ilk karakter olan "f"yi büyük yapacaktır.
#   -CASEFOLD
# casefold  metodu lower ile aynı işleve sahip olup, daha güçlü halidir. Yani daha fazla karakteri küçük yapabilir.
#ayrıca ASCII tablosunda olmayan bazı özel karakterleride küçültme yetkisine sahiptir. ancak lower değildir.
#**ÖNERİ mümkünse lower yerine casefold kullan. Tek eksisi, casefold lowerdan daha yavaş çalışır.
#duruma göre lower veya casefold kullanılabilir.
#   -TITLE
# title metodu, bir string değerde her kelimesinin ilk karakterini büyük harf yapar. Capitalize'dan farkı,
#sadece ilk harfi değil, her kelimenin ilk harfini büyük yapar.
#** title çalışma prensibi: alfabetik olmayan her karakterden sonra büyük harf uygular. f7f7f7 çıktısı: F7F7F7
#   -SWAPCASE
# swapcase metodu, isminden de anlaşılacağı gibi küçük harfleri büyük, büyük harfleri ise küçük yapar.
#örnek: text = "Bugün Hava Güneşli" string'i print(text.swapcase()) kullanımı sonrası "bUGÜN hAVA gÜNEŞLI" olacaktır.
#text = "Bugün Hava Güneşli"
#print(text.swapcase()) 
#   -IS LOWER / IS UPPER
# islower ve isupper metodları, bir string değerin içindeki tüm karakterlerin hepsi küçük veya büyük ise True
#döndürecektir. islower tüm karakterler küçük ise True, en az bir tanesi büyük ise False, isupper tüm karakterler 
#büyük ise True, en az bir tane küçük var ise False döndürecektir.Sorgulamak için kullanılabilir.
#   -CENTER
# center metodu, bir string değeri ortalar.
#örneği:
#text = "Hello Python"
#result = text.center(20,"*") #bu satırda center metodunun ilk paramteresi kaç karakterli bir alanda ortalamak istediğimizi
#ikinci parametre ise bu boşluklara istersek ne yazdırmak istediğmizi belirtir.
#print(result)
#   -COUNT
# count komutu verilen değişkende tanımlanan string ifade içinde belirli bir string ifadenin kaç kere olduğunu söyler.
#text = "World is world and world is world."
#print(text.count("world")) # bu kodun çıktısında 3 yazacaktır. çünkü "world" ifadesi ana stringde 3 kere geçer.
#EK BİLGİ** count metodunda 3 parametre girilebilir. ilk metod aranacak string ifadeyi belirlerken,
#2 ve 3. parametreler aramaya başlanacak ve aramanın bitirileceği indexleri belirler.
#("world",11,22) world kelimesini 11. indexten başlayıp 22. indexe kadar arar.
#   -STARTSWITH & ENDSWITH
# startswith ve endswith metodları, bir string değer metodda istenen değer ile başlıyor veya bitiyor ise True
#değerini döndürür. startswith metodu tanımladıysak başladığı ifadeye bakar, endswith metodu ise sonuna bakar.
#text = "Hello World!"
#print(text.startswith("Hello")) #true döndürür.
#print(text.endswith("World!")) #true döndürür.
#print(text.startswith("wor")) #false döndürür.
#print(text.endswith("hel!")) #false döndürür.
#EK BİLGİ** aynı şekilde 3 parametre verebiliriz bu iki metoda, 2 ve 3. parametreler arama yapılacağı index
#aralığını belirler. eğer verilen aralıkta başlıyor ise istenen karakter veya karakterler, true değeri gelir.
#   -EXPANDTABS
# expandtabs metodu tanımlandığı string ifadeye verdiğimiz parametreye göre tab boşluğu verilmesini sağlar.
#varsayılan olarak 8 değeri atanmıştır. kullanmak için string değerde istenen yerlere \t konulmalıdır.
#text = "P\ty\tt\th\to\tn"
#print(text.expandtabs())
#print(text.expandtabs(2))
#print(text.expandtabs(4))
#print(text.expandtabs(6))
#print(text.expandtabs(10))
#   -FIND
# find metodu bir string değerde istenen ifadeyi arar, bulur ise başlangıç index numarasını verir, bulamazsa -1 verir.
#text = "For manipulate the programmes of worlds, need to know python."
#print(text.find("python")) #burada 54 çıktısı alacağız
#print(text.find("earth")) #burada -1 çıktısı alacağız
#EK BİLGİ** 3 parametre verebiliriz. 2 ve 3. parametreler aramanın yapılacağı index aralığını belirler.Başlangıç-Bitiş.
#   -INDEX
# index metodu find metodu ile benzer çalışır, tek farkı bir parametreyi bulamadığı zaman -1 yazmaz, hata mesajı verir.
#   -ISALNUM
# verilen değişkene tanımlanmış string ifadede alfanümerik karakter veya karakterler olup olmadığını tespit eder.
#eğer alfanümerik bir karakter tespit eder ise false döndürür, yoksa true döndürür.
#   -ISALPHA
# isalpha metodu bir string ifadenin tamamı alfabetik ise true döndürür, en az 1 tane alfabetik dışı karakter var ise
#false döndürür.*****(boşluk karakteri alfabetik değildir.!)*****
#   -ISASCII
# isascii metodu bir string ifadede bulunan tüm karakterler 128 adet ascii verisini içeriyor ise true döndürür.
#en az bir tane 129 ve sonrası ascii karakteri içerirse false döndürür.
#   -ISDECİMAL
# isdecimal metodu bir string ifadede sadece rakam olduğu zaman true döndürür. eğer rakam harici bir karakter olursa
#false döndürür.
#   -ISDIGIT
# isdigit metodu bir string ifadede sadece rakam olduğu zaman true döndürür. eğer rakam harici bir karakter varsa
#false döndürür.
#   -IS IDENTIFIER
# isidentifier metodu sadece (a-z, 0-9 ve _) karakterlerini kabul edip True döndürür. Aksi takdirde false döndürür.
#EK BİLGİ** bir identifier sayı ile başlayamaz. sayı ile başlayan değerler is identifier metodunda false değeri alır.
#   -IS NUMERİC
# isnumeric metodu kontrol ettiği string değerde ki tüm karakterler nümerik yani rakamdan oluşuyor ise,
#true değerini döndürür. bir veya daha fazla nümerik olmayan karakter olduğunda false döndürür.
#EK BİLGİ** "-" işareti ve ".(ondalık işareti)" de false olarak değerlendirilir. çünkü isnumeric sadece nümerik karakterleri kabul eder.
#   -IS PRINTABLE
# isprintable metodu, kendisine verilen string değerde tüm karakterler çıktıda yazdırılabilir ise true döndürür,
#bir veya daha fazla çıktıda yazdırılmayan karakter string ifadede mevcut ise false döndürür.
#Örneğin "\n" çıktıda yazdırılamaz bir ifadedir ve bunu içeren bir string değer, isprintable metoduna atanırsa 
#false döndürür.
#   -IS SPACE
# isspace metodu bir strin değerde ki tüm karakterler boşluk karakterinden oluşuyor ise true döndürür, aksi takdirde
#false döndürür.
#   -IS TITLE
# istitle metodu, title metoduna uyan stringleri true uymayanları false döndürür. Title metodu: her kelimenin
#ilk harfinin büyük harf olması.
#   -JOIN
#join metodu, bir listedeki string ifadeleri tek bir string ifadede toplamaya yarar.
#kullanımında bir seperator belirlemek gereklidir. ", - _" benzeri. 
# mylist = ("honda","bmw","skoda","toyota") #bir tuple tanımladık.
# print(",".join(mylist)) #bir adet seperator "," ve .join("string atanmış değişken") şeklinde oluşturduk. 
#bu kod çıktıda honda,bmw,skoda,toyota verecektir.
#   -LJUST -RJUST
#ljust ve rjust kendilerine verilen parametre değer kadar istenen string değeri sola veya sağa yaslar.
# text = "strawberry"
# result = text.ljust(19)
# print(result,"is my favorite") #bu kod çıktısı "strwaberry yazısını 19 birim sola yaslar."
#EK BİLGİ** ljust ve rjust metodlarına verilecek ikinci bir parametre, ilk parametrede verilen dolgunun ne 
#olacağını belirler. örneğin (19,".") şeklinde parametre verirsek
#EK BİLGİ*** verdiğimiz ilk parametre sola yaslarken değerin kendisini de sayar. örneğin strawberry 10 karakterdir
# doğal olarak araya 9 karakterde boşluk koyar ve ilk verilen 19 parametresini gerçekleştirmiş olur.
#   -LSTRIP -RSTRIP
#lstrip ve rstrip, strip metodu ile aynı olup birisi soldaki istediğimiz karakteri/karakterleri siler diğeri sağdaki.
#   -MAKETRANS VE TRANSLATE
#maketrans ve translate beraber kullanılır. maketrans yapmak istediğimiz değişimin kurallarını belirler,
#örneğin text = "Python"
#       result = text.maketrans("P","T")
#       print(text.translate(result)) #bu şekilde yazdığımızda, maketrans yapılacak işlemi belirler, translate ise
#bu işi gerçekleştirir. Çıktıda Tython yazacaktır. Çünkü "P" ile "T" yer değiştirmiştir.
#EK BİLGİ** maketrans metoduna verilecek 3. bir parametre, translate metoduna verdiğimiz string ifadeden kaldırmak
#istediğimiz karakterleri belirler.
# text = ("Hello Python!")
# x = "eyt"
# y = "bzk"
# z = "H"
# result = text.maketrans(x,y,z)
# print(text.translate(result)) # bu kod çıktıda, 3. parametreden kaynaklı "H" karakterini siler, 1. parametrede ki
# eyt harflerini, 2. parametredeki bzk harfleri ile sırası ile değiştirir.
# e --> b, y --> z, t --> k. "Çıktıda bllo Pzkhon!" yazacaktır. 
#   -PARTITION
#partition metodunu kullanarak, bir string ifadeyi 3'e bölebiliriz. metoda verdiğimiz parametre, 2. değer
#olarak referans alınır ve öncesi ve sonrasını bölerek toplamda string değeri 3'e böler.
#   Örnek:
# text = ("My favorite is strawberry in fruits.")
# result = text.partition("strawberry")
# print(result) #bu kodun çıktısı ('My favorite is ', 'strawberry', ' in fruits.') olarak çıkacaktır.
#   -REPLACE
#replace metodu, bir string ifade için kendisine verilen ilk parametreyi, ikinci parametre ile yer değiştirir.
#   Örnek:
# text = "I love animals"
# result = text.replace("animals","fruits")
# print(result) # bu çıktıda kodda replace metoduna verilen ilk parametre olan animals, fruits ile yer değiştirir.
#EK BİLGİ** replace metoduna verilecek 3. bir parametre, ilk 2 parametrenin string ifadede kaç kere yer değiştireceğini
#belirler. örneğin ana string ifadede 3 adet animals yazısı var ise ve 3.parametre 2 ise ilk 2 animals fruits olur.
