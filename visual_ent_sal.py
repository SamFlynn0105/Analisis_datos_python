import pandas as pd
import graphing
# Load and prepare matplotlib to use for plotting graphs
import matplotlib.pyplot as plt

# Leer el archivo de texto que contiene datos usando pandas
dataset = pd.read_csv('doggybh.csv')

# Imprimir los datos
# Debido a que hay muchos datos, use head() para imprimir solo las primeras filas
#dataset.head()
#--------------------------------------------

"""# Look at the harness sizes
print("Harness sizes")
print(dataset.harness_size)

# Remove the sex and age-in-years columns.
del dataset["sex"]
del dataset["age_years"]

# Print the column names
print("\nColumnas disponibles después de eliminar la información de sexo y edad:")
print(dataset.columns.values)"""
#------------------------
"""# Print the data at the top of the table
print("ARRIBA DE LA TABLA")
print(dataset.head())

# print the data at the bottom of the table
print("\nABAJO DE LA TABLA")
print(dataset.tail())"""
#------------------------------------

"""# Print how many rows of data we have
print(f"Tenemos {len(dataset)} lineas de datos")

# Determine whether each avalanche dog's harness size is < 55
# This creates a True or False value for each row where True means 
# they are smaller than 55
is_small = dataset.harness_size < 55
print("\nSi el arnés del perro es menor a talla 55:")
print(is_small)

# Now apply this 'mask' to our data to keep the smaller dogs
data_from_small_dogs = dataset[is_small]
print("\nDatos para perros con arnés menor a la talla 55:")
print(data_from_small_dogs)

# Print the number of small dogs
print(f"\nNúmero de perros con talla de arnés inferior a 55: {len(data_from_small_dogs)}")"""
#----------------------------------------

# Haga una copia del conjunto de datos que solo contenga perros con
# una talla de bota inferior a la talla 40
# La llamada a copiar() es opcional pero puede ayudar a evitar cambios inesperados.
# comportamiento en escenarios más complejos
data_smaller_paws = dataset[dataset.boot_size < 40].copy()


# Print information about this
print(f"Ahora tenemos {len(data_smaller_paws)} lineas en el conjunto de datos. Las ultimas 5 lineas:")
print (data_smaller_paws.tail())
#----------------------------------------

# Show a graph of harness size by boot size:
#plt.scatter(data_smaller_paws["harness_size"], data_smaller_paws["boot_size"])

"""# add labels
plt.xlabel("harness_size")
plt.ylabel("boot_size")
plt.show()"""
#---------------------------
# Convert harness sizes from metric to imperial units 
# and save the result to a new column
data_smaller_paws['harness_size_imperial'] = data_smaller_paws.harness_size / 2.54

# Show a graph of harness size in imperial units
plt.scatter(data_smaller_paws["harness_size_imperial"], data_smaller_paws["boot_size"])
plt.xlabel("harness_size_imperial")
plt.ylabel("boot_size")
plt.show()