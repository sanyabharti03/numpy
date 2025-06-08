# Split a colored image array of shape (100, 100, 3) into R, G, B channels.

import numpy as np
arr=np.random.randint(0,256,size=(100,100,3))
print(arr)
split_array=np.split(arr,3,axis=2)
print("Split Array:  ")    #prints the array

for item in split_array:     #print each chunk of the split_array
    print(item)