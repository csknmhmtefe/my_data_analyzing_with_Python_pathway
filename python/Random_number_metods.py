import random
                                            #RANDOM SAYI METODLARI


#seed metodunu kullanarak, random bir sayının sabit şekilde sonuçlar vermesini sağlayabiliriz.kodu her 
# çalıştırdığımızda aynı sonuçları verir.

# random.seed(5)
# print(random.random())
# print(random.random())
# print(random.random())

#getstate, setstate kullanımı. getstate kullanarak komuttan sonra gelen random sayı verisini kaydedip, setstate 
# kullanarak setstate komutundan sonra gelen random değere sabit olarak kaydettiğimiz getstate'e bağlı random sayı 
# veya sayıları işleyebiliriz.
# print (random.random())

# state = random.getstate()

# print (random.random())

# random.setstate(state)

# print (random.random())

#getrandbits, istediğimiz bit boyutunda sayı üretmeyi sağlayan metod.
# print(random.getrandbits(8))

#randrange, verdiğimiz aralıkta sayı üretmeyi sağlayan metod. verilen ilk değeride kapsarken, ikinci değer bu 
# aralığa girmez. örneğin 2,10 aralığını verdiğimizde 2 sayısı da gelme ihtimaline sahipken, 10 sayısı'nın gelme 
# ihtimali yoktur.
# ayrıca randrange metoduna verilecek üçüncü bir parametre, verilen ilk değerden itibaren kaçar kaçar artarak 
# üretmesini istediğimizi belirlememizi sağlar.
#print(random.randrange(2,10))
#print(random.randrange(2,10,3)) 2'den başlayarak 3 katlarını dahil eder sadece koda. yani 2+3=5,5+3=8, 8+3=11 
# olduğundan sadece 2,5,8 ele alınır kodda. ikinci parametre
# dışarda tutulur. ve 2,5,8 sayılarını random şekilde verir.
# kısa bir tanımla, ilk parametre başlangıç, ikinci parametre bitiş ancak kendisi hariç, üçüncü parametre ise adım 
# sayısını temsil eder.
#print(random.randrange(2,10,3))

#randint metodu ise randrangeden farkı ikinci parametreyide dahil eder ve üçüncü bir parametre belirtemeyiz 
# adım sayısı için.
#print(random.randint(2,10))

#choice metodu verilen değerlerden random 1 tane seçer.
# myList = ["red","blue","green"]
# print(random.choice(myList))
# text = "python"
# print(random.choice(text))
# choice metodu yukarıda ki kodun çıktısı olarak sadece bir harfi random seçerek verecektir.

#choices metodu ise choicedan farklı olarak çoğul seçer.
# myList = ["grape","strawberry","banana","apple"]
# print(random.choices(myList,weights=[10,1,1,1],k=20))
#burada weights metodu liste içinde hangi string değere ne kadar ağırlık verileceğini belirler. k metodu ise
#çıktıda verilecek listenin uzunluğunu belirler. yukarıda ki koda göre "grape" değeri diğerlerinin 10 katı
#gelme ihtimaline sahip olup, çıktıdaki değer sayısı 20 olacaktır.

#shuffle metodu verilen değerleri rastgele yeniden sıralar. uygulandıktan sonra değişken içindeki değerler artık
# shuffle etkisindedir. orjinalliğini kaybetmiştir.
# myList = ["skoda","bmw","audi","mercedes","nissan","opel","lada"]
# random.shuffle(myList)
# print(myList)
#yukarıda bulunan kod dizisi, verilen listedeki string değerlerin yeniden sıralanarak çıktı verilmesini sağlar.

#sample metodu shuffledan farklı olarak bir listeden belirli sayıda değeri rastgele seçer, ancak sonrasında yeni
# bir kod yazdığımızda liste eski halini korur. shuffle metonda ise uygulandıktan sonra artık orjinal liste,shuffle 
# etkisine uğramış hali ile kalır.
# myList = ["ford","toyota","suzuki","honda","hyundai"]
# print(random.sample(myList,k=2))

#random metodu ise varsayılan olarak 0 ile 1 arasında ondalıklı bir sayı çıktısı verir.
# print(random.random())

#uniform metodu ise random ile benzer işlevde olup, bu sefer verilen iki parametre arasında ondalıklı değer üretimini
# sağlar.
# print(random.uniform(2,4))

#triangular metodu uniform ile benzer işlevdedir. ancak 3. bir parametre girerek aralığın modunu belirleyebiliriz.
#örneğin 30 ile 70 arası 35 olarak mod belirlersek bize verilen random ondalıklı sayılar, 30 a daha yakın olacaktır.
# print(random.triangular(30,70,35))