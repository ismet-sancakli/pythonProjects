'''

***Modüllerin kullanımı***

'''

import math as matematik # böyle yaparak artık math modülünü matematik olarak kullanıyoruz.
dir(math)
help(math)
print(math.factorial(6)) # Faktoriyeli  hesaplar.

math.floor(5.5) # girilen değere en yakın integer değerini verir. 5 çıkar buarda.
math.ceil(5.5)  # girilen değeri yukarı yuvarlar
matematik.factorial(4)
 #%%
 
 # 2. yöntem olarak 
 
from math import * # dersek modül adını yazmadan fonksiyonları kullanabiliriz.
 
factorial(5)
#%%
 
#Eğer sadece birkaç fonksiyonu almak istiyorsak 
 
from math import floor,ceil   # burada sadece foor ve ceil fonkiyonlarını tanımladık.
ceil(5.2)

def factorial(sayi):
    fact = 1
    print("Benim fonksiyonum .. ")
    if(sayi == 0 or sayi == 1 ):
        return 1
    else:
        while (sayi >= 1):
            fact *= sayi
            sayi -= 1
        return fact

from math import * # burada python en son yazılan fonksiyonu kabul eder . Yani bizim yazdığımz fonksiyon çalışmaz..
factorial ( 5)

#%%

# Kendi modülümüzü nasıl yazarız ??
# Yazıdğımız modüle her yerden ulaşmak için pyhton içindeki lib klasörüne atıyoruz.
# Daha sonra import ederek kullanıyoruz.
    
















