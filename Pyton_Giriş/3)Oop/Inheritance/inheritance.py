# parent class
class Animal(object):
    
    def __init__(self):
        print("Animal is created")
        
    def toString(self):
        print("Animal")
        
    def walk(self):
        print("Animal walk")
        
# child class

class Monkey(Animal):
    
    def __init__(self):
        
        super().__init__() # use  init of parent(animal) class
        print("Monkey is created")
        
    def toString(self):
        print("Monkey")
      
    def climb(self):
        print("Monkey can climb")
  
class Bird(Animal):
    
    def __init__(self):
        super().__init__() # use init of parent( animal ) class
        print("Bird is created")
        
    def toString(self):
        print("Bird")
         
    def fly(self):
        print("Bird can fly")

b1 = Bird()
b1.fly()
b1.walk()   
b1.toString()
print("--------")      
m1 = Monkey()
m1.climb()
m1.walk()              
m1.toString()   



