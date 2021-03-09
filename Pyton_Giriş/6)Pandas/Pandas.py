#%% -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 18:14:18 2019

@author: İSMET
"""

# Pandas 
# 1- pandas data frameler için hızlı ve etkilidir
# 2- pandas kayıp veriler için kullanılarbilir
# 3- csv ve text dosyalarını acip inceleyebiliriz sonucları bu dosya tiplerine rahat  bir şekilde kaydedebilir
# 4- xciling ve indexing numpy a göre daha kolay kullanılır
# 5- reshabe ile  veri daha etkili bir şekilde kullanılabilir
# 6- time series analizde kullanılırız
# **7- pandasın en önemli özelliği hızıdır 

import pandas as pd

dictionary = {"NAME":["ali", "veli" , "ahmet" , "mahmut" , "hilal" , "filiz"],
              "AGE" : [15,16,17,18,19,20] , 
              "SALARY" : [1000,2000,3000,4000,5000,6000]}

dataFrame1 = pd.DataFrame(dictionary) # excel dosyası şeklinde bir dataFrame oluşturduk

head = dataFrame1.head() # data frame içindeki baştan 5 satırı bize verir // ayrıca parantezin içine kaç tane yazarsak bize o kadarını gösterir
tail = dataFrame1.tail() # data frame içindeki sondan 5 satırı bize verir // ayrıca parantezin içine kaç tane yazarsak bize o kadarını gösterir
# head ve tail kullanmamızın sebebi ilk olarak bize gelen datanın içeriğinin mantığını öğrenemektir
 
print(head)
print(tail)    
#%%
# Pandas Basics Methods  
print(dataFrame1.columns)
print(dataFrame1.info()) # object demek aslında string tutuyor demek
print(dataFrame1.dtypes) # bu genel olarak hangi sütun hangi veri tipini almış onu gösteriyor

print(dataFrame1.describe()) # describe sadece numeric feature ları alır numeric feature = (age, salary)
                            # ve aynı zamanda bize sayılsal sütunlar hakkında ortalama min max gibi birçok özellik bilgisi verir   

#%% 
# Indexing & Slicing 

print(dataFrame1["NAME"]) # sadece isimleri aldık
print(dataFrame1["AGE"])
print(dataFrame1.AGE)

dataFrame1["New_Feature"] = [-1,-2,-3,-4,-5,-6]
print(dataFrame1.New_Feature)

print(dataFrame1.loc[:,"AGE"]) # bütün satırlar dahil sadece age sutünunu al demek

print(dataFrame1.loc[0:3,"AGE"]) # burada bütün satırlar içinde sadece Age sütunun 0 ile 3 arasındaki (3 dahil) sayıları alır
                                 # numpy ve list te 0:3 dırımında 3 dahil olmuyor
                                 
print(dataFrame1.loc[0:1,"NAME":"SALARY"]) # 0 ile 1. satırları ve nameden salary e kadar olan sütunları yazdır

print(dataFrame1.loc[0:1,["NAME","SALARY"]]) # yukarıdakinden farklı olarak 0 ile 1. satırları alır sadece name ve salary sütunlarını yazar
 
print(dataFrame1.loc[::-1,:]) # burası ise data frame i tersten yazdırır. 

print(dataFrame1.loc[:,:"AGE"]) # tüm satırları age e kadar olacak şekilde yazdır AGE dahil !!!!

print(dataFrame1.iloc[:,0:2]) # buradaki 2 index i 2 olan sütunu gösterir. ve iloc dediğimiz için int istediği için sayı kullandık 
                                # iloc deme location ı integer olarak göster anlamına gelir

#%%
# Filtering Pandas Data Frame
filtre1 = dataFrame1.SALARY > 2000
filtrelenmis_data = dataFrame1[filtre1]

filtre2 =dataFrame1.AGE < 20
filtre3 =dataFrame1.New_Feature < -4 
print(dataFrame1[filtre1 & filtre2 & filtre3]) 

print(dataFrame1[dataFrame1.New_Feature > -2  ])

#%%
# List Comprehension

#import numpy as np
#ort_maas = np.mean(dataFrame1.SALARY)

mid_salary = dataFrame1.SALARY.mean()

dataFrame1["MAAS SEVİYESİ "] = ["yüksek" if (mid_salary < each) else "düsük" for each in dataFrame1.SALARY]
# maas seviyesine göre ayrımım burada list comprehension kullanarak yaptık

#for each in dataFrame1.SALARY:
#    if(mid_salary < each):
#        print("düsük")
#    else:
#        print("yüksek")
        
dataFrame1.columns = [each.lower() for each in dataFrame1.columns]  # sütündaki ifadeleri küçük harflerle yazdık

dataFrame1.columns =  [ each.split()[0]+"__"+each.split()[1]  if(len(each.split())) > 1 else each for each in dataFrame1.columns]
# burada sütun isimleri arasında boşluk olanlar için aralarını doldurduk 

#dataFrame1.drop("new-feature" , axis = 1 , inplace = True) # istediğimiz sütunu silmek için kullanıyoruz

#%%
#Concatenating & Drop 


data1 = dataFrame1.head()
data2 = dataFrame1.tail()   

# vertical
data_v_concat = pd.concat([data1 , data2], axis = 0) # axis = 0 olursa yukarıdan aşağı birleştirm yapar

# horizontal
maas = dataFrame1.salary
yas = dataFrame1.age
isim = dataFrame1.name
data_h_concat = pd.concat([isim,yas],axis = 1) # axis = 1 ise yan yana birleştirm yapar

#%%

# Transforming data

dataFrame1["List_Comp"]=[each*2 for each in dataFrame1.age] # list comp yöntemi ile 

# apply() metodu
def multiply(age):             # Transforming Data Metodu kullandık
    return age*2            

dataFrame1["Apply_Method"] = dataFrame1.age.apply(multiply)    
#%%












































 