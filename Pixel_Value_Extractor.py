# Flatten a color image array of shape (3, 100, 100) using ravel() and flatten().

import numpy as np
#Generating random data
arr=np.random.randint(0,256,size=(3,100,100))
print(arr)
#Converting to 1D using flatten
flat=arr.flatten()
#Converting to 1D using ravel
rav=np.ravel(arr)
print("Flatten: ",flat)      
print("Ravel: ",rav)
