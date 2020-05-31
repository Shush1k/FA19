"""
Задача 2:
В массиве найти максимальный элемент с четным индексом.
Другая формулировка задачи: среди элементов массива с четными индексами, найти тот,
который имеет максимальное значение.
"""
import array
from random import randint
arr = array.array('i', [randint(-100, 100) for _ in range(10)])
print("Исходный массив:", arr)
max_elem = -100
for i in range(len(arr)):
    if i % 2 == 0 and arr[i] > max_elem:
        max_elem = arr[i]
print(f"Максимальный элемент с четным индексом: {max_elem}")