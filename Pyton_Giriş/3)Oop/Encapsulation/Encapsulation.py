class BankAccount(object): # some information should be private
    
    inflation_rate = 1.32
    def __init__(self , name , money , address):
        self.name = name    # global
        self.__money = money   # private
        self.address = address
    
    def getMoney(self):
        return self.__money
        
    def setMoney(self,amount):
        self.__money = self.__money + amount
        
    def __increase(self): # this method is not accessible from outside for special cases
 
        self.__money = self.__money + self.__money*self.inflation_rate
    
        
        
p1 = BankAccount("ali", 1500, "ankara")
p2 = BankAccount("ahmet" , 1200 , "izmir")

print("get method : " , p1.getMoney())
p1.setMoney(2500)
print(p1.getMoney())
#p1.__increase() # private olduğu için dışarıdan erişemeyiz.
print(p1.getMoney())
p2.setMoney(100)
p2.getMoney()

