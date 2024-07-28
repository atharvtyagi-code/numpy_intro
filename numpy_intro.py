import numpy as np
list = [8, 3, 5, 2, 9, "Atharv"]
print(type(list)) 
numpy_array = np.array(list)
print(type(numpy_array))
#array_diff = np.array([1, 2, 3], "Lakshmi") Don't mix up the array and the strings in array.

zero_array = np.zeros(5)
print(zero_array)

one_array = np.ones(6)
print(one_array)

num = np.array([1, 2, 3, 4, 5], dtype = "f")
print(num)

num1 = np.array([2, 4, 3, 1, 8, 5], dtype = "U")
print(num1)

Array2D = np.array([[1, 2], [3, 4]])
print(Array2D)

#Homogenious array: All arrays in numpy should have same number of numbers.
Array2D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(Array2D)

print(Array2D.ndim)
print(Array2D.shape)
print(Array2D.size)
print(Array2D.nbytes)