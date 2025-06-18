import numpy as np

arr = np.array([1, 2, 3, 4, 5,6])
print(arr)
print(type(arr))
print("Dimension:", arr.ndim)
arr = arr.reshape(2, 3)
print(arr)
print("Shape: ", arr.shape)

#0-D array
a = np.array(45)
print(a)
print("Dimension:", a.ndim)

#2-D array
a2 = np.array([[1, 2], [3, 4], [5, 6]])
print(a2)
print("Dimension:", a2.ndim)
print("Shape:", a2.shape)

#n-D array
a3 = np.array([1, 2, 3, 4], ndmin = 5)
print(a3)
print("Dimension:", a3.ndim)
print("Shape:", a3.shape)

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)