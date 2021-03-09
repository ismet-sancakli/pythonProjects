
'''
Hatalar ve istisnalar
'''
a = 10
zero = 0



#if(zero == 0):
#    print(a)
#else:
#    b = a/zero


try:
    b = a/zero
except ZeroDivisionError: # Sıfıra bölünememe hatası.
    b =0
    
#%%
    



try:    
    a = int(input("Sayı 1 :"))
    b = int(input("Sayı 2 :"))
    print(a/b)
    
    #print("Program burada")
except (ValueError,ZeroDivisionError): # olma ihtimali olan hatalar için kullanıcıya daha güzel bilgi vermek için kullanabiliriz.
    print("Hata Oluştu")
    print("Inputları kontol ediniz")
    print("Bir sayı 0'a bölünemez")
    print("Bloklar sona erdi")
    
#%%
    
try:    
    a = int(input("Sayı 1 :"))
    b = int(input("Sayı 2 :"))
    print(a/b)
    
    #print("Program burada")
except ValueError: 
    print("Hata Oluştu")
    print("Inputları kontol ediniz")
    
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez")

finally : # Burası her türlü çalışacaktır. Biz mutlaka çalışmasını istediğimiz kodları buaraya yazıyoruz.. 
    print("Finally bloğu çalıştı")


print("Bloklar sona erdi")
    
    
#%%

'''
Hata Fırlatmak
'''

def terscevir(s):
    if (type(s) != str ):
        raise ValueError("Lütfen string tipinde bi değer giriniz ") 
    else:
        
        return s[::-1]
print(terscevir("Python"))
    
#print(terscevir(12))
 
try :
    print(terscevir(12))
    
except ValueError:
    print("Fonksiyon hata verdi.")
    
#%%
    #******** EXAMPLE ******
   
    # Listedeki elemanların sadece int tipinde olanları yazdıran kod
    
liste = ["345" , "asd14" , "asdfgfsdgf" ,   "5645"]



for eleman in liste :
    
    try :
        eleman = int(eleman)
        print("Elaman : {}".format(eleman))

    except:
        pass
    
#%%
        # *********EXAMPLE***********
        '''Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. 
            Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün. 
            Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın. 
            Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve 
            liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.
        '''
    
    
def ciftMi(sayı):
    
    
    if (sayı % 2 == 0):
        return sayı

    else:
        raise ValueError
        
liste1 = [20,3,12,11,5,6,4,88,99,77,66,121]

for i in liste1:
    try :
        print(ciftMi(i))
    except ValueError:
        pass
        
   

    
    
    
    
    




     