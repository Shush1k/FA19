"""
Задача 4:
Найти в массиве те элементы, значение которых меньше среднего арифметического, взятого от
всех элементов массива.
"""
import array
from random import randint
arr = array.array('i', [randint(0, 10) for _ in range(5)])
print("Исходный массив:", arr)

res = 0
for i in range(len(arr)):
    res += arr[i]
ar_avg = res / len(arr)
print("Ср.арифм", ar_avg)
print("Элементы, значение которых меньше среднего арифметического:\n")
for i in range(len(arr)):
    if arr[i] < ar_avg:
        print(f"Индекс {i} значение", arr[i])
    