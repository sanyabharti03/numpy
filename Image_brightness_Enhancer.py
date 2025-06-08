# You have a 2D grayscale image stored as an array. Increase brightness by adding 50 using
# broadcasting, without using loops.

import numpy as np
#Generating random data
arr=np.random.randint(0,256,size=(8,16))
print("Array before: ")
print(arr)
arr=arr+50
print("Array after updation: ")
print(arr)