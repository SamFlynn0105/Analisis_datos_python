import numpy as np

data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]

grades = np.array(data)
#print(grades) 
#print('---')

#print (type(data),'x 2:', data * 2)
#print('---')
#print (type(grades),'x 2:', grades * 2)

#obtiene el numero de espacios en la lista
#print(grades.shape)

# da el valor que se encuentra en la posicion de la lista 
#print(grades[6])
#print(grades.mean())

# Define en array las horas de estudio
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

# Crea array 2d (una serie de matrices)
student_data = np.array([study_hours, grades])

# imprime los arreglos guardados en student_data
#print (student_data)

# imprime grados de arreglos
#print (student_data.shape)

# muestra el primer elemento del primer array
#print (student_data[0][3])

# ontiene el valor medio de los 2 arreglos
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

#print('Average study hours: {:.2f}\nAverage grade: {:.2f}'.format(avg_study, avg_grade))