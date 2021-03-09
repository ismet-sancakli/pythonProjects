# Inheritance Project

# Parent 
class Webside(object):
    def __init__(self , isim , soyisim):
        self.name = isim
        self.surname = soyisim
        
    def toString(self):
        print("Webside method")
    
    def loginInfo(self):
        print(self.name + " " + self.surname)
        
# child 1
class webside1(Webside):
    def __init__(self , isim , soyisim, ids):
        Webside.__init__(self, isim , soyisim) # parent constructor ı için böyle yazılmalı.
        self.id = ids
        
    def toString(self):
        print("webside1 (child 1) method")
        
    def loginInfo1(self):
         print(self.name + " " + self.surname + " "+ self.id)
         
# child 2       
class webside2(Webside):
    def __init__(self,isim , soyisim, e_mail):
        
        Webside.__init__(self,isim , soyisim)        
        self.e_mail = e_mail  
        
    def toString(self):
        print("webside2 (child 2) method")
        
    def loginInfo2(self):
         print(self.name + " " + self.surname + " " + self.e_mail)
         
        
p1 = Webside("ismet" , "sancaklı")
p1.loginInfo()
p1.toString()        

p2 = webside1("ismet" ,"sancaklı" , "123456")
p2.loginInfo1()
p2.toString()

p3 = webside2("ismet" , "sancaklı" , "ismet@hotmail.com")
p3.loginInfo2()
p3.toString()




