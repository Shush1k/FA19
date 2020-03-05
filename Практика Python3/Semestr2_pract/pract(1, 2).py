from math import pi, atan


def recurrent(x, n=0, e=0):
    M = -1
    L = 1
    P = x
    res = M / (L * P)
    s = f'-1/({x}) + '  # Проверка ряда
    if e:
        while abs(M / (L * P)) > e:
            M = -M
            L = L + 2
            P = P * x ** 2
            res += M / (L * P)
            s += f'{M}/({L}*{P}) + '  # Проверка ряда
    if n:
        for _ in range(1, n):
            M = -M
            L = L + 2
            P = P * x**2
            res += M / (L * P)
            s += f'{M}/({L}*{P}) + '  # Проверка ряда
    return pi / 2 + res, s


def Task1():
    """Task_1"""
    x = float(input('x = '))
    while not x > 1:
        print('Неверное значение x')
        x = float(input('x = '))
    print(atan(x), f'- Верно при x = {x}')
    print('/'*34)
    for i in range(5, 11):
        res, s = recurrent(x, i)
        print(res, f'- при n = {i}')
        print(s[:-2])  # Весь ряд
        if i == 10:
            print('/'*34)
        else:
            print()


def Task2():
    """Task_2"""
    x = float(input('x = '))
    print(atan(x), '- Проверка от модуля math')
    print()
    res, _ = recurrent(x=x, e=10**-3)
    print('С точностью E = 10^-3:', res)
    print()
    res, _ = recurrent(x=x, e=10**-5)
    print('С точностью E = 10^-5:', res)


def main():
    Task1()
    Task2()


if __name__ == "__main__":
    main()
