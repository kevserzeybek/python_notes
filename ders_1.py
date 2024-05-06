
#! Yorum Satırı:
"""
- Yorum satırı eklemek için '#' satır bu işaret ile başlamalıdır. 
- Satır sonu yorumlarında # işaretinden önce 2 boşlup # işaretinden sonra 1 boşluk bırakılmalıdır.
- Çok uzun bir yazıyı yoruma almak isetsek başına ve sonun 3 adet " işareti eklemeliyiz.
"""

#? Tek Satırlık Yorum
# print bir fonksiyondur. Eğer ekrana bir değer bastırmak istersek print fonksiyonunu kullanırız.
print("Hello World!!!")

#? Satır İçi Yorum
a = 3 + 2 
if a == 5:
    print(a)  # koşul sağlanırsa a değeri ekranda yazdıralacak

#? Çok Satırlı Yorum
# Yorum satırı eklemek için satır '#'  işaret ile başlamalıdır. 
# Satır sonu yorumlarında # işaretinden önce 2 boşlup # işaretinden sonra 1 boşluk bırakılmalıdır.
# Çok uzun bir yazıyı yoruma almak isetsek başına ve sonun 3 adet ' işareti eklemeliyiz.



#! Bakalım yazdığımız çok staırlı yorumlar pep'8 kurallarına göre 72 satırı aşıp aşmıyor mu ?

a = "Yorum satırı eklemek için '#' satır bu işaret ile başlamalıdır. "
b = "Satır sonu yorumlarında # işaretinden önce 2 boşlup # işaretinden sonra 1 boşluk bırakılmalıdır."
c ="Çok uzun bir yazıyı yoruma almak isetsek başına ve sonun 3 adet işareti eklemeliyiz."

#? len() fonksiyonu, bir Python nesnesinin uzunluğunu (kaç eleman içerdiğini) hesaplar ve bu uzunluğu bir tamsayı olarak döndürür. 
print(len(a))
print(len(b))
print(len(c))

#!Değişken Tanımlama:
#? Geçici olarak bir veri sakladığımız alana Değişken denilebilir.

#! Değişken Tanımlama kuralları:
#  1- Türkçe karakter içermemesi tavsiye edilir.
#? 2- Sayı ile başlanmamalıdır. Harf veya _ ile başlamalıdır.
#  3- karakterler arasında boşluk olmamalıdır.
#? 4- Büyük küçük harf duyarlılığı vardır.
#  5- Keywordler değişken ismi olarak kullanılamaz. help('keywords') ile bu keywordslere ulaşabiliriz.


number = 1  # ==> ✔️

# 1number = 1 ==> ✖️

# 1 = b ==> ✖️

# İstanbul = 34 ==> ✖️

# number two = 2 ==> ✖️

# number@ = 3 ==> ✖️

# number-four = 4 ==> ✖️

number_five = 5  # ==> ✔️

# for = 6  # ==> ✖️

print(help('keywords'))


#! Numerik Veri Tipleri: Pythonda değişken tipleri bellek alanına ayırmak için açık bir bildirime ihtiyaç duymaz,
#  int ---> Tam Sayı
#? float ---> Ondalıklı Sayı
#  str ---> "" veya '' içerisine yazılan bütün karakterler
#? bool ---> True veya False bilgisi
#  complex ---> a+bj olarak ifade edilen hemen hemen hiç kullanılmaz.

#? c++ da değişken tipleri bellek alanına ayırmak için açık bir bildirime ihtiyaç duyar:
# int sayi1 = 5

sayi = 5


#? String (str):
# "" , '' ve """""" içine yazılan bütün karakterler string'dir.
print("Merhaba Python")
print('Merhaba Python')
print("""Merhaba Python""")
print('''Merhaba Python''')

#? Python'da üç sayısal tür vardır:
# 1- Integer (int)
# 2- Float 
# 3- Complex

#? Integer (int) 
# Int veya tamsayı, pozitif veya negatif, ondalık basamak içermeyen, sınırsız uzunlukta bir tam sayıdır.
x = 1
y = 35656222554887711
z = -3255522


#! VERİ TÜRLERİNİ KONTROL ETMEK İÇİN TYPE KULLANIRIZ JS DEKİ TYPEOF AYNI GÖREVİ GERÇEKLEŞTİRİR.

print(type(x))  # <class 'int'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'int'>

"""
type() fonksiyonu, verilen bir nesnenin sınıfını döndürür. 
Örneğin, type(x) ifadesi, x değişkeninin sınıfını döndürür. 
Eğer x bir tamsayı sayı ise, type(x) ifadesi <class 'int'> olarak değerlendirilir. 

Bu ifade, x değişkeninin int sınıfına ait bir nesne olduğunu ve int sınıfının özelliklerini ve davranışlarını sergilediğini gösterir.
class, Python'da bir nesnenin türünü belirtir. 
Bir nesnenin sınıfı, o nesnenin özelliklerini ve davranışlarını belirleyen bir şablon gibi düşünülebilir. 
Örneğin, int sınıfı, tamsayılar için bir türdür ve bu türdeki nesnelerin özellikleri ve davranışları, 
tamsayılar işlem yapmak için gereken özellikleri içerir.
"""


#? Float
# Bir veya daha fazla ondalık basamak içeren pozitif veya negatif bir sayıdır. 
# Float, 10'un kuvvetini belirtmek için "e" harfi bulunan bilimsel sayılar da olabilir. 
x = 1.10
y = 1.0
z = -35.59

print(type(x))  # <class 'float'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'float'>

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))  # <class 'float'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'float'>


#? Complex
# Karmaşık sayılar sanal kısım olarak "j" ile yazılır:
x = 3+5j
y = 5j
z = -5j

print(type(x))  # <class 'complex'>
print(type(y))  # <class 'complex'>
print(type(z))  # <class 'complex'>

#? Boolean (bool):
# doğru ve yanlış değerleri saklamak için kullanılan veri türüdür.
a = True
b = False

print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>


#! Tip Kontrolü:
# type() işlevini kullanarak herhangi bir nesnenin veri türünü alabilirsiniz 

#! Tip Dönüşümü:

age = 24
weight = 48.7
name = 'Pakize'
isStudent = True

print(type(age))  # <class 'int'>
print(type(weight))  # <class 'float'>
print(type(name))  # <class 'str'>
print(type(isStudent))  # <class 'bool'>

#? int to float
resault = float(age)  
print(resault)  # 24.0 
print(type(resault))  # <class 'float'>

#? float to init 
resault2 = int(weight)
print(resault2)  # 48
print(type(resault2))  # <class 'int'>

#? bool to str 
resault3 = str(isStudent)
print(resault3)  # True
print(type(resault3))  # <class 'str'>

#? bool to int 
resault4 = int(isStudent)
print(resault4)  # 1
print(type(resault4))  # <class 'int'>

#? bool to float
resault5 = float(isStudent)
print(resault5)  # 1.0
print(type(resault5))  # <class 'float'>

#? int to str
resault6 = str(age)
print(resault6)  # 24
print(type(resault6))  # <class 'str'>

#? float to str
resault7 = str(weight)
print(resault7)  # 48.77
print(type(resault7))  # <class 'str'>

#! Not: Karmaşık sayıları başka bir sayı türüne dönüştüremezsiniz.


#!Değişken Tanımlama:
#? Geçici olarak bir veri sakladığımız alana Değişken denilebilir.

#  Değişkenlerin belirli bir türle bildirilmesi gerekmez ve hatta ayarlandıktan sonra türü değiştirebilirler.
#  js de const var veya let gibi tanımlamalar yapmak zorundaydık
x = 4       # x type = int
print(x)  # 4
x = "Sally" # x type = str
print(x)  # "Sally"

#? Bir değişkenin veri tipini belirtmek istiyorsanız, bu Casting ile yapılabilir.
x = str(3)    # x will be '3'
print(type(x))  # <class 'str'>
y = int(3)    # y will be 3
print(type(y))  # <class 'int'>
z = float(3)  # z will be 3.0
print(type(z))  # <class 'float'>


#? Python, bir satırda birden çok değişkene değer atamanıza izin verir: 
#! Not: Değişken sayısının değer sayısıyla eşleştiğinden emin olun, aksi takdirde bir hata alırsınız.
a, b, c = 10, 20, 30
print(a)  # 10
print(b)  # 20
print(c)  # 30

#? Aynı değeri tek bir satırda birden çok değişkene atayabilirsiniz : 
x = y = z = "Orange"
print(x)  # Orange
print(y)  # Orange
print(z)  # Orange


#! Değişken Çıktısı | Output Variables
#? Python print() işlevi genellikle değişkenleri çıktısını görüntülemek için kullanılır. 
x = "Python is awesome"
print(x)  # Python is awesome

# İşlevde print(), virgülle ayırarak birden çok değişken çıktısı alırsınız: 
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)  # Python is 100

#? Birden fazla değişkenin çıktısını almak için operatörü de kullanabilirsiniz +:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)  # Python is awesome

# İşlevde print(), bir diziyi ve bir sayıyı operatörle birleştirmeye çalıştığınızda + , Python size bir hata verecektir:
x = 5
y = "John"
# print(x + y)

#? İşlevde birden çok değişken çıktısı almanın en iyi yolu, print() bunları farklı veri türlerini bile destekleyen virgüllerle ayırmaktır:
x = 5
y = "John"
print(x, y)


"""
Neden Değişken Kullanmalıyız?
Bir senaryo düşünelim, bir e-ticaret sitemiz var ve ürünleri aldığımız fiyata ek olarak biraz kar elde etmek için fiyatı yükselteceğiz:
"""

print(500 + (500 * 0.18))  # 590.0

"""
Şimdi toptancıdan aldığımız 500 fiyatına zam geldi ve bizde bu tarz çok FAZLA ürün var ve birden fazla yerde geçmektedir. 
Hepsini tek tek hesaplamamız gerekecek. 
Bu ürünlerin fiyatlarını bir değişkene atayıp bu değişken adı ile formül ticaretini yaparsak kendimizi daha az tekrar ederiz ve zaman kazanırız vb. tasarruf ederiz.
"""

productA = 800
profit = 0.18
print(productA + (productA * profit))  # 944.0

