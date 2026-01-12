name="efe"
age=23
weight=102.2
comp=2j
myList = ["Musaba","Aktürkoğlu","Duran","Asensio","Mercan","Skriniar","Ederson","Guendouzi"] #list data type
myTuple = ("Aydın","Szymanski","Nesyri","Fred","Yüksek","Brown","Oosterwolde","Söyüncü") #tuple data type
myRange = range(9) #range data type 0-8
myDict = {"name":"efe", "age":34}#dict data type "dict=dictionary"
mySet = {"Musaba","Aktürkoğlu","Duran","Asensio","Mercan","Skriniar","Ederson","Guendouzi"}#set data type
myFrozen = frozenset({"Musaba","Aktürkoğlu","Duran","Asensio","Mercan","Skriniar","Ederson","Guendouzi"})#frozenset data type
myBool = True #Boolean data type "True or False"
myNone = None #null none type
name=b"" #bytes data type, b is "bytes" variablename=b"" or variablename=bytes("") for using.
name=bytearray("Hello") #bytearray is dynamic byte variable type. difference of byte type is developer will make changes on this variable type.
name=memoryview(bytes(5)) #memoryview using for manipulating ram usage of programmes or etc. users will optimizing ram performance with use this variable type.

##str veri tipinde harfler kullanılır. "tırnak içine yazılır" değişkene atarak kullanılır. 
##int veri tipinde rakamlar kullanılır. değişkene atarak kullanılır.
##float veri tipinde rakamlar kullanılır. ondalıklı değerler için kullanılır. değişkene atarak kullanılır.
##complex veri tipinde rakam + imajiner değer kullanılır. değişkene atarak kullanılır. 
##list veri tipi listeleme için kullanılır. köşeli parantez ile kullanılır. değişkene atarak kullanılır.
##tuple list veri tipi ile benzer çalışır, varsayılan olarak değeri değiştirlemezdir. normal parantez kullanılır.
#(tuple listesinin belirlenmiş değerini değiştirmek için, ekstra olarak list veritipi dönüşümü uygulanmalıdır.)
##range veri tipi aralık belirtmek için kullanılır. ekstra olarak "range" yazarak değişkene atanmalıdır.
#örnek range kullanımı: degisken = range(9) "çıktıya range=(0,9) yazar. ekstra olarak print işleminin başına * 
# koyarak 0'dan 8'e kadar görüntüleme sağlanabilir." varsayılan olarak 0'dan itibaren yazılan sayıya kadar listeler.
##dict veri tipi anahtar-değer ikilisi girilmesini sağlar. print işleminde değişkenine * eklenirse sadece anahtar
#kısımları alır.
##set veri tipi list veri tipine benzer fakat sırasız çıktı yapar. yani içindeki değerler belirli bir sırada değildir.
##frozenset veri tipi tuple'ın mantığı gibi set ile aynı amaçtadır ancak değiştirilemezdir.
##bool veri tipi True False olarak çalışır.
##none veri tipi içi boştur.
##b ise bytes anlamına gelir. yazılan değerin byte karşılığını verir. değiştirilemezdir.
##bytearray veri tipi bytes'ın değiştirilebilir halidir.
##memoryview metodu ram kullanımını açığa çıkarmak için kullanılabilir.
