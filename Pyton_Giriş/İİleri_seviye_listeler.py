# İleri Seviye listeler 

'''
append() metodu
append metodu listenin en sonuna eleman eklememizi sağlar.
'''

liste = [1,2,3,4,5,6,7]
liste.append(34)
liste.append("Python")
liste
#%%
'''
extend() metodu
extend() metodu bir listeye başka bir listenin elemanları eklememizi sağlar.
'''

liste = [1,2,3,4,5,6,7]
liste.extend([10,11,12])
liste
#%%
'''
insert() metodu
insert() metodu listenin belli bir indeksine bir eleman eklememizi sağlar.
'''
liste = [1,2,3,4,5,6,7,8,9]
liste.insert(2,"Python") # 2.indekse "Python" değerini ekliyoruz.
liste
#%%
'''
pop() metodu
pop() metodu içine hiçbir değer vermezsek listenin son elemanını silerek ekrana basar. 
İçine belli bir indeks değeri verirsek o indeksi siler ve ekrana basar.
'''
liste = [1,2,3,4,5,6,7]
liste.pop() # Son eleman siliniyor.

liste
liste.pop(2) # 2.indeksteki eleman siliniyor.

#%%
'''
remove() metodu
remove() metodu verdiğimiz değeri listeden çıkarmamızı sağlar.
'''
liste = ["Python","Php","Java","C"]
liste.remove("Python") # Python'ı siliyoruz.
liste

liste.remove("Javascript") # Listede yok hata verir.
#%%

'''
ndex() metodu
index() metodu verilen bir değerin baştan başlayarak hangi indekste olduğunu söyler. Değer listede yoksa hata döner. 
Eğer ekstra index değeri belirtilirse, index metodu() değeri bu indeksten itibaren aramaya çalışır.
'''
liste = [1,2,3,4,3,3,5,6,7,8,9]
liste.index(3) # 3 elemanı baştan başlayarak 2.indekste

liste.index(3,3) # 3 elemanı 3.indekten itibaren arandığından 4.indekste 
liste.index("Python")
#%%

'''
count() metodu
count() metodu verilen bir değerin listede kaç defa geçtiğini sayar.
'''
liste = [1,2,3,4,5,6,1,1,1,1,1,1,1,1,8]
liste.count(1)
liste.count(10)
#%%

'''
sort() metodu
sort() metodu bir listenin elemanlarını sayıysa küçükten büyüğe , string ise alfabetik olarak sıralar.
Eğer özellikle içine reverse = True değeri verilirse elemanları büyükten küçüğe sıralar.
'''
liste = [12,-2,3,1,34,100]
liste.sort()
liste

liste2 = ["Python","Php","C","Java"]
liste2.sort()
liste2

liste = [12,-2,3,1,34,100]
liste.sort(reverse = True) # Büyükten küçüğe sıralar.
liste

liste2 = ["Python","Php","C","Java"] # Alfabetik olarak sıralar. reverse=True olduğu sondan başa doğru sıralar.
liste2.sort(reverse = True)
liste2
#%%






