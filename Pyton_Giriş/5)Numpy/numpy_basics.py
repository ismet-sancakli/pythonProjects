# %%
import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9])

x = array.reshape(3,3) # reshape bize matris oluşturmak için 
print("Shape" , x.shape)
print("dimension : " , x.ndim)
print("Data type :" , x.dtype.name)
print("size : " , x.size)
print("type : " , type(x))


array1 = np.array([[1,2,3,4,] , [3,2,1,0] , [7,8,9,6]])
array1.shape

zeros = np.zeros((3,4)) # burayı bellekten yer ayırmak şeklinde düşünebiliriz aynı zamanda sıfır matrisi veriyor  bize 
zeros[0,0] = 5
print(zeros) 

ones = np.ones((3,4)) # np.ones bize istediğimiz boyyutta birim matis veriyor
print(ones)
 
np.empty((3,4))  # bize hafızadan boş matris veriyor

a = np.arange(11,50,5) # 11 ile 50 arasında (50 dahil değil) 5 er 5 er artan sayılar oluşturur liste şeklinde
print(a)
np.linspace(10,20,5) # 10 ile 20 arasını 20 dahil olacak şekilde 5 eşit parçaya böler
# %%
# numpy basics operations


a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

print(np.sin(a))
print(a<2) # burada a array inin içindeki satıların 2 den küçük olma durumunu inceliyor


x = np.array([[1,2,3], [4,5,6]])
y = np.array([[4,5,6] , [1,2,3]])
# element wise product
print(x*y)

# matrix product 

#x.dot(y) # bura da matrisler bu şekilde iken hata veriyor çünkü matrisin çarpma kuralın 2,3*3,2 tarzında olmalıdır
         # bunu için ise burada transpoz devreye girer         
x.dot(y.T)

print(np.exp(a)) # a matrisinin exponansiyelini alır.

v = np.random.random((5,5)) # bize (5,5) lik 0 ile 1 arsında sayılardan oluşan bir matris verir
print(v)
print(v.sum())
print(v.min())
print(v.max())
print(v.sum(axis = 0)) # satırları toplarız
print(sum(v)) # sadece ilk satırı toplar
print(v.sum(axis = 1)) # sutunları toplarız 

print(np.sqrt(x)) # matrisin karekökünü alır
print(np.square(x))# matrisin karesini alır
print(np.add(x,y)) # toplama

# %%

# indexing and sciling
import numpy as np # burayı her zaman yazmayı unutma 
array = np.array([1,2,3,4,5,6,7])
print(array[0:4])
reverse_array = array[::-1]
print(reverse_array)


array1 = np.array([[1,2,3,4,5] , [6,7,8,9,10]])
print(array1[1,1])
print(array1[:,1])
print(array1)
print(array1[1,1:4]) # virgülden önceki yer satır sonraki yer ise sütunu işaret eder
print(array1[:,-1]) # çok boyutlu arrayin son sütununu verir
print(array1[-1,:])# çok boyutlu arrayin son satırını verir

# %%
# shape manupulation
import numpy as np

array2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array2)
k = array2.ravel() # matrisi düz bir liste haline getirdik
array2 = k.reshape(3,3) # listeyi tekrar matris haline getirdik
array_T = array2.T # array2 nin transpozu nu aldık 

array3 = np.array([[1,2],[3,4],[5,6]])
print(array3)
array3.reshape(2,3)
print(array3)
array3.resize(2,3)
print(array3)
print(array3)
# %%
# stacking arrays
import numpy as np
arrayx= np.array([[1,2], [3,4]])
arrayy= np.array([[-1,-2], [-3,-4]])
    
arrayv = np.vstack((arrayx, arrayy)) # arrayleri dikey ( vertical ) olarak birleştirmek için kullanıyoruz
print(arrayv)

arrayh = np.hstack((arrayx, arrayy))# arrayleri yatay ( horizontal ) olarak birleştirmek için kullanıyoruz
print(arrayh)
# %%

# conver and copy array
import numpy as np

liste = [1,2,3,4]
arrayt = np.array(liste) # matrise geçişi sağlar

liste2 = list(arrayt)

a = np.array([10,11,12])

b = a
c = a
d = a.copy()
b[0] = 5 # burada sadece a b ve c nin ilk elemanı değişir ama d nin elemanaları değişmez çünkü d de kopyası var
        # d deki kopya için hafızadan ayrıca bir yer daha ayrılır..
        

