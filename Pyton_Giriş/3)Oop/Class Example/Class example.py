class Calisan(object):
    
    zam_orani = 1.8
    counter = 0
    def __init__(self , isim , soyisim , maas):
        self.name=isim
        self.surname=soyisim
        self.salary=maas
        self.email=isim+soyisim+"@asd.com"
        
        Calisan.counter = Calisan.counter + 1
        
    def giveNameSurname(self):
        return self.name +" "+self.surname
    def zam_yap(self):
        self.salary =  self.salary + self.salary*self.zam_orani
    
    
calisan1 = Calisan("ali" , "veli" , 1000)
print("ilk maas : ", calisan1.salary)   
calisan1.zam_yap()
print("yeni maas :",calisan1.salary) 
    
calisan2 = Calisan("ahmet" , "hakan" , 2000)
calisan3 = Calisan("mehmet" , "yavuz" , 3000)
calisan4 = Calisan("enes" , "berke" , 4000)

liste = [calisan1, calisan2 , calisan3 , calisan4]

max_maas = -1
index = -1
for each in liste:
    if(each.salary > max_maas):
        max_maas = each.salary
        index = each
                
print( "en cok maas alan kisi :",index.giveNameSurname(), " ----  maası :",max_maas)
print("Sirkette calisan kisi sayisi :" , Calisan.counter)

#%%

# Class örneği

class Araba():
    
    def __init__(self,model = "Bilgi Yok",renk = "Bilgi Yok"  ,beygir_gücü = "Bilgi Yok",silindir ="Bilgi Yok"): # __init__ fonksiyonu python tarafından otomatik olarak oluşturuluyor.
        # self anahtar kelimedir farklı objeler kullanmak için gereklidir. Yok sa her obje aynı bilgilere sahip olur..
        print("Init Fonksiyonu çağrıldı .")
        self.model = model
        self.renk = renk
        self.beygir_gücü = beygir_gücü
        self.silindir = silindir
        

araba = Araba(model = "Volvo" ,renk = "siyah" , beygir_gücü = 250 ,silindir = 8)
araba1 = Araba(model = "VW" ,renk= "Beyaz" ,beygir_gücü= 275 ,silindir = 6)

araba2 = Araba(model = "VW") # default olarak tanımlanmış olan renk ve diğer bilgileri kullanıyor.

#%%

# OOP de method kıllanımı

class Yazılımcı():
    
    def __init__(self,isim, soyisim , numara , maas , diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller
        
    def bilgilerigöster(self):
        print('''
              
        Yazılımcı objesinin özellikleri 
        
        isim : {}
        
        soyisim = {}
        
        numara = {}
       
        maas = {}
        
        bildiği diller = {}
        
        '''.format(self.isim,self.soyisim,self.numara,self.maas , self.diller))
        
        
    def zam_yap(self,zam_miktarı):
        print("Zam yapıldı")
        print("Eski maas : {}" .format(self.maas))
        self.maas += zam_miktarı 
        print("Yeni maas : {}" .format(self.maas))
    
    def yeni_dil(self , yeni_dil):
        
        print("Yeni dil eklendi .")
        self.diller.append(yeni_dil)
        
        

yazılımcı1 = Yazılımcı("İsmet" , "Sancaklı" , 159 , 5800 , ["Python" , "C" , "C++"])

yazılımcı1.bilgilerigöster()

yazılımcı1.yeni_dil("Java")
yazılımcı1.bilgilerigöster()


yazılımcı1.zam_yap(250)

#%%

# Intheritence

class çalisan():
    
    def __init__(self,isim, soyisim ,  maas , departman):
        self.isim = isim
        self.soyisim = soyisim        
        self.maas = maas
        self.departman = departman
        
    def bilgilerigöster(self):
        print("Calisan sinifinin bilgileri\n")
        
        print(" Isim : {}\n Soyisim : {}\n Maas : {}\n Departman : {}\n ".format(self.isim , self.soyisim , self.maas , self.departman))


    def departmanDegistir(self , yeni_departman):
        print("Departman Güncellendi")
        self.departman = yeni_departman
        print("Yeni Departman : {}\n".format(self.departman))
        
        
class yönetici(çalisan):
    
    def zam(self,zam_miktarı):
        
        print("Zama yapıldı")
        self.maas += zam_miktarı
        print("Yeni maas : {}\n ".format(self.maas))
        
    
    
   
yönetici1 = yönetici("ismet" , "sancaklı" , 5000 , "AR-GE") 
yönetici1.bilgilerigöster()

yönetici1.departmanDegistir("Finans") # Departman değiştirdik
yönetici1.bilgilerigöster()

dir(yönetici) # Burada sahip olduğumuz fonksiyonları bize gösteriyor.

yönetici2 = yönetici("Hilal", "Sancaklı" , 5500 , "İnsan Kaynakları")
yönetici2.bilgilerigöster()
print("\n\n")
yönetici2.departmanDegistir("Finans Müdürü")
yönetici2.zam(1500)

yönetici2.bilgilerigöster()

#%%

# Overriding (İptal Etme)

class çalisan():
    
    def __init__(self,isim, soyisim ,  maas , departman):
        self.isim = isim
        self.soyisim = soyisim        
        self.maas = maas
        self.departman = departman

    def bilgilerigöster(self):
        print("Calisan sinifinin bilgileri\n")
        
        print(" Isim : {}\n Soyisim : {}\n Maas : {}\n Departman : {}\n ".format(self.isim , self.soyisim , self.maas , self.departman))


class yönetici(çalisan): # burada artık mirasçı klasın init fonksiyonu ile kendi özelliklerini oluşturuyoruz.
    
    def __init__(self,isim,soyisim,maas,departman, kişisayısı):
        print("Yönetici sınıfının init  fonksiyonu çalıştı..")
        
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.departman = departman
        self.kişisayısı = kişisayısı
        
    def bilgilerigöster(self):
        print(" Isim : {}\n Soyisim : {}\n Maas : {}\n Departman : {}\n Sroumlu olunan kişi sayısı : {}\n".format(self.isim , self.soyisim , self.maas , self.departman, self.kişisayısı))

'''
Burada yönetivi mirasçısın içerisinde tekrar oluşturduğumuz aynı isimli fonksiyonlar ile yönetici class ına ait 
bir nesne tanımladğımız zaman parent ın fonksiyonlarını override etmiş oluyoruz.  
'''
    
    def zam(self,zam_miktarı):
        
        print("Zama yapıldı")
        self.maas += zam_miktarı
        print("Yeni maas : {}\n ".format(self.maas))

yön = yönetici("İsmet" , "Sancaklı", 5000,"Bilişim", 100)
yön.bilgilerigöster()
#%%

# Süper anahtar kelimesi

'''
Süper anahtar kelimesi miras aldığmız sınıfın sahip olduğu metodları mirasçıların da kullanması için kullanılır.
Yani  hem çalışan sınıfında hemde yönetici sınıfında ortak olanları 2 defa yazmamıza gerek kalmadan yazabiliriz.

'''

class çalisan():
    
    def __init__(self,isim, soyisim ,  maas , departman):
        self.isim = isim
        self.soyisim = soyisim        
        self.maas = maas
        self.departman = departman
        
    def bilgilerigöster(self):
        print("Calisan sinifinin bilgileri\n")
        
        print(" Isim : {}\n Soyisim : {}\n Maas : {}\n Departman : {}\n ".format(self.isim , self.soyisim , self.maas , self.departman))


    def departmanDegistir(self , yeni_departman):
        print("Departman Güncellendi")
        self.departman = yeni_departman
        print("Yeni Departman : {}\n".format(self.departman))
        
        
class yönetici(çalisan): # burada artık mirasçı klasın init fonksiyonu ile kendi özelliklerini oluşturuyoruz.
    
    def __init__(self,isim,soyisim,maas,departman, kişisayısı):
        
        super().__init__(isim,soyisim,maas,departman)
        print("Yönetici sınıfının init  fonksiyonu çalıştı..")              
        self.kişisayısı = kişisayısı
        
    def bilgilerigöster1(self):
        super().bilgilerigöster()
        #print(" Isim : {}\n Soyisim : {}\n Maas : {}\n Departman : {}\n Sroumlu olunan kişi sayısı : {}\n".format(self.isim , self.soyisim , self.maas , self.departman, self.kişisayısı))
        print("Sorumlu olunan kişi sayısı : {}\n".format(self.kişisayısı))
'''

Burada parentın sahip olduğu __init__() ve bilgilerigöster() fonksiyonlarına super anahtar kelimesi ile tekrar
yazmaktan kurtularak ulaşmış olduk.
'''
       

ob_yönetici = yönetici("Ali" , "Veli" , 4000 , "Finans" , 120)
ob_yönetici.bilgilerigöster1()


#%%

'''
OOP de özel metodlar.

'''

class Kitap():
    
    def __init__(self , isim , yazar , sayfa_sayisi , tür):
        print("init fonksiyonu çalışıyor")
        self.isim= isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tür = tür
        
    def __str__(self):
        # Return kullanmamız gerekli
        
        return  "İsim : {}\nYazar : {}\nSayfa_sayisi : {}\nTür : {}\n".format(self.isim,self.yazar,self.sayfa_sayisi,self.tür)
        
    def __len__(self): # Python init ve str gibi kendisi oluşturmaz len metodunu.
        # Return kullanmamız gerekli
        return  self.sayfa_sayisi


    def __del__(self):
        print("Kitap klasının objesi siliniyor.... ")
        
        
kitap = Kitap("Enigma" , "Andrew Hodges" , 650 , "Biyografi")

print(kitap)
len(kitap)
del(kitap) # Kitap nesnesi silindi.


























