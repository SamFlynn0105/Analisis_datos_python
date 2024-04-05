import pandas as pd
from matplotlib import pyplot as plt

df_students = pd.read_csv('grades1.csv',delimiter=',',header='infer')

# Get the variable to examine
 #var_data = df_students['Calif']

# Create a Figure
 #plt.figure(figsize=(10,4))

# Plot a histogram
 #plt.hist(var_data)

# Add titles and labels
 #plt.title('Distribicion Datos')
 #plt.xlabel('Valor')
 #plt.ylabel('Frecuencia')

# Show the figure
 #plt.show()

 # Get the variable to examine
 #var = df_students['Calif']

# Get statistics
 #min_val = var.min()
 #max_val = var.max()
 #mean_val = var.mean()
 #med_val = var.median()
 #mod_val = var.mode()[0]

 #print('Minimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'.format(min_val,
    #                                                                                      mean_val,
    #                                                                                       med_val,
     #                                                                                      mod_val,
     #                                                                                   max_val))

# Create a Figure
 #plt.figure(figsize=(10,4))

# Plot a histogram
 #plt.hist(var)

# Add lines for the statistics
 #plt.axvline(x=min_val, color = 'gray', linestyle='dashed', linewidth = 2)
 #plt.axvline(x=mean_val, color = 'cyan', linestyle='dashed', linewidth = 2)
 #plt.axvline(x=med_val, color = 'red', linestyle='dashed', linewidth = 2)
 #plt.axvline(x=mod_val, color = 'yellow', linestyle='dashed', linewidth = 2)
 #plt.axvline(x=max_val, color = 'gray', linestyle='dashed', linewidth = 2)

# Add titles and labels
 #plt.title('Data Distribution')
 #plt.xlabel('Value')
 #plt.ylabel('Frequency')

# Show the figure
 #plt.show()

# diagrama de caja
# Get the variable to examine
 #var = df_students['Calif']

# Create a Figure
 #fig = plt.figure(figsize=(10,4))

# Plot a histogram
 #plt.boxplot(var)

# Add titles and labels
 #plt.title('Distribucion Datos')

# Show the figure
 #fig.show()

 # Create a function that we can re-use
"""def show_distribution(var_data):
    #from matplotlib import pyplot as plt

    # Get statistics
    min_val = var_data.min()
    max_val = var_data.max()
    mean_val = var_data.mean()
    med_val = var_data.median()
    mod_val = var_data.mode()[0]

    print('Minimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'.format(min_val,
                                                                                            mean_val,
                                                                                            med_val,
                                                                                            mod_val,
                                                                                            max_val))

    # Create a figure for 2 subplots (2 rows, 1 column)
    fig, ax = plt.subplots(2, 1, figsize = (10,4))

    # Plot the histogram   
    ax[0].hist(var_data)
    ax[0].set_ylabel('Frequency')

    # Add lines for the mean, median, and mode
    ax[0].axvline(x=min_val, color = 'gray', linestyle='dashed', linewidth = 2)
    ax[0].axvline(x=mean_val, color = 'cyan', linestyle='dashed', linewidth = 2)
    ax[0].axvline(x=med_val, color = 'red', linestyle='dashed', linewidth = 2)
    ax[0].axvline(x=mod_val, color = 'yellow', linestyle='dashed', linewidth = 2)
    ax[0].axvline(x=max_val, color = 'gray', linestyle='dashed', linewidth = 2)

    # Plot the boxplot   
    ax[1].boxplot(var_data, vert=False)
    ax[1].set_xlabel('Value')

    # Add a title to the Figure
    fig.suptitle('Data Distribution')

    # Show the figure
    plt.show()

# Get the variable to examine
col = df_students['Calif']
# Call the function
show_distribution(col)"""

def show_density(var_data):
    #from matplotlib import pyplot as plt

    fig = plt.figure(figsize=(10,4))

    # Plot density
    var_data.plot.density()

    # Add titles and labels
    plt.title('Data Density')

    # Show the mean, median, and mode
    plt.axvline(x=var_data.mean(), color = 'cyan', linestyle='dashed', linewidth = 2)
    plt.axvline(x=var_data.median(), color = 'red', linestyle='dashed', linewidth = 2)
    plt.axvline(x=var_data.mode()[0], color = 'yellow', linestyle='dashed', linewidth = 2)

    # Show the figure
    plt.show()

# Get the density of Grade
col = df_students['Calif']
show_density(col)