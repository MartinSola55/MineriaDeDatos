import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pylab as py

path = "data"

#importamos el archivo csv
data = pd.read_csv(path + "/clientes.csv", sep=',', encoding='latin-1')

#previsualizamos los primeros datos
data.head()