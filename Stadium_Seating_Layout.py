# Generate a stadium seating layout using arrays and stack seat blocks together row-wise and
# column-wise.

import numpy as np

#Random data entered manually
block1=np.array([[1,2,3],[4,5,6]])
block2=np.array([[7,8,9],[10,11,12]])
block3=np.array([[13,14,15],[16,17,18]])

#Column-wise
h_stack=np.hstack((block1,block2,block3))
print("Column-wise: \n",h_stack)

#Row-wise
v_stack=np.vstack((block1,block2,block3))
print("Row-wise: \n",v_stack)
