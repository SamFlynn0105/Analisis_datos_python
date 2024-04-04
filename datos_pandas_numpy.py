import datos_numpy as dn
import pandas as pd
import subprocess

df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                    'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':dn.student_data[0],
                            'Grade':dn.student_data[1]})

print (df_students) 

# obtiene los datos para el indidce 5
#print (df_students.loc[5])

# obtiene las lineas del incide de valores de 0 a 5
#print (df_students.loc[0:5])

# obtiene los datos de las primeras 5 lineas
#print (df_students.iloc[0:5])

# trae los valores del incice indicanco las columnas
#print (df_students.iloc[4,[1,2]])

# trae los valores del indice 0 de la columna grade
#print (df_students.loc[0,'Grade'])

# trae el valor del indice localizando por nombre de le columna name
print (df_students.loc[df_students['Name']=='Aisha'])
print (df_students[df_students['Name']=='Aisha'])
print (df_students.query('Name=="Aisha"'))
print (df_students[df_students.Name == 'Aisha'])
