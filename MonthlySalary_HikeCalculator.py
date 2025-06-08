# You have a 1D array of salaries for 50 employees. Apply a 10% hike using broadcasting.

import numpy as np

#Generating random data
arr=np.random.randint(20000,100000,size=50)
print("Salary before hike:\n",arr)

#Broadcasting
arr=arr+(0.1*arr)
print("Salary after hike:\n",arr)