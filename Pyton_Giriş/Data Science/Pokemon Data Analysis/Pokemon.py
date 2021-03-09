#import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv("pokemon.csv")

data.info() # Data Frame hakkında ilk bilgileri aldım

data.describe()  # Describe fonksiyonu bize sayısal veriler hakkında bilgiler veriyor
data.columns # sutün bilgileri

data.head(10) # ilk 10 terime baktık

data.corr()  # bu fonksiyon yeni bize doğru ve ters orantı hakkında bilgi verir. +1 e yaklaşırsa doğru -1 e yaklaşırsa ters orantı olur.

sns.heatmap()
 

