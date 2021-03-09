# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# bu yorum satiri olarak kullanılıyor.

# variable (degisken)
# 1-variable
# 2-function 
# 3-object

var1 = "ankara"
var2="istanbul"
var3=var1+var2
print(var3)
var4="100"
var5="200"
var6=var4+var5
print(var6)
uzunluk = len(var6)
print(uzunluk)
#%%
# numbers
 
z=12
s="ben kelo"

print(s)
print(z)

print(s)
benim_adim="mahmut"
print(benim_adim)

c=8.9
d=-8
int(c+d)
type(benim_adim)
type(s)
type(z)
#%%
# built in function

str1="deneme"
len(str1)
print(str1)
a=10
float(a)
b=1.89
int(b)
c=2.6
round(c)
str2="2005"
int(str2)
type(int(str2))
#%%

# user defined function

var1=20
var2=40

output = ((var1+var2)*var1)/var2

def my_function(a,b):
    """
    burası yorum satırı gibi düşünülebilir.
    """
    output = ((a+b)*a)/b
    return output    

sonuc = my_function(var1,var2)
print(sonuc)

def deneme1():
    print("bu benim ikinci fonksiyonum")
# %% default flexible function
    
    
#def cember_cevresi(r,pi=3.14):
#     
#        output = 2*pi*r
#        return output
# flexible
        
def hesapla(boy,kilo,*args): 
    print(args)
    output = (boy+kilo)*args[0]    
    return output  
    
# %%
    
    # QUIZ
yas = 5
name = "mehmet"
soyisim = "eren"
soyisim2 = "mahmut"

def function(yas,name, *args,ayakkabi_numarasi = 42):
    print("cocugun ismi: ",name, "/yasi: ",yas, "/ayakkabi numarasi : ",ayakkabi_numarasi)
    print(type(name))
    print(type(yas))
    print(float(yas))
    print(len(name))
    
    output= args[0]*yas
    
    return output

sonuc =function(yas,name,soyisim2)
    
print("args[0]*yas : ",sonuc)    
# %%

# Lamda Function 
def hesapla(x):
    return x*x
print(hesapla(4))

sonuc=lambda x: x*x
print(sonuc(3))




    
    
