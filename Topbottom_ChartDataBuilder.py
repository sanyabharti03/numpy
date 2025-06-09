# Stack sales data of 2 months (as 2D arrays) vertically and horizontally to prepare combined
# reports.

import numpy as np
#Generating random data
month1=np.random.randint(10,1000,size=(2,3))
month2=np.random.randint(10,1000,size=(2,3))

print("Horizontal stack:\n",np.hstack((month1,month2)))
print("Vertical stack:\n",np.vstack((month1,month2)))