import pandas as pd

df_students = pd.read_csv('grades.csv',delimiter=',',header='infer')
df_students.head()

#print (df_students)

#print (df_students.isnull())

#print (df_students.isnull().sum())

#print (df_students[df_students.isnull().any(axis=1)])

#df_students.StudyHours = df_students.StudyHours.fillna(df_students.StudyHours.mean())
#print (df_students)

df_students = df_students.dropna(axis=0, how='any')
print (df_students,'\n')

# Get the mean study hours using to column name as an index
mean_study = df_students['StudyHours'].mean()

# Get the mean grade using the column name as a property (just to make the point!)
mean_grade = df_students.Grade.mean()

# Print the mean study hours and mean grade
#print('Average weekly study hours: {:.2f}\nAverage grade: {:.2f}'.format(mean_study, mean_grade),'\n')

# Get students who studied for the mean or more hours
#print (df_students[df_students.StudyHours > mean_study],'\n')

# What was their mean grade?
print ('promedio de estudiantes con mas tiempo de estudio: ', df_students[df_students.StudyHours > mean_study].Grade.mean())

passes  = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

print (df_students, '\n')

print(df_students.groupby(df_students.Pass).Name.count(),'\n')

print(df_students.groupby(df_students.Pass)[['StudyHours', 'Grade']].mean(),'\n')

# Create a DataFrame with the data sorted by Grade (descending)
df_students = df_students.sort_values('Grade', ascending=False)

# Show the DataFrame
print (df_students)
