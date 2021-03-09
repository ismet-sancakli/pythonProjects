from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def walk(self): pass

    @abstractmethod
    def run(self): pass        
        
class Bird(Animal):
     
    
    def __init__(self):
        print("Bird")
        
    def walk(self):
        print("walk")
        
    def run(self):
        print("run")
        
b1 = Bird()
b1.run()
b1.__init__()  
b1.walk()      
