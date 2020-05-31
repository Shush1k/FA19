"""
Выполните расчет временных затрат для 5 функций работы со списками и работы с массивами,
и выскажите обоснованное предположение полученной разницы во времени исполнения
"""
# Я ничего не понял! Но списки выполняются быстрее, почему Макрушин говорил о быстродействии массивов? Не знаю. Смысл всех тасков не понятен :D

import array as ar
import numpy as np
from timeit import default_timer
arr_1 = ar.array ('i', [1,2,2,3,4])
arr_2 = ar.array ('i', [1,2,2,3,4,1,2,2,3,4,1,2,2,3,4,1,2,2,3,4,1,2,2,3,4,1,2,2,3,4,1,2,2,3,4]*20000)
list_1 = [1,2,2,3,4]
list_2 = [1,2,2,3,4,1,2,2,3,4,1,2,2,3,4,1,2,2,3,4,1,2,2,3,4,1,2,2,3,4,1,2,2,3,4]*20000
np_arr_1 = np.array([1,2,2,3,4])
np_arr_2 = np.array([1,2,2,3,4,1,2,2,3,4,1,2,2,3,4,1,2,2,3,4,1,2,2,3,4,1,2,2,3,4,1,2,2,3,4]*20000)



start_time = default_timer()
l = len(arr_1)
print(f'\nВремя на измерение длины массива array из {l} элементов:\n', default_timer()-start_time)
start_time = default_timer()
l = len(arr_2)
print(f'Время на измерение длины массива array из {l} элементов:\n', default_timer()-start_time)

start_time = default_timer()
l = np_arr_1.shape[0]
print(f'\nВремя на измерение длины массива numpy из {l} элементов:\n', default_timer()-start_time)

start_time = default_timer()
l = np_arr_2.shape[0]
print(f'Время на измерение длины массива numpy из {l} элементов:\n', default_timer()-start_time)

start_time = default_timer()
l = len(list_1)
print(f'\nВремя на измерение длины списка из {l} элементов:\n', default_timer()-start_time)
start_time = default_timer()
l = len(list_2)
print(f'Время на измерение длины списка из {l} элементов:\n', default_timer()-start_time)
