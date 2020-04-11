def ez_word(N, delit=2):
    """Дано натуральное число n>1. Проверьте, является ли оно простым. Программа должна
    вывести слово YES, если число простое и NO, если число составное.
    Указание. Понятно, что задача сама по себе нерекурсивна, т.к. проверка числа n на
    простоту никак не сводится к проверке на простоту меньших чисел. Поэтому нужно сделать
    еще один параметр рекурсии: делитель числа, и именно по этому параметру и делать
    рекурсию."""
    if N < 2:
        return False
    elif N == 2:
        return True
    elif N % delit == 0:
        return False
    elif delit < N/2:
        return ez_word(N, delit + 1)
    else:
        return True
def input_N():
    """Ввод числа N"""
    try:
        N = int(input("Ввод: "))
        return N
    except ValueError:
        print("Вводить число!")
        return input_N()

N = input_N()    
print(ez_word(N, 2))