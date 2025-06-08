#Create a NumPy array to represent daily temperature readings for 12 months (each with 30 days).
# Fill the array with random integers from 10°C to 45°C.

import numpy as np


#Generating random data
arr=np.random.randint(10,46,size=(12,30))
print(arr)