# sqlite veri tabanı


'''
Veritabanı nedir ?¶
Veritabanı uygulamalarımızda , websitelerimizde veya en genel anlamda programlarımızda gerekli olan bilgileri depoladığımız bir yapıdır.
Örneğin , Facebook'un kullanıcıları, gönderileri tuttuğu veritabanları gibi. 
Günümüzde kullanılan bazı veritabanı türleri şunlardır;

      Relational Database (İlişkisel Veritabanları) : Tablolardan oluşur. Mysql, Sqlite vs.
      DocumentBased Database (Doküman Veritabanları) : Dokümanlardan oluşur. MongoDb, Azure DocumentDb
                               //
                               //
                               //

Bizim bu bölümde inceleyeceğimiz veritabanı Sqlite ilişkisel bir veritabanıdır ve bu veritabanı tablolardan oluşur. 
Her bir tablo veritabanında belli gruplanmış verileri tutar.
'''


# Tablo Oluşturma 
import sqlite3

con = sqlite3.connect("kütüphane.db")
#kütüphane.db veritabanını oluşturup bağlanıyoruz.
#Eğer öyle bir veritabanı varsa bağlanıyoruz. Bağlantıyı con isimli bir değişkene atıyoruz.

#Database üzerinde Sql sorgularını çalıştırmak için cursor bir tane imleç oluşturuyoruz. 
cursor =  con.cursor()


def tablo_oluştur():
    
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")# Sorguyu çalıştırıyoruz.
    con.commit() # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.

tablo_oluştur()
con.close()  
#%%


# veri ekleme 
import sqlite3

con = sqlite3.connect("kütüphane.db")
#kütüphane.db veritabanını oluşturup bağlanıyoruz.
#Eğer öyle bir veritabanı varsa bağlanıyoruz. Bağlantıyı con isimli bir değişkene atıyoruz.

#Database üzerinde Sql sorgularını çalıştırmak için cursor bir tane imleç oluşturuyoruz. 
cursor =  con.cursor()

#Kullanıcıdan almadık kendimiz veri ekledik.
def veri_ekle(): 
    cursor.execute("INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    # Sorgu girilirken büyük küçük harf farketmez.
    con.commit() # sorgunun çalışması için gerekli.

veri_ekle()

#Veritabanı işlemlerinin sonunda con.close() ile bağlantımızı koparıyoruz.
con.close()  

#%%

# kullanıcıdan alınan verinin eklenmesi

import sqlite3

con = sqlite3.connect("kütüphane.db")
#kütüphane.db veritabanını oluşturup bağlanıyoruz.
#Eğer öyle bir veritabanı varsa bağlanıyoruz. Bağlantıyı con isimli bir değişkene atıyoruz.

#Database üzerinde Sql sorgularını çalıştırmak için cursor bir tane imleç oluşturuyoruz. 
cursor =  con.cursor()


def tablo_oluştur():
    
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")# Sorguyu çalıştırıyoruz.
    con.commit() 
def kullanıcıdan_veri_girisi(isim , yazar, yayınevi , sayfa_sayisi): # Kullanıcıdan alınan veririnin tabloya eklenmesi.
    con.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()


isim= input("İsim : ")
yazar = input("Yazar :")
yayınevi = input("Yayınevi :")
sayfa_sayısı = int(input("Safya :"))
kullanıcıdan_veri_girisi(isim , yazar, yayınevi , sayfa_sayısı)
# veri_ekle()
#tablo_oluştur()
    
#Veritabanı işlemlerinin sonunda con.close() ile bağlantımızı koparıyoruz.
con.close()     

#%%


# Tablodaki verileri çekme . tablodan veri okuma
'''
1-Select * From kitaplık - Tablodaki tüm bilgileri almamızı sağlar.

2-Select İsim,Yazar From kitaplık Tablodaki tüm bilgileri sadece İsim ve Yazar özelliklerini almamızı sağlar.

3-Select * From kitaplık where Yayınevi = 'Everest' Sadece Yayınevi özelliği Everest olanları alır.
'''
import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık") # Bütün bilgileri alıyoruz.
    data = cursor.fetchall() # Veritabanından bilgileri çekmek için fetchall() kullanıyoruz.fetchall bilgileri liste tipinde döndürüyor.
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
    # con.commit() işlemine gerek yok. Çünkü tabloda herhangi bir güncelleme yapmıyoruz.
verileri_al()
con.close()
#%%

'''
2. Sorgu

2-Select İsim,Yazar From kitaplık Tablodaki tüm bilgileri sadece İsim ve Yazar özelliklerini almamızı sağlar.
'''

import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık") # Sadece İsim ve Yazar özelliklerini alıyoruz.
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
verileri_al2()
con.close() 

#%%

'''
3. Sorgu
3-Select * From kitaplık where Yayınevi = 'Everest' Sadece Yayınevi özelliği Everest olanları alır. 

'''
import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ?",(yayınevi,)) # Sadece yayınevi ,Everest olan kitapları alıyoruz.
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
verileri_al3("Everest")
con.close()

#%%

'''
Verileri Güncelleme¶
Tablodaki verileri güncelleme için şöyle bir sorgu kullanabiliriz.

Update kitaplık set Yayınevi = 'Everest' where Yayınevi = 'Doğan Kitap' --
 Yayınevi 'Doğan Kitap' olan kitapların Yayınevi bilgilerini 'Everest' e günceller.

Şimdi isterseniz bu sorguyu çalıştırdığımız kodumuzu yazalım
'''


import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ?",(yayınevi,))
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verigüncelle(yayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi =  ?",("Panama",yayınevi))
    con.commit()

verigüncelle("Yapı Kredi")
con.close() 

# Yayınevi everest olan kitapların yayınevlerini Panama yaptık.

#%%

'''
Verileri Silme
Tablodaki verileri silme için şöyle bir sorgu kullanabiliriz.

Delete From kitaplık where Yazar = 'Ahmet Ümit' -- Yazar özelliği 'Ahmet Ümit' olan kitapları tablodan siler.
'''

import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ?",(yayınevi,))
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verigüncelle(yayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi =  ?",("Everest",yayınevi))
    con.commit()
def verilerisil(yazar):
    cursor.execute("Delete  From kitaplık where Yazar = ?",(yazar,))
    con.commit()
  

verilerisil("Ahmet Ümit")
verileri_al()
con.close()
















