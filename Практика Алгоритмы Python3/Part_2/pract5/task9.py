"""
Задача 9:
Дан список/массив целых чисел. Упорядочьте по возрастанию только:
а) положительные числа;
б) элементы с четными порядковыми номерами в списке.
"""
import numpy as np
from random import randint

def subtask_a(np_arr):
    """По возрастанию только положительные числа"""
    positiv_arr = np_arr[np_arr > 0]
    positiv_sorted_arr = np.sort(positiv_arr)
    pos = 0
    for i in np.arange(np_arr.shape[0]):
        if np_arr[i] > 0:
            np_arr[i] = positiv_sorted_arr[pos]
            pos += 1
    return np_arr

def subtask_b(np_arr):
    """По возрастанию только элементы с четными порядковыми номерами"""
    sorted_arr = np.sort(np_arr[::2])
    pos = 0
    for i in np.arange(np_arr.shape[0]):
        if i % 2 == 0:
            np_arr[i] = sorted_arr[pos]
            pos += 1
    return np_arr
    

np_arr = np.array([randint(-100, 100) for _ in range(10)])
print(f"Исходный массив:\n{np_arr}")
print(f"Упорядочьте по возрастанию только положительные числа:\n{subtask_a(np_arr)}")
print(f"Упорядочьте по возрастанию только элементы с четными порядковыми номерами:\n{subtask_b(np_arr)}")