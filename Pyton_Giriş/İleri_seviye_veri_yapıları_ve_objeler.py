# İleri seviye veri yapıları ve objeler

# Decimal to Binary 2 lik tabanda gösterme
bin(4) 

bin(19)
#%%
# Decimal to Hex

hex(4)
hex(20)
hex(512)
#%%
# abs fonksiyonu
# Sayının mutlak değerini almamızı sağlar.
abs(-4)
#%%
'''
 round fonksiyonu
 Sayıları alta veya üste yuvarlar.
'''
round(3.7)
round(3.21329321321323,4) # Ondalıklı sayının 4. hanesine göre yuvarlar
#%%
'''
max ve min fonksiyonu

max() fonksiyonu verdiğimiz değerlerin en büyüğünü döndürür.

min() fonksiyonu verdiğimiz değerlerin en küçüğünü döndürür.
'''

max(100,-2,3,4,1,131)  # İstediğimiz kadar değer verebiliriz.

max([13.2,-4.32,1.2,15.6]) # Sayıları liste şeklinde de verebiliriz.

max((13.2,-4.32,1.2,15.6)) # Sayıları demet şeklinde de verebiliriz.

min(100,-2,3,4,1,131)
#%%
'''
sum fonksiyonu
sum() fonksiyonu verilen değerleri toplayarak döndürür. Değerlerin liste,demet vb. şeklinde verilmesi gerekir.
'''

sum([3,4,5,6,7])

sum((3,4))
#%%
'''
pow fonksiyonu
pow() fonksiyonu üs alma işlemlerinde kullanılır.
'''

pow(2,4) # 2 üzeri 4
pow(3,4) # 3 üzeri 4
pow(17,2) # 17 üzeri 2
    
#%%

# İleri Seviye String Yapıları

'''
upper() ve lower()
upper() metodu stringin tüm karakterlerini büyük harfe çevirir.

lower() metodu stringin tüm karakterlerini küçük harfe çevirir.
'''

"python".upper()
"PYTHON".lower()
"PythOn".upper()
"PythOn".lower()
#%%
'''
replace()
replace(x,y) : Stringteki x değerlerini y ile değiştirir.
'''
"Herkes ana baba bacı gardaş".replace("a","o")
"Kunduz".replace("duz","zun")
"Python Programlama Dili".replace(" ","-")
#%%
'''
startswith() ve endswith()
startswith(x) : String x ile başlıyorsa True, başlamıyorsa False değeri döndürür.

endswith(x) : String x ile bitiyorsa True, bitmiyorsa False değeri döndürür.
'''


"Python".startswith("py")
"Python".startswith("Py")
"Python".endswith("on")
"Python".endswith("az")
#%%
'''
split()
split(a) : Verilen bir a değerine göre string parçalara ayrılarak herbir parça listeye atılır.


'''

liste = "Python Programlama Dili".split(" ") # Boşluk karakterine göre ayrıldı.
print(liste)


liste8 = "Python-Php-Java-C-Javascript".split("-")
print(liste8)
#%%
'''
strip() , lstrip() ve rstrip()
strip(x) : Stringin başında ve sonunda bulunan x değerlerini siler.

lstrip(x) : Stringin sadece başında bulunan x değerlerini siler.

rstrip(x) : Stringin sadece sonunda bulunan x değerlerini siler.

'''

"                   python                   ".strip() # değer göndermezsek varsayılan olarak boşluk karakteri
">>>>>>>>>>>>>>Mustafa>>>>>>>>>>>>>>>>>>>>>>>>>>".strip(">")

"                            python      ".lstrip()
"                            python      ".rstrip()

#%%
'''
join()
Listenin elemanlarını bir string değeriyle birleştirmemizi sağlar.

'''

liste9 = ["21","02","2014"]
"/".join(liste9)

liste = ["T","B","M","M"]
".".join(liste)

#%%
'''
count()
count(x): Stringin içindeki x değerlerini sayar.

count(x,index): Stringin içindeki x değerlerini verilen index değerinden başlayarak saymaya başlar.
'''
"ada kapısı yandan çarklı".count("a")
"ada kapısı yandan çarklı".count(" ")
"ada kapısı yandan çarklı".count("a",2)
#%%
'''
find() ve rfind()
find(x) : x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. 
Bulamazsa "-1" değerini verir.

rfind(x) : x değerini sondan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür.
Bulamazsa "-1" değerini verir.
'''
"araba".find("a")
"araba".find("s")
"araba".rfind("a")
"araba".rfind("s")

#%%

# İleri Seviye Kümeler (sets) ve Metodları

'''
Kümeler, matematikte olduğu gibi bir elemandan sadece bir adet tutan bir veritipidir. 
Bu açıdan kullanıldıkları yerlerde çok önemli bir veritipi olmaktadırlar.
'''
x =  set() # Boş küme
type(x)

liste = [1,2,3,3,1,1,2,2,2] # Aynı elemanı birçok defa  barındıran bir liste
x = set(liste) # Veri tipi dönüşümü
print(x)# Aynı elemanlar tek bir elemana indirgendi.

x = set("Python Programlama Dili")  # Aynı karakterler tek bir karaktere indirgendi.
print(x)

a = {"Python","Php","Python"}
print(a)
#%%
'''
For döngüsüyle Gezinmek
Kümeler de tıpkı sözlükler gibi sırasız bir veri tipidir. Bunu for döngüsüyle görebiliriz

'''
y  = {"Python","Php","Java","C","Javascript"}

for i in y:
    print(i) 

# Peki bir kümenin elemanlarına direk olarak ulaşabiliyor muyuz ?
y
#%%
'''
Buradaki işlemler aslında kümelerde tanımlı değil. Yani biz bir kümenin elemanlarına ne indexle ne de eleman ismiyle erişebiliyoruz.
Erişmek için mutlaka veritipi dönüşümü yapmamız gerekiyor.
'''
liste = list(y)

liste[0]
#%%
'''
Kümelerin Metodları
Eleman Eklemek : add() metodu
Kümeye eleman eklemimizi sağlar. Aynı eleman eklenmeye çalışırsa hata vermez ve herhangi bir ekleme işlemi yapmaz.
'''
z = {1,2,3}
z.add(4)
print(z)
#%%
'''
İki kümenin farkı : difference() metodu
Bu metod birinci kümenin ikinci kümeden farkını döner.

    küme1.difference(küme2) # Küme1'in Küme2'den farkı

'''

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme1.difference(küme2)

küme2.difference(küme1)
#%%
'''
İki kümenin farkı ve güncelleme : difference_update() metodu
Bu metod birinci kümenin ikinci kümeden farkını dönerek birinci kümeyi bu farka göre günceller.

küme1.difference_update(küme2) # Küme1'in Küme2'den farkı
'''
küme1.difference_update(küme2)
küme1
#%%
'''
Kümeden Eleman Çıkartmak : discard() metodu
İçine verilen değeri kümeden çıkartır. Eğer kümede öyle bir değer yoksa, bu metod hiçbir şey yapmaz(Hata vermez).
'''

küme1 = {1,2,3,4,5,6}
küme1.discard(2)
küme1
küme1.discard(10)
#%%
'''
Küme kesişimleri : intersection() metodu
Bu metod iki kümenin kesişimleri bulmamızı sağlar.

'''
kümex = {1,2,3,10,34,100,-2}
kümey = {1,2,23,34,-1}

kümex.intersection(kümey)
#%%

'''

Küme kesişimleri ve güncelleme : intersection_update() metodu
Bu metod birinci kümeyle ikinci kümenin kesişimlerini bulur ve birinci kümeyi bu kesişime göre günceller.
'''
küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme1.intersection_update(küme2)
küme1
#%%
'''
Kümeler ayrık küme mi ? : isdisjoint() metodu
Bu metod, eğer iki kümenin kesişim kümesi boş ise True, değilse False döner.
'''

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme3 = {30,40,50}
küme1.isdisjoint(küme2)

küme1.isdisjoint(küme3)
#%%
'''
Alt kümesi mi ? : issubset() metodu
Bu metod , birinci küme ikinci kümenin alt kümesiyse True, değilse False döner.
'''
küme1 = {1,2,3}
küme2 = {1,2,3,4}
küme3 = {5,6,7}
küme1.issubset(küme2)

küme1.issubset(küme3)
#%%
'''

Birleşim Kümesi : union() metodu
Bu metod, iki kümenin birleşim kümesini döner.
'''


küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme1.union(küme2)
#%%
'''
Birleşim Kümesi ve update : update() metodu
Bu birinci kümeyle ikinci kümenin birleşim kümesini döner ve birinci kümeyi buna göre günceller.
'''
küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

küme1.update(küme2)
küme1




