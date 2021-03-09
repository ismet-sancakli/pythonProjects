
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("pokemon.csv")
data.info()

data.corr()
f,ax = plt.subplots(figsize=(18,10))
sns.heatmap(data.corr(), annot=True , linewidth = 0.5, fmt = '.1f', ax=ax)# Heatmap fonksiyonu bize verilerin tablo halindeki görsel durumunu söyler
    
data.head(10)
#data.Speed.plot(kind= 'hist', bins = 50 , figsize = (15,15))
print(data.Speed.plot(kind= 'hist', bins = 100 , figsize = (15,15)))

dictionary = {'spain' : 'madrid' , 'usa': 'vegas'}
print(dictionary.keys())

dictionary['spain'] = 'barcelona'   # burada sözlüüğe yeni eleman ekliyoruz  
print(dictionary)

dictionary['france'] = 'paris'      # sözlüğe yeni eleman eklemek için kullanıyoruz.
print('france' in dictionary )
print('germany' in dictionary )

del dictionary['spain']             # key silmek için kullanıyoruz.
print(dictionary)

dictionary.clear()                  # bütün sözlüğün içini siler 
print(dictionary)

#del dictionary                      # daha önceden sözlüğü sildiğimiz için burada hata verir.
#print(dictionary)


# 1- Filtering Pandas Data Frame 
x= data['Defense']>200              # Defansı 200 den büyük olanları alıyoruz
data[x]                             # sadece 200 den büyük olanları yazdırır.

data[np.logical_and(data['Defense']>200 , data['Attack']>100)] # ikiside filtreleme işlemi görmektedir

data[(data['Defense']>200) & (data['Attack']>100)]


# 2- While an For Loops 

liste = [1,2,3,4,5]
for i in liste:
    print("i is " , i)
print(' ')

for index , value in enumerate(liste):          # burada enumerate bizim listedeki hem değerleri hem de indexleri kullanmamızı sağlıyor 
    print(index, ":", value) 
print(' ')    
 
dictionary = {'spain' : 'madrid' , 'usa': 'vegas'} 
for key,value in dictionary.items():            # burada dictionary.items() yukarıdaki enumerate ile aynı işlevi görüyor
    print(key, ":", value)
print(' ')    
     
for index, value in data[['Attack']][0:1].iterrows(): # burada da pandasa erişmek istiyoruz ve iterrows kullanıyoruz.
    print(index, ':',value)                           # [0:1] ilk eleman anlamına geliyor 0 = rows 1 = column (1'e kadar)



































