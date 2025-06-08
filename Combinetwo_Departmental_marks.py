# <!-- You have two arrays: marks of 10 students in Physics and Chemistry. Combine them horizontally
# and vertically. -->

import numpy as np
#Generating random data
marks_physics=np.random.randint(60,100,size=10)
marks_chemistry=np.random.randint(60,100,size=10)
print("Physics marks= ",marks_physics)
print("Chemistry marks= ",marks_chemistry)


#Approach 1:using hstack and vstack
h_stack=np.hstack((marks_physics,marks_chemistry))
v_stack=np.vstack((marks_physics,marks_chemistry))

print("Horizontally combined= \n",h_stack)
print("Vertically combined= \n",v_stack)

