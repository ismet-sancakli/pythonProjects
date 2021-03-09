'''
Dosya işlemleri

'''

#  w kipi ile dosya açmak biraz tehlikeli bir durum. Çnkü eğer aynı isimde başka bir dosya varsa içini temizliyor 
#ve veri kkaybına sebep olabilir.

open("bilgiler.txt" , "w")
file = open("bilgiler.txt" , "w")
file.close()
file = open("bilgiler.txt" , "w", encoding = "utf=8") # utf 8 türkçe karakterler için.
file.write("İsmet Sancaklı\n")
file.close()

#%%
# a kipi imleci dosyanın en sonuna götürüyor..


     # utf 8 türkçe karakterler için.
file = open("bilgiler.txt" , "a", encoding = "utf=8")
file.write("abs\n")
file.close()    

file = open("bilgiler.txt" , "a", encoding = "utf=8") # utf 8 türkçe karakterler için.

file.write("Hilal sancaklı\n")
file.close()

file = open("bilgiler.txt" , "a", encoding = "utf=8") # utf 8 türkçe karakterler için.
file.write("Mesut sancaklı\n")
file.close()

#%%

# Dosyalarda kullanılan fonksiyonlar

# ve dosyanın otomatik kapatılması .

# with open("bilgiler.txt" , "a", encoding = "utf=8") as file taslağı dosyları otomatik kapatır.


# imleci hareket ettirmek için seek() fonksiyonunu
# imlecin nerede olduğunu öğrenmek için ise tell() fonksiyonunu kullanıyoruz..

with open("bilgiler.txt" , "a", encoding = "utf=8") as file:
    print(file.tell())
    file.seek(0) # 0 bayta gönderdik imleci
    print(file.tell())

#%%

# Dosyada 5. bayttan başlayarak 10 baytlık yer okuduk.

with open("bilgiler.txt" , "r", encoding = "utf=8") as file:
    file.seek(5)
    icerik = file.read(10)
    print("5. bayttan itibaren 10 bayt okur :")
    print(icerik)
    print("imlecin yeri :")
    print(file.tell())
    file.seek(0) #imlcei başa alır.
    icerik2 = file.read(5)
    print("Baştan itibaren 5 bayt okur :")
    print(icerik2)
    

#%%

# "r+" hem okuma hem yazma işlmi için kullanılır.

with open("bilgiler.txt" , "r+", encoding = "utf=8") as file:
    print(file.read())
    file.seek(10)
    #print(file.read())
    
# Dosyanın sonunda değişiklilk yapmak için 

with open("bilgiler.txt" , "a", encoding = "utf=8") as file:
    file.write("Selim sancaklı\n")

with open("bilgiler.txt" , "r+", encoding = "utf=8") as file:      
    print(file.read())
#%%
    # Dosyanın başında değişiklik yapmak

with open("bilgiler.txt" , "r+", encoding = "utf=8") as file:  
    icindekiler = file.read()
    icindekiler = "hho\n"+icindekiler
    print(icindekiler)
#%%
    # Dosyanın ortasında değşiklik yapmak için.
    
    # readlines() fonksiyonu bizim bize satırı liste halinde dönderiyor 
    # bizde listenin herhangi bir yerine eleman ekleyip for döngüsü ile dosyaya yazacağız.

with open("bilgiler.txt" , "r+", encoding = "utf-8") as file: 
    liste = file.readlines()
    print(liste)
    liste.insert(3,"mfmfmfmfmfmfm\n")
    file.seek(0)
    for i in liste:
        file.write(i) # for kullanarak dosyaya elemanları ekledik
        
#%%
with open("bilgiler.txt" , "r+", encoding = "utf-8") as file: 
    liste = file.readlines()
    print(liste)
    liste.insert(3,"qqqqqqqqqqqqqqwwwwwww\n")
    file.seek(0)
    file.writelines(liste) # for yerine writelines() fonksiyonu kullandık.




#%%
        
with open("bilgiler.txt" , "r+", encoding = "utf=8") as file: 
    print(file.read())










