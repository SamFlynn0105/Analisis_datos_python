import pandas
import statsmodels.formula.api as smf
import graphing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data = pandas.read_csv("dog-training.csv", delimiter="\t")

'''print(data.shape)
print(data.head())'''
#----------------------------------

# First, we define our formula using a special syntax
# This says that rescues_last_year is explained by weight_last_year
'''formula = "rescues_last_year ~ weight_last_year"

model = smf.ols(formula = formula, data = data).fit()

fig = graphing.scatter_2D(data, "weight_last_year", "rescues_last_year", trendline = lambda x: model.params[1] * x + model.params[0])
fig.show()'''
#-----------------------------------

# Obtain the label and feature from the original data
dataset = data[['rescues_last_year','weight_last_year']]

# Split the dataset in an 70/30 train/test ratio. We also obtain the respective corresponding indices from the original dataset.
train, test = train_test_split(dataset, train_size=0.7, random_state=21)

print("Train")
print(train.head())
print(train.shape)

print("Test")
print(test.head())
print(test.shape)
#-----------------------------------

# You don't need to understand this code well
# It's just used to create a scatter plot

# concatenate training and test so they can be graphed
plot_set = pandas.concat([train,test])
plot_set["Dataset"] = ["train"] * len(train) + ["test"] * len(test)

# Create graph
'''fig = graphing.scatter_2D(plot_set, "weight_last_year", "rescues_last_year", "Dataset", trendline = lambda x: model.params[1] * x + model.params[0])
fig.show()'''
#--------------------------------------

# First, we define our formula using a special syntax
# This says that rescues_last_year is explained by weight_last_year
formula = "rescues_last_year ~ weight_last_year"

# Create and train the model
model = smf.ols(formula = formula, data = train).fit()

# Graph the result against the data
'''fig = graphing.scatter_2D(train, "weight_last_year", "rescues_last_year", trendline = lambda x: model.params[1] * x + model.params[0])
fig.show()'''
#-------------------------------------

correct_labels = train['rescues_last_year']
predicted = model.predict(train['weight_last_year'])

MSE = mean_squared_error(correct_labels, predicted)
print('MSE = %f ' % MSE)
#-----------------------------------

'''fig = graphing.scatter_2D(test, "weight_last_year", "rescues_last_year", trendline = lambda x: model.params[1] * x + model.params[0])
fig.show()'''
#-----------------------------------

correct_labels = test['rescues_last_year']
predicted = model.predict(test['weight_last_year'])

MSE = mean_squared_error(correct_labels, predicted)
print('MSE = %f ' % MSE)
#-----------------------------------