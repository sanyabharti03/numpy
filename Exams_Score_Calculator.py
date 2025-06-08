# Combine arrays of Math and Science scores of 5 classes using np.concatenate() along the
# correct axis.

import numpy as np

#Generating random data
maths=np.random.randint(30,100,size=(5,10))
science=np.random.randint(30,100,size=(5,10))

#Horizontal Stacking
merge=np.concatenate((maths,science),axis=1)
print(merge)