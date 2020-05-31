"""
Задача 19:
Заполнить вводом с клавиатуры численный массив за исключением последнего элемента,
вывести его на экран. Запросить еще одно значение и его позицию в в массиве. Вставить
указанное число в заданную позицию, подвинув элементы после него.
"""
import array as ar
from random import randint
def input_N(text_inp):
    """Ввод числа N"""
    try:
        N = int(input(f"{text_inp}"))
        return N
    except ValueError:
        print("Вводить число!")
        return input_N(text_inp)

def main():
    arr = ar.array("i", [])
    N = input_N("Кол-во элементов массива: ")
    for i in range(N-1):
        numb = input_N(f"Введите элемент массива №{i+1}: ")
        arr.append(numb)

    print("Исходный массив:", arr)
    numb = input_N("Введите элемент для вставки: ")
    pos = input_N("Введите номер позиции: ")
    arr.insert(pos-1, numb)
    
    print("Полученный массив:", arr)

main()