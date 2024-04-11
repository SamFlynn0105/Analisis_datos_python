import pandas
import statsmodels.formula.api as smf
import joblib
"""!pip install statsmodels
!wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/graphing.py
!wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/doggy-boot-harness.csv"""

# Load a file containing dog's boot and harness sizes
data = pandas.read_csv('doggybh.csv')

# Print the first few rows
data.head()
#---------------------------------------
# Fit a simple model that finds a linear relationship
# between boot size and harness size, which we can use later
# to predict a dog's boot size, given their harness size
model = smf.ols(formula = "boot_size ~ harness_size", data = data).fit()

print("Modelo entrenado!")
#---------------------------------------


model_filename = './avalanche_dog_boot_model.pkl'
joblib.dump(model, model_filename)

print("Model saved!")
#---------------------------------------

model_loaded = joblib.load(model_filename)

print("Hemos cargado un modelo con los siguientes parámetros:")
print(model_loaded.params)
#---------------------------------------

# Let's write a function that loads and uses our model
def load_model_and_predict(harness_size):
    '''
    This function loads a pretrained model. It uses the model
    with the customer's dog's harness size to predict the size of
    boots that will fit that dog.

    harness_size: The dog harness size, in cm 
    '''

    # Load the model from file and print basic information about it
    loaded_model = joblib.load(model_filename)

    print("Hemos cargado un modelo con los siguientes parámetros.:")
    print(loaded_model.params)

    # Prepare data for the model
    inputs = {"harness_size":[harness_size]} 

    # Use the model to make a prediction
    predicted_boot_size = loaded_model.predict(inputs)[0]

    return predicted_boot_size

# Practice using our model
predicted_boot_size = load_model_and_predict(45)

print("Tamaño previsto de la bota del perro:", predicted_boot_size)
#------------------------------------------

def check_size_of_boots(selected_harness_size, selected_boot_size):
    '''
    Calculates whether the customer has chosen a pair of doggy boots that 
    are a sensible size. This works by estimating the dog's actual boot 
    size from their harness size.

    This returns a message for the customer that should be shown before
    they complete their payment 

    selected_harness_size: The size of the harness the customer wants to buy
    selected_boot_size: The size of the doggy boots the customer wants to buy
    '''

    # Estimate the customer's dog's boot size
    estimated_boot_size = load_model_and_predict(selected_harness_size)

    # Round to the nearest whole number because we don't sell partial sizes
    estimated_boot_size = int(round(estimated_boot_size))

    # Check if the boot size selected is appropriate
    if selected_boot_size == estimated_boot_size:
        # The selected boots are probably OK
        return f"¡Gran elección! Creemos que estas botas le quedarán bien a su perro de avalanchas."

    if selected_boot_size < estimated_boot_size:
        # Selected boots might be too small 
        return "Las botas que has seleccionado pueden ser DEMASIADO PEQUEÑAS para un perro como "\
               f"grande como tu. Recomendamos una talla de botas para perros de {estimated_boot_size}."

    if selected_boot_size > estimated_boot_size:
        # Selected boots might be too big 
        return "Las botas que has seleccionado pueden ser DEMASIADO GRANDES para un perro. "\
               f"pequeño como tu. Recomendamos una talla de botas para perros de {estimated_boot_size}."
    

# Practice using our new warning system
check1 = check_size_of_boots(selected_harness_size=55, selected_boot_size=39)
print (check1)