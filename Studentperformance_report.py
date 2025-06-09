# Given a (50, 5) array representing scores of 50 students in 5 subjects, write a function to flatten
# the data, calculate mean per student.

import numpy as np
#Generating random data
arr=np.random.randint(30,100,size=(50,5))
flat=arr.flatten()
print(flat)
mean=np.mean(arr,axis=1)
print("Mean: \n",mean)