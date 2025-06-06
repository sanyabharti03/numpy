import numpy as np

#Create a 1D NumPy array of integers from 10 to 50 (inclusive) with a step of 5.
arr=np.arange(10,51,5)
print(arr)

#Convert the 1D array [1, 2, 3, 4, 5, 6] into a 2D array with 2 rows and 3 columns.
array1D=np.array([1, 2, 3, 4, 5, 6])
shape=array1D.reshape(2,3)
print(shape)

#Slice the array [10, 20, 30, 40, 50, 60] to obtain [30, 40].
slicing=np.array([10, 20, 30, 40, 50, 60])
print(slicing[2:4])

#Join two arrays a = [1, 2, 3] and b = [4, 5, 6] using NumPy.
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.concatenate((a,b)))

#Split the array [100, 200, 300, 400, 500, 600] into 3 equal parts.
split_array=np.array([100, 200, 300, 400, 500, 600])
s=np.array_split(split_array,3)
for part in s:
    print(part)

#6. Explain the difference between .copy() and .view() in NumPy. Show a short example.
arr1=np.array([12,15,17])
x=arr1.copy();
y=arr1.view();
arr1[0]=100
print("Copy ",x)
print("View ",y)

#Reshape the array [1, 2, 3, 4, 5, 6, 7, 8] into shape (4, 2).
shape=np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(shape.reshape(4,2))

#Change the value at index 2 in [10, 20, 30, 40] to 300.
ind=np.array([10, 20, 30, 40])
c=ind.view()
ind[2]=300
print(c)

#Delete the 3rd element from [5, 10, 15, 20, 25] using NumPy.
dele=np.array([5, 10, 15, 20, 25])
new_dele=np.delete(dele,2)
print(new_dele)
# 10. Insert the value 99 at index 1 in [1, 2, 3, 4] using NumPy.

ins=np.array([1, 2, 3, 4] )
new_ins=np.insert(ins,1,99)
print(new_ins)
# 11. Mask an array [12, 55, 4, 78, 33] to extract values greater than 50.
mask=np.array([12, 55, 4, 78, 33])
print(mask[mask>50])


# 12. Flatten a 2D array [[1, 2], [3, 4]] into 1D.
array2D=np.array([[1, 2], [3, 4]])
new_array2D=array2D.flatten()
print(new_array2D)


# 13. Vertically stack [[1, 2], [3, 4]] and [[5, 6], [7, 8]].
stack1=np.array([[1, 2], [3, 4]])
stack2=np.array([[5, 6], [7, 8]])

v_stack=np.vstack((stack1,stack2))
print(v_stack)
# 14. Horizontally stack the same two arrays.
h_stack=np.hstack((stack1,stack2))
print(h_stack)
# 15. Create a 3x3 identity matrix with NumPy.
iden=np.identity(3)
print(iden)


# 16. Replace all even numbers in [2, 5, 8, 11, 14] with -1.
even=np.array([2, 5, 8, 11, 14])
even[even%2==0]=-1
print(even)

# 17. Find the index/indices of the maximum value in [9, 4, 7, 9, 2].
max=np.array([9, 4, 7, 9, 2])
max_element=max.max()
for i in range(5):
    if(max[i]==max_element):
        print(i)
    



# 18. Broadcast: Add [1, 2, 3] to every row of [[10, 20, 30], [40, 50, 60]].
add=np.array([[10, 20, 30], [40, 50, 60]])  #Broadcasting works here because the shape of broad (3,) matches the number of columns in add.
broad=np.array([1, 2, 3])
print(add+broad)

# 19. Use np.where to replace negative numbers with 0 in [-3, 5, -1, 8].
rep=np.array([-3, 5, -1, 8])
result=np.where(rep<0,0,rep)
print(result)

# 20. Reverse the elements of [100, 200, 300, 400] so it becomes [400, 300, 200, 100].

reverse=np.array([100, 200, 300, 400])
print(reverse[::-1])
