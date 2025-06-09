# Convert a 2D keyword matrix from resumes to a 1D array.

import numpy as np
#Generating random data
arr=np.random.randint(20,100,size=(20,100))
#converting to 1D 
print(arr.flatten())