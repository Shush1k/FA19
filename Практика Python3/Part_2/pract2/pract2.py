import math
import numpy as np
import matplotlib.pyplot as plt


def get_R_2(x_list, y_list, coeff, func=lambda x: x):
    """
    Получение коэффициента детерминации R^2
    """
    if len(coeff) == 2:
        a, b = coeff
        n = len(y_list)
        y_middle = sum(y_list) / n
        upper = sum([(y - func(x, a, b)) ** 2 for y, x in zip(y_list, x_list)])
        lower = sum([(y - y_middle) ** 2 for y in y_list])
        R = upper / lower
    elif len(coeff) == 3:
        a, b, c = coeff
        n = len(y_list)
        y_middle = sum(y_list) / n
        upper = sum([(y - func(x, a, b, c)) ** 2 for y,
                     x in zip(y_list, x_list)])
        lower = sum([(y - y_middle) ** 2 for y in y_list])
        R = upper / lower
    return 1 - R


def get_linear_coeff(x_list, y_list, x_func=lambda x: x, y_func=lambda y: y):
    """
    Получение коэффициентов a и b для уравнений типа a + bx
    """
    n = len(x_list)
    sum_x = sum([x_func(x) for x in x_list])
    sum_y = sum([y_func(y) for y in y_list])
    sum_x2 = sum([x_func(x) ** 2 for x in x_list])
    sum_xy = sum([x_func(x) * y_func(y) for x, y in zip(x_list, y_list)])
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    a = (sum_y - b * sum_x) / n

    return a, b


def get_koef_polim(x_list, y_list):
    """
    Получение коэффициентов a и b для уравнений типа ax^2 + bx + c
    """
    n = len(x_list)
    sum_x = sum([x for x in x_list])
    sum_y = sum([y for y in y_list])
    sum_x2 = sum([x ** 2 for x in x_list])
    sum_xy = sum([x * y for x, y in zip(x_list, y_list)])
    sum_x3 = sum([x ** 3 for x in x_list])
    sum_x4 = sum([x ** 4 for x in x_list])
    sum_x2y = sum([(x ** 2) * y for x, y in zip(x_list, y_list)])
    M1 = np.array([[n, sum_x, sum_x2], [sum_x, sum_x2, sum_x3],
                   [sum_x2, sum_x3, sum_x4]])
    V1 = np.array([sum_y, sum_xy, sum_x2y])
    a, b, c = np.linalg.solve(M1, V1)
    return c, b, a


def get_avg_deviation(x_list, y_list, x_func=lambda x: x, y_func=lambda y: y):
    """
    Вычисление величины среднего квадратичного отклонения S(x) и S(y)
    """
    n = len(x_list)
    sum_x = sum([x_func(x) for x in x_list][::5])
    sum_y = sum([y_func(y) for y in y_list][::5])
    deviation_x = (sum([(x - sum_x) ** 2 for x in x_list]) / n) ** 0.5
    deviation_y = (sum([(y - sum_y) ** 2 for y in y_list]) / n) ** 0.5
    return deviation_x, deviation_y


# Переменные, константы. По заданию
X_MIN = -9
X_MAX = 12
X_1 = -3
X_2 = 5
H = 0.2

# Функции. По заданию

def F1(x): 
    return math.cos(x + 3)


def F1_integral(x): 
    return x * math.cos(x + 3) - math.sin(x + 3)


def F2(x): 
    return x + 4


def F2_integral(x): 
    return (x ** 2) / 2


def F3(x): 
    return 3 * (abs(x+4) ** 0.5)


def F3_integral(x): 
    return (x + 4) * math.sqrt(x + 4) - 12 * math.sqrt(x + 4)


def linear_func(x, a, b): 
    return a + b * x


def quad_func(x, a, b, c): 
    return a * x ** 2 + b * x + c

# Списки
FUNCS_LIST = [F1, F2, F3]
INTEGRATED_FUNC_LIST = [F1_integral, F2_integral, F3_integral]
X_INTERVALS_LIST = [X_MIN, X_1, X_2, X_MAX]
X_LIST = [(x/10) for index in range(3) for x in range(X_INTERVALS_LIST[index] * 10, int(X_INTERVALS_LIST[index+1]*10), int(H*10))]
Y_LIST = [FUNCS_LIST[index](x/10) for index in range(3) for x in range(X_INTERVALS_LIST[index]*10, int(X_INTERVALS_LIST[index+1]*10), int(H*10))]

# Main
# <class 'matplotlib.figure.Figure'> obj1, 2, 3 - axes(графики)
fig, (obj1, obj2, obj3) = plt.subplots(nrows=3, ncols=1, figsize=(10, 25))
# Математическое ожидание для частично непрерывной функции M(x)
expected_value = 0
for index in range(3):
    definite_integral = INTEGRATED_FUNC_LIST[index](X_INTERVALS_LIST[index + 1]) - FUNCS_LIST[index](X_INTERVALS_LIST[index])
    expected_value += definite_integral
# рисуем график "r" это цвет
obj1.plot(X_LIST, Y_LIST, 'r')
obj1.set_title(f'M(x) = {expected_value}')
lgnd1 = obj1.legend(['My func'], loc='upper center', shadow=True)
lgnd1.get_frame().set_facecolor('#57f5ff')


X_INTERVALS_LIST[3] = X_MAX + 2
new_X_LIST = [(x/10) for index in range(3) for x in range(X_INTERVALS_LIST[index] * 10, int(X_INTERVALS_LIST[index+1]*10), int(H*10))]
new_Y_LIST = [FUNCS_LIST[index](x/10) for index in range(3) for x in range(X_INTERVALS_LIST[index]*10, int(X_INTERVALS_LIST[index+1]*10), int(H*10))]


a1, b1 = get_linear_coeff(X_LIST, Y_LIST)
# создаем список значений "у" для линейной функции типа a + bx
y_trend = [linear_func(x, a1, b1) for x in new_X_LIST]
# получаем коэффы детерминации и среднее отклонение
R_1 = get_R_2(X_LIST, Y_LIST, [a1, b1], func=linear_func)
otkl_x1, otkl_y1 = get_avg_deviation(X_LIST, y_trend)
obj2.plot(X_LIST, Y_LIST, 'r', new_X_LIST, y_trend, 'b', linestyle='solid')
obj2.set_title(f'R^2 = {R_1}\nS(x) = {otkl_x1}\nS(y) = {otkl_y1}\n')
lgnd2 = obj2.legend(['My func', f'y = {a1} + {b1}x'], loc='upper center', shadow=True)
lgnd2.get_frame().set_facecolor('#57f5ff')


# Для трех уравнений
a2, b2, c2 = get_koef_polim(X_LIST, Y_LIST)
y_trend2 = [quad_func(x, a2, b2, c2) for x in new_X_LIST]  
R_2 = get_R_2(X_LIST, Y_LIST, [a2, b2, c2], func=quad_func)
otkl_x2, otkl_y2 = get_avg_deviation(X_LIST, y_trend2)
obj3.plot(X_LIST, Y_LIST, 'r', new_X_LIST, y_trend2, 'b', linestyle='solid')
obj3.set_title(f'R^2 = {R_2}\nS(x) = {otkl_x2}\nS(y) = {otkl_y2}\n')
lgnd3 = obj3.legend(['My func', f'y = {a2}x^2 + {b2}x + {c2}'], loc='upper center', shadow=True)
lgnd3.get_frame().set_facecolor('#57f5ff')