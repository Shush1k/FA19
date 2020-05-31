"""
Задача 1. В массиве, содержащем положительные и отрицательные целые числа, вычислить
сумму четных положительных элементов.
"""
import array
from random import randint
arr = array.array('i', [randint(-100, 100) for _ in range(10)])
print("Исходный массив:", arr)
res = 0
for i in arr:
    if i > 0 and i % 2 == 0:
        res += i

print(f"Сумма: {res}")