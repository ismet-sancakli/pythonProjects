'''

İç içe Fonksiyonlar ve Fonksiyon Parametreleri

*args parametresi


'''
def fonksiyon(*args): # İstediğimiz sayıda argüman gönderebiliyoruz.
    print(args)
    for i in args:
        print(i)


fonksiyon(1,2,3)
fonksiyon(1,2,3,4,5)

def fonksiyon1(isim,*args): 
    print("İsim:",isim)
    for i in args:
        print(i)

fonksiyon1("Murat",1,2,3,4,5,6,7,8)        
#%%
'''
**kwargs parametresi


sözlük yapısını kullanır.
'''

def fonksiyon(**kwargs):
    print(kwargs)
fonksiyon(isim = "Murat", soyisim = "Coşkun", numara = 12345)

'''
Dikkat ederseniz 2 yıldız koyarak keyword argümanlar ile (anahtar kelimeli argümanlar) fonksiyonumuzu tanımladık 
ve argümanlara isim vererek fonksiyonumuzu çağırdığımızda isimleri anahtar kelime , argüman değerlerini değer olarak alarak fonksiyonumuz sözlük oluşturdu. 
İşte keyword argümanlar bu şekilde kullanılabiliyor.
'''
def fonksiyon(**kwargs):
    for i,j in kwargs.items():
        print("Argüman İsmi:",i,"Argüman Değeri:",j)
    
fonksiyon(isim = "Murat", soyisim = "Coşkun", numara = 12345)


def fonksiyon2(*args,**kwargs):
    for i in args:
        print("Argümanlar:",i)
    print("------------------------------")
    for i ,j in kwargs.items():
        print("Argüman İsmi:",i,"Argüman Değeri:",j)
        
fonksiyon2(1,2,3,4,5,6,7,isim = "Murat",soyisim = "Coşkun", numara = 12345)

#%%%

# İç içe Fonksiyonlar

'''

Pythonda fonksiyonlar da birer obje oldukları için hem bir tane değişkene atanabilirler, 
hem de başka bir fonksiyonun içinde tanımlanabilirler. Şimdi bunlara bakmaya başlayalım.
'''
def selamla(isim):
    print("Selam",isim)
selamla("Ayşe")
# Bir tane değişkene atıyoruz.

merhaba = selamla
merhaba

merhaba("Ayşe") # Fonksiyon olduğu için artık bu isimle de kullanabilirim.

del selamla # Selamla fonksiyonunu siliyorum.
# selamla fonksiyonunu silmeme rağmen merhaba değişkenine atadığım fonksiyon silinmedi.

merhaba("Kemal") # selamla objesi silinmesine rağmen merhaba objesi silinmedi.
merhaba

def fonk():
    def fonk2():
        print("Küçük fonksiyondan Merhaba")
    print("Büyük fonksiyondan Merhaba")
    fonk2() # Tanımladığım fonksiyonu kullanabilirim.


fonk()
#fonk2() # Lokal bir değişken olduğu için fonksiyon() çağrısından sonra yok oldu.

def fonksiyon(*args): # args : (1,2,3,4,5,6)
    
    def topla(args): # (1,2,3,4,5,6)
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    
    print(topla(args))

fonksiyon(1,2,3,4,5,6)

#%%

'''
Python Decorator fonksiyonlarının oluşturulması ve kullanılması.

Decorator fonksiyonlar, Pythonda fonksiyonlarımıza dinamik olarak ekstra özellik eklediğimiz fonksiyonlardır
 ve decorator fonksiyonların kullanımı kod tekrarı yapmamızı engeller.
 Pythonda decorator fonksiyonlar Flask gibi frameworklerde oldukça fazla kullanılır.

'''

import time

def kareleri_hesapla(sayilar):
    
    sonuc=list()
    baslama = time.time() # for döngüsü başlamadan önceki zamanı bize verir.
    
    for i in sayilar:
        sonuc.append(i**2)
    
    bitis = time.time()
    
    print("Bu fonksiyon " +str(bitis - baslama) +"saniye sürdü")
    return sonuc

def küpleri_hesapla(sayi):
    
    sonuc2 = list()
    baslama = time.time()
    for i in sayi:
        sonuc2.append(i**3)
    bitis = time.time()
    print("Bu fonksiyon " +str(bitis - baslama) +"saniye sürdü")    
    
    return sonuc2


kareleri_hesapla (range(100000))
küpleri_hesapla (range(100000))

#%%

# decorator kullanarak nasıl yapılır ?



import time

def zaman_hesapla(func):
    def wrapper(sayilar):
        baslama = time.time()
        sonuc = func(sayilar)        
        bitis = time.time()
        print("Bu fonksiyon " +str(bitis - baslama) +"saniye sürdü")  
        return sonuc
    return wrapper


@zaman_hesapla  
def kareleri_hesapla(sayilar):
    
    sonuc=list()   
    
    for i in sayilar:
        sonuc.append(i**2)
    

    return sonuc


@zaman_hesapla
def küpleri_hesapla(sayi):
    
    sonuc2 = list()   
    for i in sayi:
        sonuc2.append(i**3)  
    
    return sonuc2


kareleri_hesapla (range(100000))
küpleri_hesapla (range(100000))

'''
1. kareleri_hesapla fonksiyonu zaman_hesapla fonksiyonuna argüman olarak gidiyor.
2. wrapper fonksiyonu kareleri_hesapla fonksiyonuna argüman olarak gönderilen 
"sayılar" argümanını argüman olarak alıyor.sd
3. wrapper fonksiyonu hem zaman hesaplama işlemini gerçekleştiriyor,hem de gönderilen
fonksiyonu çalıştırıyor. Böylelikle bu fonksiyona ekstra özellik ekliyor.
4.zaman_hesaplama fonksiyonu en son işlem olarak wrapper fonksiyonumuzu dönüyor.
'''





