# You have an array of speeds of cars on a highway. Write a vectorized rule: if speed > 100 km/h,
# assign a fine of INR1000. Else, INR0.

import numpy as np
#Generating random data
arr=np.random.randint(20,120,size=10)
result=np.where(arr>100,1000,0)
print(result)