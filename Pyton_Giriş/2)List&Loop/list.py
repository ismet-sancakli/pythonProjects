
# List

liste = [1,2,3,5,6,4]
#
print(liste[0])
print(liste[-1])
print(liste[-2])

liste2=[2,5,6,9,8,6,1,2]

liste.extend(liste2)
print("extend list: " , liste) # extend liste listeleri toplamak ile aynı işlmei yapıyor.

print(liste2*3)  # burada listeyi tam sayılarla çarpabiliyoruz ancak orijinal listede değişim yaşanmaz

liste2[1] = 10 # Stringlerde olmayan bir özellik olan listelerin elemanlarını değitirebiliyoruz. burada 2. elemanı değişti
print(liste2)
liste2[:2]=[50,23] # 2'ye kadar olan liste elamnlarını değiştirdik. ancak 2. elemanı almadık.
print(liste2)

# List of Methods

# append()
liste2.append("python") # append metodu listenin sonuna eleman eklememizi sağlar.
print(liste2)

#pop()

liste2.pop() # listenin son elemanını listeden atar.
print(liste2)

liste2.pop(2) # index vererek istediğimiz elemanı çıkartabiliriz

#sort()

liste2.sort() # listeyi küçükten büyüğe doğru sıralar.
print(liste2)

liste2.sort(reverse=True) # büyükten küçüğe doğru sıralama yapar.
print(liste2)

# aynı şekilde alfabetik sıralamada yapılabilir.

liste3=[[1,2],[3,4],[5,6]] # iç içe listeler
print(liste3[1][1])



#%%
# tuple (demetler)
# listeler en temel farkı değiştirilemez olmalarıdır.

demet = (1,0,2,3,6,5,9,11)
type(demet)
# listelerde yaptığımız ayırma ters çevirme işlemleri uygulanabilir.
print(demet)

demet2 = (1,1,1,1,2,3,6,5,5,5,6,8,4,32,2,2)
demet2.count(2) # tuple da tekrar eden sayıları bulur.

demet3 = ("Python", "C" ,   "C++" )
demet3.index("C") # aradığımız elemanın bize hangi indexte olduğunu söylüyor.

# Değiştirilmeyen değerler kullanılıyorsa tuple kullanılmalıdır. 

#%%
# Dictionary

dictionary = {"ali":23,"ahmet":22,"mahmut":55}
type()
len(dictionary)  # bize sözlük veri tipinin içinde kaç tane eleman olduğunu söyler..
print(dictionary["ali"])

dictionary["mehmet"] = 32
# Sözlüklerde eleman ekleme herhangi bir bölüme yapılabilir biz index yerine anahtar kelime kullandığımız için problem olmuyor.
print( dictionary)

a = {"bir" : [1,2,3,4] , "iki" : [[1,2],[5,6],[8,9]] , "üç" : 15}
a["iki"]
a["iki"][2] = [10,11] 

a.keys() # a sözlüğündeki anahtarları bize veriyor.
a.values() # anahtar kelimelerin sahip olduğu değerleri bize döndürür.
a.items() # a sözlüğünün içindekileri demetler(tuple) olarak bizim karşımıza çıkarıyor.

def deneme():
    dictionary= {"ali":23,"ahmet":22,"mahmut":55}
    return dictionary

dic=deneme() 
print(dic)
print(dictionary.keys()) # burada bize sözlükteki anlamı olan ilk kelimeler verilir mesela burda ali nin anlamı 23 tür.
print(dictionary.values()) # burası sadece anlamları taşıyan bir liste gibi düşünğlebilir. (23, 22, 55)
print(dic["ali"]) # burada bize ali ögesinin sözlükteki karşılığını verir.

#%%

# Kullanıcıda girdi almak (Input Function)
a = input("Please enter number :") 
print("It is entered number by user ",a)

type(a)
print(a*3)

# input fonksiyonunu kullanırken dikkat etmemiz gereken durum input bize girilen değeri her zaman string olarak döndürür.

b = int(input("Please enter the number :"))
print(b*5)

x=int(input("Birinci sayıyı giriniz :"))
y=int(input("ikinci sayıyı giriniz :"))
print("Toplam :", x+y)






#%%
# conditionals
# if - else

var1 = 10
var2 = 20

if(var1 > var2):
    print("var1 buyktur")
elif(var1  == var2):
    print("esitler")
else:
    print("var2 buyuktur")
    
liste = [1,2,3,4]

value = 51

if value in liste:
    print("evet {} degeri listenin içindedir".format(value))
else:
    print("hayır {} deegeri listenin içinde degildir".format(value))

dic_val = dictionary.values()

if 23 in dic_val:
    print("evet")
else:
    print("hayir")
#%%

    #QUIZ ÖNEMLİ !!!! # Bulunduğumuz yılın hangi yüzyıla ait olduğunu bulma örneği.
    
    # 1. çözüm
yıl=input("yıl giriniz:")

if(int(yıl)<1000):
    print("bulundugunuz yüzyıl : ",int(yıl[0])+1,"yy")
if(len(yıl)>3):
    print("bulundugunuz yüzyıl : ", int(yıl[0:2])+1,"yy")    
    
   # 2. çözüm

def century_year(year):
    str_year = str(year)
    if(len(str_year)<3):
        return 1
    elif(len(str_year) == 3):
        if(str_year[1:3] == "00"):
            return int(str_year[0])
        else:
            return int(str_year[0])+1
    else:
        if(len(str_year[2:4]) == "00"):
            return int(str_year[:2])
        else:
            return int(str_year[:2])+1
       
#%%
            #   FOR LOOP
for each in range(1,15):
    print(each)
for a in "ankara ist".split():
    print(a)

liste = [1,2,3,55,558,66]
print(sum((liste)))

count = 0
for a in liste:
    count = count + a
print(count) # pyton da boşluklara dikkat et çünkü sonucu etkiliyor burada print boşluk olmadan yazılırsa for un dışında sayılır.
    
#%%
        # WHILE LOOP 
#i = 0
#while(i < 5 ):
#    print(i)
#    i = i+1
#    
liste3 = [1,2,3,5,6,9,8,7,44,55]
 
sinir = len(liste3)
print(sinir)
print(sum(liste3)) # sum fonksiyonu python da hzır bulunur ve listedeki elemanları toplar. 
index = 0
count = 0
while(index < sinir): # listedeki elemanları while döngüsü ile topluyoruz.
    count = count + liste3[index]
    index = index + 1
print(count)

#%%


            # Quiz 3 listenin en küçük elemanını bul.

listem = [1,2,3,4,5,6,4,23,67,21,-500,23,-1500,67,-501]

a = listem[0]
index = 1
for each in listem:
    if(a < listem[index]):
        index = index + 1
    else:
        temp = a 
        a = listem[index]
        listem[index] = temp
print("en küçük eleman :",a) # buradaki print fonksiyonu else içinde olursa a değişimden sonra ki kendisinden küçük olan bütün değerleri yazar.
        
#%%
        # Quiz 3 2. çözüm

listem = [1,2,3,4,5,6,4,23,67,21,-500,23,451,67]    

mini = 100000
for each in listem:
    if(each < mini):
        mini = each
    else:
        continue
print("listenin en küçük elemanı ",mini)
#%%

listeci = [x**2 for x in (0,2,3,4,5,6,7,8)]
listeci1 = [a*3 for a in (-100,2,3,5,6,9,8,7)]

dilim = listeci[2::2]
print("listecinin elamanları index 2 den başlar ve 2'şer atlayarak devam eder", dilim)
listeci.extend(listeci1)
print("listeci  listesine listeci1 eklendi:",listeci)
listeci.pop(5) # 5. indexteki eleman pop tarafından alındı.
listeci.reverse()
print("listecinin ters yazımı : ", listeci)
listeci.reverse()
print("listecinin tekrar ters yazımı : ",listeci)

print("listeci1 'in min elamnı : {}".format(min(listeci1)))
print("listeci1 ' in max elemanı : {}".format(max(listeci1)))    # min ve max hazır fonksiyonları listedeki en küçük ve en büyük elemanı döndürürler.
print("listeci'nin max elamnı : {}".format(max(listeci)))
print("listeci' nin min elamnı : {}".format(min(listeci)))       

#%%
range(0,20)
print(*range(0,20,5))       

 
for i in range(1,20):
        print("*" * i ) # burada i nin hemen önündeki yıldız range aralığında i gezerken onu yazdırması için.
        
        

#%%     
    # List Comprehension
    
liste=[1,2,3,4,5]
liste1=[i for i in liste] # liste yi liste 1 e ekledik.
print(liste1)

liste2=[3,4,5]
liste3=[a*2 for a in liste2]
print(liste3)

liste4=[(1,2),(3,4),(5,6)] # listenin içinde tuples(demetler) var
liste5=[i*j for i,j in liste4]
print(liste5)

s="python"
liste6=[i*3 for i in s]
print(liste6)

liste7=[[1,2,3],[3,4,5,6,7,8],[9,10,11,12,13,14]] # burada listenin içindeki listelerin elemanlarına teker teker ulaşılabilir.
for i in liste7:
    for x in i:
        print(x)

liste8=[[1,2,3],[3,4,5,6,7,8],[9,10,11,12,13,14]] # yukarıda ki işlemin lisr comprehension şeklinde yapılmış hali.
liste9 = [x for i in liste8 for x in i]
print(liste9)

#%%
# Listede Tekrar eden elemanları yok etmek.
# 1. yol
a=[1,2,5,3,1,1,15,14]
a=list(set(a))
print(a)

# 2. yol
a=[1,2,5,3,15,15,15,14]
b = []
for i in a:
    if i not in b:
        b.append(i)

print(b)











