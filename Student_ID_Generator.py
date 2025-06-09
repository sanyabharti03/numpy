# Create a 2D NumPy array with 100 student IDs starting from 1001 to 1100 and reshape it to
# 10x10.

import numpy as np
arr=np.arange(1001,1101).reshape(10,10)
print(arr)