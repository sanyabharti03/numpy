import numpy as np
#create_array
l=[10,20,30,40]
a=np.array(l)
print(a)

#craete_array from a range with step count
b=np.arange(0,19,3)
print(b)

#Create a NumPy array with 6 values between 1 and 3 (inclusive).
c=np.linspace(1,3,6)
print(c)

#4. Convert a 1D array [1, 2, 3, 4, 5, 6] into a 2D array with 2 rows and 3 columns.
arr=np.array([1,2,3,4,5,6])
d=arr.reshape(2,3)
print(d)

#5. Find the average (mean) of the array [10, 20, 30, 40, 50].
arr1=np.array([10, 20, 30, 40, 50])
print("mean of [10, 20, 30, 40, 50] is",np.mean(arr1))




#6. Find the median of the array [5, 1, 9, 3, 7].
arr2=np.array([5, 1, 9, 3, 7])
print("Median is",np.median(arr2))


#7. Calculate the standard deviation of the array [1, 2, 3, 4, 5].
arr3=np.array([1, 2, 3, 4, 5])
print("Standard Deviation is",np.std(arr3))


#8. Add all the elements of the array [10, 20, 30].
arr4=np.array([10, 20, 30])
print("Sum is",np.sum(arr4))


#9. Find the dot product of two arrays: [1, 2] and [3, 4].
arr5=np.array([1,2])
arr6=np.array([3,4])
print("Dot product is ",np.dot(arr5,arr6))

#10. Join two arrays [1, 2] and [3, 4] into one array

print(np.concatenate((arr5,arr6)))


