"""
Задача 3:
Выполните oбработку элементов прямоугольной матрицы A, имеющей N строк и M столбцов. Все
элeменты имeют целый тип. Дано целое число H. Опрeделите, какие столбцы имeют хотя бы
однo такое число, а какие не имeют.
"""
from random import randint
import numpy as np
def func():
    for i in range(n): #строки
        for j in range(m): #столбцы
            if arr [i][j] == h:
                return 'строка {} столбец {} содержит цифру {}'.format(i+1,j+1,h)
    return f"Столбцы не имеют цифры {h}"

n = int(input('Введите N(кол-во строк): '))
m = int(input('Введите M(кол-во столбцов): '))
h = int(input('Введите H(число): '))
arr = np.array([[randint(0,10) for _ in range (m)] for _ in range (n)])

print("Исходный массив:\n", arr)
print(func())
