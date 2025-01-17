import pandas as pd
from matplotlib import pyplot as plt
import scipy.stats as stats
from sklearn.preprocessing import MinMaxScaler
from scipy import stats

# Load data from a text file
df_students = pd.read_csv('grades1.csv',delimiter=',',header='infer')

# Remove any rows with missing data
df_students = df_students.dropna(axis=0, how='any')

# Calculate who passed, assuming '60' is the Calif needed to pass
passes  = pd.Series(df_students['Calif'] >= 60)

# Save who passed to the Pandas dataframe
df_students = pd.concat([df_students, passes.rename("Pase")], axis=1)


# Print the result out into this notebook
print(df_students)

""" # Create a function that we can re-use
def show_distribution(var_data):
    '''
    This function will make a distribution (graph) and display it
    '''
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
    fig.show()

#show_distribution(df_students['Calif'])"""

"""# Get the variable to examine
col = df_students['HrsEstudio']
# Call the function
show_distribution(col)"""

"""# Get the variable to examine
# We will only get students who have studied more than one hour
col = df_students[df_students.HrsEstudio>1]['HrsEstudio']

# Call the function
show_distribution(col)

# calculate the 0.01th percentile
q01 = df_students.HrsEstudio.quantile(0.01)
# Get the variable to examine
col = df_students[df_students.HrsEstudio>q01]['HrsEstudio']
# Call the function
show_distribution(col)"""


"""def show_density(var_data):
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

# Get the density of StudyHours
show_density(col)"""

for col_name in ['Calif','HrsEstudio']:
    col = df_students[col_name]
    rng = col.max() - col.min()
    var = col.var()
    std = col.std()
    print('\n{}:\n - Range: {:.2f}\n - Variance: {:.2f}\n - Std.Dev: {:.2f}'.format(col_name, rng, var, std))



"""# Get the Calif column
col = df_students['Calif']

# get the density
density = stats.gaussian_kde(col)

# Plot the density
col.plot.density()

# Get the mean and standard deviation
s = col.std()
m = col.mean()

# Annotate 1 stdev
x1 = [m-s, m+s]
y1 = density(x1)
plt.plot(x1,y1, color='magenta')
plt.annotate('1 std (68.26%)', (x1[1],y1[1]))

# Annotate 2 stdevs
x2 = [m-(s*2), m+(s*2)]
y2 = density(x2)
plt.plot(x2,y2, color='green')
plt.annotate('2 std (95.45%)', (x2[1],y2[1]))

# Annotate 3 stdevs
x3 = [m-(s*3), m+(s*3)]
y3 = density(x3)
plt.plot(x3,y3, color='orange')
plt.annotate('3 std (99.73%)', (x3[1],y3[1]))

# Show the location of the mean
plt.axvline(col.mean(), color='cyan', linestyle='dashed', linewidth=1)

plt.axis('off')

plt.show()"""    

print (df_students.describe())

df_sample = df_students[df_students['HrsEstudio']>1]
print (df_sample)

#df_sample.boxplot(column='HrsEstudio', by='Pase', figsize=(8,5))
#plt.show()

# Create a bar plot of name vs Calif and study hours
#df_sample.plot(x='Nombre', y=['Calif','HrsEstudio'], kind='bar', figsize=(8,5))



"""# Get a scaler object
scaler = MinMaxScaler()

# Create a new dataframe for the scaled values
df_normalized = df_sample[['Nombre', 'Calif', 'HrsEstudio']].copy()

# Normalize the numeric columns
df_normalized[['Calif','HrsEstudio']] = scaler.fit_transform(df_normalized[['Calif','HrsEstudio']])
df_normalized.Calif.corr(df_normalized.HrsEstudio)

# Plot the normalized values
#df_normalized.plot(x='Nombre', y=['Calif','HrsEstudio'], kind='bar', figsize=(8,5))
#plt.show()

# Create a scatter plot
df_sample.plot.scatter(title='Tiempo Estudio vs Calificacion', x='HrsEstudio', y='Calif')
plt.show()"""



#
df_regression = df_sample[['Calif', 'HrsEstudio']].copy()

# Get the regression slope and intercept
m, b, r, p, se = stats.linregress(df_regression['HrsEstudio'], df_regression['Calif'])
print('slope: {:.4f}\ny-intercept: {:.4f}'.format(m,b))
print('so...\n f(x) = {:.4f}x + {:.4f}'.format(m,b))

# Use the function (mx + b) to calculate f(x) for each x (StudyHours) value
df_regression['fx'] = (m * df_regression['HrsEstudio']) + b

# Calculate the error between f(x) and the actual y (Calif) value
df_regression['error'] = df_regression['fx'] - df_regression['Calif']

# Create a scatter plot of Calif vs StudyHours
df_regression.plot.scatter(x='HrsEstudio', y='Calif')

# Plot the regression line
plt.plot(df_regression['HrsEstudio'],df_regression['fx'], color='cyan')

# Display the plot


print (df_regression[['HrsEstudio', 'Calif', 'fx', 'error']])

# Define a function based on our regression coefficients
def f(x):
    m = 6.3134
    b = -17.9164
    return m*x + b

study_time = 14

# Get f(x) for study time
prediction = f(study_time)

# Grade can't be less than 0 or more than 100
expected_grade = max(0,min(100,prediction))

#Print the estimated grade
print ('Studying for {} hours per week may result in a grade of {:.0f}'.format(study_time, expected_grade))

plt.show()

