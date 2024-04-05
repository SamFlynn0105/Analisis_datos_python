import pandas as pd
from matplotlib import pyplot as plt

# Load data from a text file
#!wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv
df_students = pd.read_csv('grades1.csv',delimiter=',',header='infer')

# Remove any rows with missing data
df_students = df_students.dropna(axis=0, how='any')

# Calculate who passed, assuming '60' is the grade needed to pass
passes  = pd.Series(df_students['Calif'] >= 60)

# Save who passed to the Pandas dataframe
df_students = pd.concat([df_students, passes.rename("Pase")], axis=1)

# Print the result out into this notebook
print (df_students) 

#df_students.plot.bar(x='Nombre', y='HrsEstudio', color='teal', figsize=(6,4))
#plt.show()

# Ensure plots are displayed inline in the notebook
#matplotlib inline

# Create a bar plot of name vs grade
#plt.bar(x=df_students.Nombre, height=df_students.Calif)

# Display the plot
 #plt.show()

# Create a bar plot of name vs grade
 #plt.bar(x=df_students.Nombre, height=df_students.Calif, color='orange')

# Customize the chart
 #plt.title('Calificacion Estudiantes')
 #plt.xlabel('Estudiante')
 #plt.ylabel('Calificacion')
 #plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
 #plt.xticks(rotation=90)

# Display the plot
 #plt.show()

 # Create a Figure
 #fig = plt.figure(figsize=(8,3))

# Create a bar plot of name vs grade
 #plt.bar(x=df_students.Nombre, height=df_students.Calif, color='blue')

# Customize the chart
 #plt.title('Calificacion Estudiantes')
 #plt.xlabel('Estudiantes')
 #plt.ylabel('Calificacion')
 #plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
 #plt.xticks(rotation=80)

# Show the figure
 #plt.show()

 # Create a figure for 2 subplots (1 row, 2 columns)
 #fig, ax = plt.subplots(1, 2, figsize = (10,4))

# Create a bar plot of name vs grade on the first axis
 #ax[0].bar(x=df_students.Nombre, height=df_students.Calif, color='orange')
 #ax[0].set_title('Grades')
 #ax[0].set_xticklabels(df_students.Nombre, rotation=90)

# Create a pie chart of pass counts on the second axis
 #pass_counts = df_students['Pase'].value_counts()
 #ax[1].pie(pass_counts, labels=pass_counts)
 #ax[1].set_title('Passing Grades')
 #ax[1].legend(pass_counts.keys().tolist())

# Add a title to the Figure
 #fig.suptitle('Student Data')

# Show the figure
 #fig.show()

