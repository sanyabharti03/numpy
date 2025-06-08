# You have an array of stock quantities and one of new shipment quantities. Update the inventory
# in-place using broadcasting and vectorization.

import numpy as np
#Generating random data
stock=np.random.randint(10,50,size=5)
shipment=np.random.randint(10,20,size=5)
#printing stock and shipment array
print("Stock: ",stock)
print("Shipment: ",shipment)

#Updating the inventory
stock=stock+shipment
print("Updated Inventory: ")
print(stock)
