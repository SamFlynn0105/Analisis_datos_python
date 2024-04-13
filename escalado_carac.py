import pandas
from m1b_gradient_descent import gradient_descent
import numpy
import graphing
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

data = pandas.read_csv("dog-training.csv", delimiter="\t")
data1 = data.head()
#print (data1)
#--------------------------------------------


# Entrenar modelo usando gradiente de descenso
# Este método utiliza un código personalizado que imprimirá el progreso a medida que avance el entrenamiento.
# No necesitas inspeccionar cómo funciona esto para estos ejercicios, pero si estás
# curioso, puedes encontrarlo en nuestro repositorio de GitHub
model = gradient_descent(data.month_old_when_trained, data.mean_rescues_per_year, learning_rate=5E-4, number_of_iterations=8000)

#--------------------------------------------

# Plot the data and trendline after training
fig = graphing.scatter_2D(data, "month_old_when_trained", "mean_rescues_per_year", trendline=model.predict)
fig.show()
#--------------------------------------------

# Agregue la versión estandarizada de "age_when_trained" al conjunto de datos.
# Observe que "centra" la edad media alrededor de 0
data["standardized_age_when_trained"] = (data.month_old_when_trained - numpy.mean(data.month_old_when_trained)) / (numpy.std(data.month_old_when_trained))

# Print a sample of the new dataset
print (data[:5])
#--------------------------------------------

fig = px.box(data,y=["month_old_when_trained", "standardized_age_when_trained"])
fig.show()
#--------------------------------------------

# Volvamos a entrenar nuestro modelo, esta vez usando la característica estandarizada.
model_norm = gradient_descent(data.standardized_age_when_trained, data.mean_rescues_per_year, learning_rate=5E-4, number_of_iterations=8000)
#--------------------------------------------

# Plot the data and trendline again, after training with standardized feature
fig = graphing.scatter_2D(data, "standardized_age_when_trained", "mean_rescues_per_year", trendline=model_norm.predict)
fig.show()
#--------------------------------------------

cost1 = model.cost_history
cost2 = model_norm.cost_history

# Creates dataframes with the cost history for each model
df1 = pandas.DataFrame({"cost": cost1, "Model":"No feature scaling"})
df1["number of iterations"] = df1.index + 1
df2 = pandas.DataFrame({"cost": cost2, "Model":"With feature scaling"})
df2["number of iterations"] = df2.index + 1

# Concatenate dataframes into a single one that we can use in our plot
df = pandas.concat([df1, df2])

# Plot cost history for both models
fig = graphing.scatter_2D(df, label_x="number of iterations", label_y="cost", title="Training Cost vs Iterations", label_colour="Model")
fig.update_traces(mode='lines')
fig.show()