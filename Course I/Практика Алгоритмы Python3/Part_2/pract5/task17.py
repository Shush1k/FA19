"""
Задача 17:
Сдвинуть элементы массива в указанном направлении (влево или вправо) и на указанное число
шагов. Освободившиеся ячейки заполнить нулями. Выводить массив после каждого шага.
"""
import array as ar
from random import randint
def input_N():
    """Ввод числа N"""
    try:
        N = int(input("Кол-во шагов: "))
        return N
    except ValueError:
        print("Вводить число!")
        return input_N()

def func(inp_arr, shift):
    res = inp_arr[:]
    if shift == "<":
        for i in range(len(inp_arr)-1):
            res[i] = res[i+1]
        res[-1] = 0
    elif shift == ">":
        for i in range(len(inp_arr)-1, 0, -1):
            res[i] = res[i-1]
        res[0] = 0
    else:
        print("Вы указали знак не верно!")
        return 
    return res
def checker(shift_mark):
    if shift_mark != "<" and shift_mark != ">":
        print("Введите знак ещё раз!")
        shift = input()
        return checker(shift)
    return shift_mark

if __name__ == '__main__':
    arr = ar.array('i', [randint(-10, 10) for _ in range(10)])
    print("\nИсходный массив: ", arr)
    print("Введите < или > для того, чтобы выбрать куда сдвигать элементы")
    shift = input()  # Направление сдвига
    shift = checker(shift)
    N = input_N()  # Кол-во шагов  
    for i in range(N):
        arr = func(arr, shift)
        print(arr)