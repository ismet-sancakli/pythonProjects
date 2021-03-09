# OOP Final Project
"""
1-Sekiller adında bir tane abstract metod olacak bunlar kare ve çember
2-bu şekillerim alanlarını ve çevrelerini bulacağız 
3- 2 farrklı mirasçı olacak 
"""
from abc import ABC , abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass

    def toString(self): pass
class Square(Shape):
     
    def __init__(self , edge):
        self.__edge = edge # edge is private   
        
    def area(self): 
        result = self.__edge**2
        print("Square area : " , result)
    
    def perimeter(self): 
        result = self.__edge*4
        print("Square perimeter : " , result)
        
    def toString(self):
        print("square edge : ", self.__edge)
        
class Circle(Shape):
    # constant value
    PI = 3.14    
    
    def __init__(self , radius):
        self.__radius = radius # radius is private
        
    def area(self): 
        result = self.PI*self.__radius**2 # pi*r^2
        print("Circle area : " , result)
    
    def perimeter(self):     # 2*pi*r
        result = 2*self.PI*self.__radius
        print("Circle perimeter : " , result)
        
    def toString(self):
        print("Circle radius : ", self.__radius)    
 
sayi=int(input("how many circle will you calculate :"))
i = 0
while(i<sayi):
    
    r = float(input("enter the radius for  circule  : "))

    c = Circle(r)
    c.area()
    c.perimeter()
    c.toString()
    
    i = i + 1

number = int(input("how many square will you calculate : "))
a = 0
while(a<number):
    
    e = float(input("enter the edge for  square  : "))
    
    k = Square(e)
    k.area()
    k.perimeter()
    k.toString()
    
    a = a + 1