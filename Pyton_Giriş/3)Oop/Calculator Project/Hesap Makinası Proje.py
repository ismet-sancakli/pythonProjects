# %%

# calculator project

class Calculate(object):
    "calculator"
    # init method
    def __init__(self,a ,b):
        # attribute
        self.value1 = a
        self.value2 = b    
    
    def add(self):
        "addition"
        return (self.value1 + self.value2)
        
    def multiply(self):
        "multiplication"
        return (self.value1 * self.value2)
    
    def subtract(self):
        "subtraction"
        return (self.value1 - self.value2)
    
    def division(self):
        "divide"
        return (self.value1 / self.value2)
i = 1
while i == 1:    
    
    select = input("choose 1-for addition , 2-for subtraction , 3-for multiplication , 4-division , (q-exit)\n")
    
    if select == "q":
        print("_Leaving_\n")
        i = 0  

    elif select == "1":  
        c1 = int(input("Enter the first number please : "))
        c2 = int(input("Enter the second number please : "))
        calc = Calculate(c1,c2)
        add_result = calc.add()
        print("Add : {} ".format(add_result))
        
    elif select == "2": 
        c1 = int(input("Enter the first number please : "))
        c2 = int(input("Enter the second number please : "))
        calc = Calculate(c1,c2)
        sub_result = calc.subtract()
        print("Subtract  : {} ".format(sub_result))
        
    elif select == "3":
        c1 = int(input("Enter the first number please : "))
        c2 = int(input("Enter the second number please : "))
        calc = Calculate(c1,c2)
        mul_result = calc.multiply()
        print("Mul : {} ".format(mul_result))
        
    elif select == "4":
        c1 = int(input("Enter the first number please : "))
        c2 = int(input("Enter the second number please : "))
        calc = Calculate(c1,c2)
        div_result = calc.division() 
        print("Div : {} ".format(div_result))       
   
    else:
        print("Wrong Selection !!  Enter the valid number please\n ")
#%%        
 # Hesap makinası kodu
giriş = """
(1) topla
(2) çıkar
(3) çarp
(4) böl
(5) karesini hesapla
(6) karekök hesapla
"""

print(giriş)

anahtar = 1

while anahtar == 1:
    soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")

    if soru == "q":
        print("çıkılıyor...")
        anahtar = 0

    elif soru == "1":
        sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
        sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
        print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

    elif soru == "2":
        sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
        sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
        print(sayı3, "-", sayı4, "=", sayı3 - sayı4)

    elif soru == "3":
        sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
        sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
        print(sayı5, "x", sayı6, "=", sayı5 * sayı6)

    elif soru == "4":
        sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
        sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
        print(sayı7, "/", sayı8, "=", sayı7 / sayı8)

    elif soru == "5":
        sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
        print(sayı9, "sayısının karesi =", sayı9 ** 2)

    elif soru == "6":
        sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
        print(sayı10, "sayısının karekökü = ", sayı10 ** 0.5)

    else:
        print("Yanlış giriş.")
        print("Yukarıdaki seçeneklerden birini giriniz:", giriş)               
            
            
            