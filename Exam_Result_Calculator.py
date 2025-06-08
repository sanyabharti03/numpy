# Given marks in 3 subjects for 100 students in a 2D array, write a vectorized function to calculate
# their average marks.

import numpy as np

#Generating random data

arr=np.random.randint(20,100,size=(100,3))
np.set_printoptions(precision=2)         #sets the number of decimal places shown when printing NumPy arrays
mean=np.mean(arr,axis=1)
print(mean)


