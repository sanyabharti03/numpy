# You have two grayscale images of shape (100, 100). Merge them horizontally using hstack.

import numpy as np
#Generating random data
image1=np.random.randint(0,256,size=(100,100))
image2=np.random.randint(0,256,size=(100,100))

#Horizontal Stacking
h_stack=np.hstack((image1,image2))
print(h_stack)