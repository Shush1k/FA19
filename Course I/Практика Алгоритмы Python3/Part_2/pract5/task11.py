"""
Задача 11:
Дан список/массив. После каждого элемента добавьте предшествующую ему часть списка.
"""
import numpy as np
print("Пример ввода: 1 2 3")
my_list = [int(i) for i in input("\nВведите список: ").split()]
arr_a = np.array(my_list)
arr_b = []
for i in range(len(arr_a)):
    for j in range(i+1):
        arr_b = np.append(arr_b, arr_a[j])

print("Исходный массив:", arr_a)
print("Конечный массив:", arr_b)