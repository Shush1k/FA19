import math
def f1(x):
    """Первая функция для интегрирования"""
    return 1/math.sqrt((pow(x,2)+math.pi))


def f2(x):
    """Вторая функция для интегрирования"""
    return (math.tan(x+0.5)/x)*pow(math.e,-x)

def get_trapezoid(f, a, b, n):
    """Метод трапеций"""
    result = 0
    h = (b-a)/n
    for i in range(1, n + 1):
        x_i = a + i*h
        x_prev = a + (i-1)*h
        result += (f(x_prev) + f(x_i)) / 2 * h
    return result


def get_simpson(f, a, b, n):
    """Метод Симпсона"""
    result = 0
    h = (b-a)/n
    for i in range(1, n):
        x = a+i*h
        if i % 2 == 0:
            result += 2*f(x)
        else:
            result += 4*f(x)
    result += f(a)+f(b)
    result *= h/3
    return result


def get_precision(method, f, a, b, precision=10**-7):
    """Интегрирование с заданной точностью"""
    n = 4
    while True:
        res_n = method(f, a, b, n)
        res_2n = method(f, a, b, 2*n)
        if abs(res_n - res_2n) > precision:
            n *= 2
        else:
            return n, res_2n

func_list = [{"f":f1, "a": 0, "b" : math.sqrt(math.pi)},{"f": f2, "a": 0.5, "b" : 1}]
print("Задание №1")
for d in func_list:
    n, res = get_precision(get_trapezoid, **d)
    print('\n*Интегрирование методом трапеций*\nРезультат: {}, число разбиений интервала n = {}'.format(res, n))
    n, res = get_precision(get_simpson, **d)
    print('*Интегрирование методом Симпсона*\nРезультат: {}, число разбиений интервала n = {}'.format(res, n))