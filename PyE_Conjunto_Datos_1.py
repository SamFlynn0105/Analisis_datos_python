import pandas
import statsmodels.formula.api as smf
import graphing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# Cargue un conjunto de datos alternativo de la sucursal europea de la organización benéfica
datos_arch = pandas.read_csv("dog-training-switzerland.csv", delimiter="\t")

print(datos_arch.shape)
print (datos_arch.head())
#------------------------------------
# Obtain the label and feature from the original data
dataset = datos_arch[['rescues_last_year','weight_last_year']]

# Primero, definimos nuestra fórmula usando una sintaxis especial.
# Esto dice que rescates_último_año se explica por peso_último_año
formula = "rescues_last_year ~ weight_last_year"
train, test = train_test_split(dataset, train_size=0.7, random_state=21)

# Create and train the model
model = smf.ols(formula = formula, data = train).fit()
# Plot the fitted model against this new dataset. 

correct_labels = datos_arch['rescues_last_year']
predicted = model.predict(datos_arch['weight_last_year'])

MSE = mean_squared_error(correct_labels, predicted)
print('MSE = %f ' % MSE)

fig = graphing.scatter_2D(datos_arch, "weight_last_year", "rescues_last_year", trendline = lambda x: model.params[1] * x + model.params[0]) 
fig.show()

