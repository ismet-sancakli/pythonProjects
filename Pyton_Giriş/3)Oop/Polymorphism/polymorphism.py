class Employee:
    def raisee(self):
        raise_rate = 0.1
        return 100 + 100*raise_rate
    
class CompEng(Employee):
    def raisee(self):
        raise_rate = 0.2
        result= 100 + 100*raise_rate    
        print("ComEng = " , result)
class EEE(Employee):
    def raisee(self):
        raise_rate = 0.3
        result= 100 + 100*raise_rate    
        print("EEE = " , result)    
            
e1 = Employee()

ce = CompEng()

eee = EEE()    
    
employee_list = [ce ,eee]

for employee in employee_list:
    employee.raisee()
dir(Employee)    
dir(e1)

    
    
    
    
    
    