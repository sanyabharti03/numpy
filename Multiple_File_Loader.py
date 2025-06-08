# You load data of 12 months in a single array. Split it into 4 quarters using np.split().

import numpy as np
#Generating random data
arr=np.random.randint(10,50,size=12)
#Splitting in 4 parts
split_array=np.split(arr,4)
for item in split_array:
    print(item)