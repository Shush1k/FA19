"""
Задача 6:
Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
Освободившиеся в конце массива элементы заполнить нулями.
"""
import numpy as np
from random import randint

np_arr = np.array([randint(1,10) for _ in range(10)])
print("Исходный массив:", np_arr)

boolean_flag = True
while boolean_flag:
    try:
        a = int(input("Введите начало интервала (число a): "))
        b = int(input("Введите начало интервала (число b): "))
        if a > b: 
            b, a = a, b
        boolean_flag = False
    except ValueError:
        print("Некорректный ввод данных!")


zeros = 0
for i in range(len(np_arr)):
    if np_arr[i] >= a  and np_arr[i] <= b:
        #print(np_arr[i])
        zeros += 1

#print("Нули", zeros)
arr = np_arr[(np_arr < a ) | (np_arr > b)]

for i in range(zeros):
    arr = np.append(arr, [0])
print(arr)
