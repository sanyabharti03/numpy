# Create an array of customer names, ages, and city codes. Merge the data.

import numpy as np

#Entering any random data manually
names=np.array(["Rohan","Shreya","Vipul"])
age=np.array([27,30,21])
city=np.array([1,2,3])
merge=zip(names,age,city)
print(np.array(list(merge)))