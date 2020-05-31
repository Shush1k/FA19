"""
Задача 10:
Даны два списка/массива. Определите, совпадают ли множества их элементов.
"""
import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([2,6,3,1,3,9,3])
arr3 = np.array([1,2,3,4])
res1 = np.array_equal(np.unique(arr1), np.unique(arr2))
res2 = np.array_equal(np.unique(arr1), np.unique(arr3))
print("arr1: ", arr1)
print("arr2: ", arr2)
print("arr3: ", arr3)
if res1 == True:
    print("множества элементов arr1 и arr2 совпадают")
else:
    print("множества элементов arr1 и arr2 \nне совпадают")

if res2 == True:
    print("множества элементов arr1 и arr3 \nсовпадают")
else:
    print("множества элементов arr1 и arr3 не совпадают")