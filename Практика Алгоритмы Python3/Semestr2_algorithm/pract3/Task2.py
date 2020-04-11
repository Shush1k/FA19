def square_or_not(N):
    """
    Дано натуральное число N. Выведите слово YES, если число N является точной степенью
    двойки, или слово NO в противном случае. Операцией возведения в степень пользоваться
    нельзя!"""
    if N == 1:
        print("Вывод: YES")
    elif N < 1:
        print("Вывод: N0")
    else:
        return square_or_not(N/2)
def input_N():
    """Ввод числа N"""
    try:
        N = int(input("Ввод: "))
        return N
    except ValueError:
        print("Вводить число!")
        return input_N()
    
N = input_N()
square_or_not(N)