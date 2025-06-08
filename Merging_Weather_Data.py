# Concatenate two datasets: one containing temperature and one containing humidity. Assume
# both have shape (30, 1).
import numpy as np
temp=np.random.randint(-10,40,size=(30,1))
humidity=np.random.randint(30,50,size=(30,1))
#printing temp and humidity array
print("Temperature=\n",temp)
print("Humidity=\n",humidity)

#Concatenating both the arrays
merge=np.concatenate((temp,humidity),axis=1)
print("Concatenated=\n",merge)