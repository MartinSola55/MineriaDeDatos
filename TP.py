import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pylab as py

path = "data"

#importamos el archivo csv
data = pd.read_csv(path + "/clientes.csv", sep=',', encoding='latin-1')

data_filt = data.drop(columns=['IdCliente', 'IdCiudad', 'Nombre', 'Apellido', 'FechaNacimiento', 'Email', 'Direccion', 'Telefono'])

# Definir array de columnas a analizar
columnas = data_filt.columns

#previsualizamos los primeros datos
data_filt.head()
# Reemplazar los valores NaN por un guion "-" en todo el DataFrame
# data_filt.fillna('-', inplace=True)

data_filt.describe(include='all')

# Calcular varianza y desvío con redondeo a 4 decimales
varianza = data_filt.var(numeric_only=True).round(4)
desvio = data_filt.std(numeric_only=True).round(4)

# Convertir resultados a cadenas de texto con formato personalizado
varianza_str = varianza.apply(lambda x: f"{x:.4f}").to_string()
desvio_str = desvio.apply(lambda x: f"{x:.4f}").to_string()

# Mostrar resultados por consola
print("\nVarianza:")
print(varianza_str)
print("\nDesvío estándar:")
print(desvio_str)

# Mostrar la cantidad de filas y columnas del DataFrame
data_filt.shape

# Recorrer array de columnas y calcular frecuencias y frecuencias relativas
for col in columnas:
    # Calcular frecuencia y frecuencia relativa de valores en la columna
    frecuencia = data_filt[col].value_counts()
    frecuencia_rel = data_filt[col].value_counts(normalize = True) * 100
    
    # Convertir resultado a cadena de texto con formato personalizado
    frecuencia_rel_str = (frecuencia_rel.round(2).apply(lambda x: str(x) + '%').to_string(float_format='%.2f'))
    
    # Mostrar resultados por consola
    print("\n\n----------" + col + "----------")
    print("Frecuencia:")
    print(frecuencia)
    print("\nFrecuencia relativa:")
    print(frecuencia_rel_str)