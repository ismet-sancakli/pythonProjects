
# %%
class Square(object):
    edge = 5
    
    def area(self):
        sonuc = self.edge * self.edge # buradaki selfin anlamı class içindekileri kullanama izni veriyor bize.
        print(sonuc)
    
s1 = Square() # burada s1 adında bir nesne oluşturduk
print(s1)
print(s1.edge)
print(s1.area())
s1.area()
s1.edge=7
s1.area()
print("yeni kenar : ",s1.edge)
s1.area()
s1.edge = 10
s1.area()
# %%

class Employee():
    
    age = 23
    salary = 1000 # $
    
    def ageSalaryRatio(self):
        a = self.age / self.salary
        print("metod yöntemi :",a)

e1 = Employee()
e1.ageSalaryRatio()       

def ageSalaryRatio(age, salary):    
    a = age / salary
    print("function : ",a)
ageSalaryRatio(30,3000)
# %%
 # Constructor or Initializer
 
class Animal(object):
    def __init__(self, isim , yas): # burası Constructor için kullanıyoruz burası main kısmında değişkenleri değiştirmemize yarıyor
        self.name = isim
        self.age = yas
        
    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name

a1 = Animal("dog" , 5)
a2 = Animal("cat" , 4)
a3 = Animal("lion", 6)
print(" name : ",a3.getName(),"age : ", a3.getAge())        
print("your animal age is : ",a2.getAge(), "your animal name is :",a2.getName())
print(a3.getName())
print(a3.getName())
        
