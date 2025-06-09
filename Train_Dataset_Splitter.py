# Given a NumPy array of shape (1000, 5) representing a dataset, split it into training and testing
# sets in an 80-20 ratio.

import numpy as np
#Generating random data
arr=np.arange(0,5000).reshape(1000,5)

# Split index at 80% of the data
percent=int(len(arr)*0.8)

# Split into training and testing sets
train_data,test_data=np.split(arr,[percent])
#Printing the shape of the arrays
print(train_data.shape)
print(test_data.shape)
#Printing the data
print("Training set: \n",train_data)
print("Testing set: \n",test_data)