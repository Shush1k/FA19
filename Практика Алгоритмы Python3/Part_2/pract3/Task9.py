def get_units():
    """
    Дана последовательность натуральных чисел (одно число в строке), завершающаяся двумя
    числами 0 подряд. Определите, сколько раз в этой последовательности встречается число 1.
    Числа, идущие после двух нулей, необходимо игнорировать.
    В этой задаче нельзя использовать глобальные переменные и параметры, передаваемые в
    функцию. Функция получает данные, считывая их с клавиатуры, а не получая их в виде
    параметров.
    """
    n = int(input())
    if n == 1:
        m = int(input())
        if m == 1:
            return get_units() + 2
        elif m == 0:
            k = int(input())
            if k == 1:
                return get_units() + 2
            elif k == 0:
                return 1
            else:
                return get_units() + 1
        else:
            return get_units() + 1
    elif n == 0:
        m = int(input())
        if m == 1:
            return get_units() + 1
        elif m == 0:
            return 0
        else:
            return get_units()
    else:
        return get_units()
            
print(get_units())