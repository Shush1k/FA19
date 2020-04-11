def sum_numb(num):
    """
    Дано натуральное число N. Вычислите сумму его цифр. При решении этой задачи нельзя
    использовать строки, списки, массивы (ну и циклы, разумеется).
    
    Суммируем разряд числа + вызываем функцию снова без данного разряда до тех пор,
    пока цифра больше 9"""
    return num%10 + sum_numb(num//10) if num > 9 else num

def input_N():
    """Ввод числа N"""
    try:
        N = int(input("Ввод: "))
        return N
    except ValueError:
        print("Вводить число!")
        return input_N()
    
N = input_N()
print(sum_numb(N))