'''
Generatorlar Pythonda iterable objeler (örnek olarak fonksiyonlar) oluşturmak için kullanılan objelerdir 
ve bellekte herhangi bir yer kaplamazlar.
 Örneğin, 100.000 tane değer üretip, bu değerleri bir listede tutmak bellekte oldukça fazla yer kaplayacaktır.
 O yüzden bu işlemi gerçekleştiren bir fonksiyonu generator fonksiyon şeklinde yazmak oldukça mantıklı olacaktır.
'''

def karelerial():
    sonuç = []
    
    for i in range(1,6):
        sonuç.append(i**2)
    return sonuç
 
 
print(karelerial())

#%%

# Generator ile yapılan hali.

def karelerial():
    for i in range(1,6):
        yield i ** 2 # yield anahtar kelimesi generator'un değer üretmesi için kullanılıyor.
generator =  karelerial()
 
print(generator) # Generator objesi
# Şu durumda generator değişkeni içinde değerler yok. Bu değerler bizim onlara erişmek istediğimizde üretilecek.
# Generator objesi iteration bir obje.

iterator = iter(generator)

next(iterator) # Burada üretilen 1 değeri üretildi ve kayboldu. Çünkü generatorlar değerleri herhangi bir yerde saklamaz.
next(iterator)
next(iterator)
next(iterator)
next(iterator)
# next(iterator) # yield değerleri bitti.

# Buradan şunu anlamalıyız generatot iterator tarafından kullanıldı ve bitti başka bir iterator aynı generator u kullanamaz. 

it2 = iter(generator)

next(it2)

#%%
 # list comprehensionları generatorlara dönüştürmek.
 

liste = [i * 3 for i in range(5)] # burada range(5) ifadesi 0 dan 5 e kadar olan sayıları alır. 5 dahil değil

print(liste)

generator1 = (i * 3 for i in range(5)) # List comprehension dan farkı sadece köşeli olmayan parantez.
print(generator1)

iter1 = iter(generator1)
next(iter1)
next(iter1)
next(iter1)
next(iter1)

#%%


# Çarpım Tablosu

def carpimtablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} x {} = {}".format(i,j,i*j)

for i in carpimtablosu(): # For döngüsü kendinden iteration kullandığı için her next iteration istediğinde yield değer üretecek. 
    print(i)
'''
Peki generatorlar Pythonda nerede kullanılıyor ?
Aslında bizim daha önce öğrendiğimiz range fonksiyonu Pythonda generatorlar yazılmış bir fonksiyondur.
'''
#%%





































