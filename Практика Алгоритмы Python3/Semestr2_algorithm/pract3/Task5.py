def reverse_numbers(N):
    """Дано натуральное число N. Выведите все его цифры по одной, в обратном порядке,
    разделяя их пробелами или новыми строками.При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы,
    разумеется). Разрешена только рекурсия и целочисленная арифметика."""
    if N < 10:
        return N
    else:
        print(str(N % 10))
        return reverse_numbers(N//10)


def input_N():
    """Ввод числа N"""
    try:
        N = int(input("Ввод: "))
        return N
    except ValueError:
        print("Вводить число!")
        return input_N()

N = input_N()
print(reverse_numbers(N))