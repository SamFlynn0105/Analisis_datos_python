import pandas as pd
#import graphing
# Load a library to do the hard work for us
import statsmodels.formula.api as smf

import matplotlib.pyplot as plt


data1 = pd.read_csv('doggybh.csv',delimiter=',',header='infer')

# Make a dictionary of data for boot sizes
# and harness sizes in cm
"""data = {
    'boot_size' : [ ],
    'harness_size': [ ]
}"""

data = {
    'boot_size' :  data1.boot_size,
    'harness_size' : data1.harness_size
}

# Convert it into a table using pandas
dataset = pd.DataFrame(data)

# Print the data
# In normal python we would write
# print(dataset)
# but in Jupyter notebooks, we simply write the name
# of the variable and it is printed nicely 
print (dataset)

#-----------------------------------------------------------

# First, we define our formula using a special syntax
# This says that boot_size is explained by harness_size
formula = "boot_size ~ harness_size"

# Create the model, but don't train it yet
model = smf.ols(formula = formula, data = dataset)

# Note that we have created our model but it does not 
# have internal parameters set yet
if not hasattr(model, 'params'):
    print("Modelo seleccionado pero no tiene parámetros configurados. Necesitamos entrenarlo!")
#------------------------------------------------------

# Entrenar (ajustar) el modelo para que cree una línea que
# se ajusta a nuestros datos. Este método hace el trabajo duro para
# a nosotros. Veremos cómo funciona este método en una unidad posterior.
fitted_model = model.fit()

# Imprimir información sobre nuestro modelo ahora que ha sido ajustado.
print("Se han encontrado los siguientes parámetros del modelo:\n" + f"Pendiente de línea: {fitted_model.params[1]}\n"+ f"Intercepción de línea: {fitted_model.params[0]}")

#--------------------------------------------------------

# Show a scatter plot of the data points and add the fitted line
# Don't worry about how this works for now
plt.scatter(dataset["harness_size"], dataset["boot_size"])
plt.plot(dataset["harness_size"], fitted_model.params[1] * dataset["harness_size"] + fitted_model.params[0], 'r', label='Fitted line')

# add labels and legend
plt.xlabel("harness_size")
plt.ylabel("boot_size")
plt.legend()

#----------------------------------------------------------

# harness_size states the size of the harness we are interested in
harness_size = { 'harness_size' : [60.5] }

# Use the model to predict what size of boots the dog will fit
approximate_boot_size = fitted_model.predict(harness_size)

# Print the result
print("Estimacion approximate_boot_size:")
print(approximate_boot_size[0])