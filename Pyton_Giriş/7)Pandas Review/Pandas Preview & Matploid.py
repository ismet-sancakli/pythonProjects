#%%
import pandas as pd

df = pd.read_csv("iris (1).csv")

print(df.columns)

print(df.Species)
print(df.Species.unique()) # çiçeğin kaç tane türü var sadece onları söyler bize
print(df.info())
print(df.describe())
print(df.dtypes)

setosa = df[df.Species == "Iris-setosa"]
virginica = df[df.Species == "Iris-virginica"]
versicolor = df[df.Species == "Iris-versicolor"]

print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())
#%%

# Line Plot verileri çizgi şeklinde  gösterir
import matplotlib.pyplot as plt

df1 = df.drop("Id" ,axis = 1) # df1 data Frame inden id yi sildik

#df1.plot()
#plt.show()

setosa = df[df.Species == "Iris-setosa"]
virginica = df[df.Species == "Iris-virginica"]
versicolor = df[df.Species == "Iris-versicolor"]

plt.plot(setosa.Id , setosa.PetalLengthCm, color = "blue" , label ="setosa - PetalLengthCm"  )
plt.plot(virginica.Id , virginica.PetalLengthCm, color = "red" , label ="virginica - PetalLengthCm"  )
plt.plot(versicolor.Id , versicolor.PetalLengthCm, color = "black" , label ="versicolor - PetalLengthCm"  )

plt.xlabel("Id") # x eksenine verilen isim
plt.ylabel("PetalLengthCm") # y ekseni içinn verilen isim
plt.legend() # sağ veya sol üst köşede renkelrin kime ait olduğunu gösteren kutu
plt.show() # ekrana basmak için kullandığımız fonksiyon

df1.plot(grid = True , linestyle = ":")  # çizilen çizgileri iki nokta haline getiriyor
plt.show()

df1.plot(grid = True , alpha = 0.7) # burada alpha istatiki çizgilerin saydamlığını belirler

#%% 
# Scatter Plot verileri nokta şeklinde gösterir

setosa = df[df.Species == "Iris-setosa"]
virginica = df[df.Species == "Iris-virginica"]
versicolor = df[df.Species == "Iris-versicolor"]


plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm, color = "yellow" , label = "setosa" )
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm, color = "red" , label = "versicolor" )
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm, color = "blue" , label = "virginica" )
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("Scatter Plot")
plt.show()
# %%
# Histogram 
plt.hist(setosa.PetalLengthCm , bins = 10) 
plt.xlabel("PetalLengthCm")
plt.ylabel("Frekans")
plt.title("Histogram Plot")
plt.show()

#%% 
# Bar Plot  kullanarak verileri sütünlar halinde gösteriyoruz

import numpy as np

x = np.array([1,2,3,4,5,6])
a = ["turkey" , "usd" , "a" ,"b" , "c", "f"]
y = x*2+6

plt.bar(a,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
# %% Subplots
  
df1.plot(grid = True , alpha = 0.7 , subplots = True)

setosa = df[df.Species == "Iris-setosa"]
virginica = df[df.Species == "Iris-virginica"]
versicolor = df[df.Species == "Iris-versicolor"]

plt.subplot(2,1,1)
plt.plot(setosa.PetalLengthCm, color = "black" , label = "setosa" )
plt.ylabel("setosa - PetalLengthCm ")

plt.subplot(2,1,2)
plt.plot(versicolor.PetalLengthCm, color = "red" , label = "versicolor" )
plt.ylabel("versicolor -PetalLengthCm" )
plt.show()

# Subplots demek verilerin ayrı ayrı görselleştirilmesidir 