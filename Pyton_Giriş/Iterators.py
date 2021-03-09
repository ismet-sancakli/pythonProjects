'''
Iteratorlar en genel anlamıyla üzerinde gezinilebilecek bir objedir ve bu obje her seferinde bir tane eleman döner.

Pythonda kendisinden iterator oluşturabileceğimiz her obje iterable bir objedir..
Örneğin, demetlerden,listelerden ve stringlerden oluşturduğumuz bütün objeler iterable bir objedir.

Bir objenin iterable olması için hazır metodlar olan __iter()__ ve __next()__ metodlarını mutlaka tanımlaması gerekir.

'''

#%%

                            # ITERATOR OLUŞTURMA

'''
Iterator oluşturma
Bir iterator objesini , iterable bir objeden (liste,demet,string vs) oluşturmak için Pythonda iter() fonksiyonunu kullanıyoruz 
ve bu objenin bir sonraki elemanını almak için next() fonksiyonu kullanıyoruz.
'''

liste = [1,2,3,4,5]
 
print(dir(liste)) # __iter__ metodu tanımlı olduğu için listeler üzerinde iterator oluşturabiliriz.


iterator= iter(liste)
next(iterator)
next(iterator)
next(iterator)
next(iterator)
next(iterator)
# next(iterator) # listede ki elemanlar bitti. o yüzden burada hata verir.


l = [1,2,3,4,5]

for i in l:
    print (i)
print("**************") 
# Aşağıda for döngüsünün içindeki iterator çalışma mantığını görüyoruz.
iterator2 = iter(l)

while True:
    try : 
        print(next(iterator2))
    except StopIteration:
        break

#%%
        # KENDI ITERABLE OBJELERIMIZI OLUSTURMAK

class Kumanda():
    def __init__(self,kanal_listesi):
        self.kanal_listesi = kanal_listesi # Kanal Listemiz
        self.index = -1 # İndeksimiz
        
    def __iter__(self):
        return self # iterator oluşturduğumuzda (iter fonksiyonu çağrıldığında )objemizi döneceğiz.
    
    def __next__(self): # next fonksiyonu çağrıldığında burası çalışacak.
        self.index += 1
        if (self.index < len(self.kanal_listesi)):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration        
        
            
kumanda = Kumanda(["Kanal d","Trt","Atv","Fox","Bloomberg"]) # Objemizi oluşturuyoruz.

iterator =  iter(kumanda) # Objemiz iterable olduğu için iterator oluşturulabilir.

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#print(next(iterator)) # listede başka eleman kalmadığı için hata fırlatacaktır. StopIteration hatası. 

for i in kumanda:
    print(i)
        
        
        
        






