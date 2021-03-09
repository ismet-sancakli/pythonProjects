# Python da gömülü fonksiyonlar.

'''
map function  map(fonksiyon,iterasyon yapılabilecek veritipi(liste,demet vb),....)

map() fonksiyonu ilk parametre olarak bir tane fonksiyon objesi alır.
2. parametre olarak da bir tane iterasyon yapılacak veritipi alarak ,
gönderilen fonksiyonu her bir eleman üzerinde uygulayarak sonuçları bir map objesi olarak döner.

'''


def double(x):
    return x*2

map(double, [1,2,34,5,6,7])
list(map(double, [1,2,34,5,6,7]))

list(map ( lambda x : x ** 2 ,(1,2,3,4,5,6,7,8,9,10)))

liste1=[1,2,3,4]
liste2 = [2,4,5,6,7]
liste3 = [5,10,11,12,15,16]
list(map(lambda x,y:x*y,liste1,liste2))

list(map(lambda x,y,z : x*y*z,liste1,liste2,liste3))# ortak eleman sayısına kadar çarpam yapıyor.
#%%

# Map fonk. Örnek
'''
Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.

         [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.

         [12, 30, 30, 9]

'''
def alan(demet):
    return demet[0]*demet[1]

a_list = [(3,4),(5,6),(7,8),(1,9)]    

print(list(map(alan,a_list)))

    





#%%
# reduce fonksiyonu ilk olarak ilk iki elemanı alıyor dahat sonra 3. eleman üzeirnde kullanılıyor.Böyle devam eder.

from functools import reduce

def toplama(x,y):
    return x+y

reduce(toplama,[12,15,16,14]) # ilk ikisi sonra çıkan sonucu 3. ile çıkan sonunuc 4. ile birikerek gidiyor.

reduce(lambda x,y:x*y,[1,2,3,4,5])

def maxi(x,y):
    if(x>y):
        return x
    else:
        return y
    
    
reduce(maxi,[-2,-3,-5,6,2,3,1,74])
    
    
    #%%
'''
 filter() fonksiyonu birinci parametre olarak mutlaka mantıksal değer dönen (True , False) bir fonksiyon alır 
 ve liste gibi veritiplerinin her bir elemanına bu fonksiyonunu uygular. 
 filter sadece True sonuç çıkaran değerleri alarak bir tane filter objesi döner
''' 
filter(lambda x :  x % 2 == 0,[1,2,3,4,5,6,7,8,9,10,11]) # sadece çift sayıları döner
list(filter(lambda x :  x % 2 == 0,[1,2,3,4,5,6,7,8,9,10,11])
   
def asal_mi(x):
    i = 2
    if (x == 1):
        return False # Asal değil
    elif(x == 2):
        return True # Asal sayı
    else:
        while(i < x):
            if (x % i == 0):
                return False # Asal Değil
            i += 1
    return True

asal_mi(34)

filter(asal_mi,range(1,100))
list(filter(asal_mi,range(1,100))) # 1 den 100' e kadar olan asal sayılar.
#%%

# filter fonk. Örnek
'''
Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]
'''
def ücgen_mi(demet):
    
    if (abs(demet[0]+demet[1]) > demet[2] and abs(demet[0]+demet[2]) > demet[1] and abs(demet[1]+demet[2]) > demet[0]):
        return True
    else:
        return False

ü_list = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(ücgen_mi,ü_list)))

#%%


# Örnek

'''
Elinizde şöyle bir liste bulunsun.

    [1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

'''

from functools import reduce
liste = [1,2,3,4,5,6,7,8,9,10]

filtre = list(filter(lambda x : x % 2 == 0,liste))

print(reduce(lambda x,y : x + y,filtre))



#%%
# Zip fonksiyonu
# zip fonksiyonu listelerin elemanları sırasıyla demet şeklinde gruplayarak bir tane liste oluşturuyor

liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11] 

# sonucu [(1,6),(2,7),(3,8),(4,9),(5,10)] yapmaya çalışalım.

i = 0
sonuç = list()
while (i < len(liste1) and i < len(liste2)):
    sonuç.append((liste1[i],liste2[i]))
    
    i +=1
print(sonuç)
    
zip(liste1,liste2)
    
list(zip(liste1,liste2))    

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = ["Python","Php","Java","Javascript","C"]    
    
list(zip(liste1,liste2,liste3))

## Aynı anda iki liste üzerinde gezinmek
liste1 = [1,2,3,4]
liste2 = ["Python","Php","Java","Javascript"]

for i,j in zip(liste1,liste2):
    print("i:",i,"j:",j)    
    
# Sözlükleri zipleyelim.
sözlük1 = {"Elma":1,"Armut":2,"Kiraz":3}
sözlük2 = {"Sıfır":0,"Bir":1,"İki":2}   

list(zip(sözlük1,sözlük2)) # Anahtarlar eşleşti.

list(zip(sözlük1.values(),sözlük2.values())) # Değerler eşleşti  
#%%

# zip fonk. Örnek
  
'''
Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.

        isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.
'''
isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(isimler,soyisimler):
    print(i,j)


#%%

'''
    Enumerate Fonksiyonu
    
'''
liste = ["Elma","Armut","Muz","Kiraz"]

# sonucu [(0,'Elma'),(1,'Armut'),(2,'Muz'),(3,'Kiraz')] yapmak istiyoruz.

sonuç = list()

i = 0

for a in liste:
    
    sonuç.append((i,a))
    i +=1
print(sonuç)    

'''
Yani aslında burada herbir elemanı indekslerle numaralandırıyor ve demet çiftleri oluşturuyoruz. 
for döngüsü yazarken bazen hem elemanları hem de indeksleri almak isteyebiliriz.
Böyle bir durumda numaralandırma işlemi yapan enumerate fonksiyonunu kullanabiliriz.
'''
liste = ["Elma","Armut","Muz","Kiraz"]
list(enumerate(liste))
   
# Örneğin bir listenin çift indekslerini(0,2,4) enumerate kullanarak nasıl yazdırabiliriz ?
liste = ["a","b","c","d","e","f","g"]

for index,eleman in enumerate(liste):
    if (index % 2 == 0):
        print("Eleman: ",eleman)    
    
    
    
# enumerate, for döngülerinde çoğu zaman işlerimizi oldukça kolaylaştırmaktadır
#%%

# All() ve Any Fonksiyonları

'''

all() fonksiyonu bütün değerler True ise True, en az bir değer False ise False sonuç döndürür.


'''
def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True
# Bütün değerler True ise True en az birisi False ise False döndürmek istiyoruz.
liste = [True,False,True,False,True]

hepsi(liste) # En az birisi False

liste = [1,2,3,4,5] # Daha önceden biliyoruz. 0' haricinde bütün sayılar True sayılmaktadır.

hepsi(liste) # Hepsi True    
    
def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False
# Herhangi bir değer True ise True, Hepsi False ise False döndürmek istiyoruz.  

liste = [True,False,True,False,True]
herhangi(liste)
    
liste1 = [0,0,0,0,0,0,0] # Bütün değerler False , 0 = False
herhangi(liste1)    
    
# all() fonksiyonu bütün değerler True ise True, en az bir değer False ise False sonuç döndürür.
all(liste) 
    
# any() fonksiyonu bütün değerler False ise False, en az bir değer True ise True sonuç döndürür.
any(liste)
any(liste1)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    