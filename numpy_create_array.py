import numpy as np

#1-D array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(f"Dimension: {arr.ndim}")

#0-D array
a = np.array(45)
print(a)
print(f"Dimension: {a.ndim}")

#2-D array
a2 = np.array([[1, 2], [3, 4], [5, 6]])
print(a2)
print(f"Dimension: {a2.ndim}")

#n-D array
a3 = np.array([1, 2, 3, 4], ndmin = 5)
print(a3)
print(f"Dimension: {a3.ndim}")