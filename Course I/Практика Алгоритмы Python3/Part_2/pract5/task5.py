"""
Задача 5:
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как
равны между собой (оба являться минимальными), так и различаться.
"""
import array
from random import randint
arr = array.array('i', [randint(-100, 100) for _ in range(10)])
print("Исходный массив:", arr)

mm = min(*arr)
arr.remove(mm)
sm = min(*arr)
print("Самый маленький:", mm, "\nВторой по малости:", sm)