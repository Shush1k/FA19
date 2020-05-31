import math
import numpy as np
import matplotlib.pyplot as plt
import random

def numerical_derivative(func, epsilon=0.0000000000001):
    def deriv_func(x):
        diffur = (func(x + epsilon) - func(x)) / epsilon
        return diffur
    return deriv_func

def teylor_linearization (function, x0 = 1):
    function_deriv = numerical_derivative(function)
    b = function(x0) - x0 * function_deriv(x0)
    a = function_deriv(x0)
    return lambda x: a * x + b, x0


def deriv_function (u, y0=0, T=2, h=0.01, k=5):
    y_list = [0]
    x_list = list(np.arange(0, 40, 0.01))
    for _ in range(len(x_list)-1):
        y_next = (h*k / T) * u + (1 - h/T)*y_list[-1]
        y_list.append(y_next)
    return y_list

#Функция линеаризации
func_line = lambda x: pow(x, 2) / math.sqrt(4 - 5 * x)

fig, (ax1, ax2, ax3) = plt.subplots(
    nrows=3, ncols=1,                   
    figsize=(12, 15)                    
)

x_list = list(np.arange(-20, -4, 0.1))
y_list = [func_line(x) for x in x_list]

ax1.plot (x_list, y_list, 'r')                                                                                          
lgnd1 = ax1.legend(['Исходная функция'], loc='upper center', shadow=True)    
lgnd1.get_frame().set_facecolor('#ffb19a')

linearizated_function, x0 = teylor_linearization(func_line, x0=random.randint(-20, -4))           
y_linear = [linearizated_function(x) for x in x_list]
ax2.plot(x_list, y_list, 'r', x_list, y_linear, 'b', linestyle='solid')               
lgnd2 = ax2.legend(['Исходная функция', f'Линеаризованная функция для x0 = {x0}'], loc='upper center', shadow=True)
lgnd2.get_frame().set_facecolor('#ffb19a')

x_list = list(np.arange(0, 40, 0.01))
y_list = deriv_function(2)
ax3.plot(x_list, y_list, 'r', linestyle='solid')
ax3.set_title(f"Решение для дифференциального уравнения 2у' + y = {5*2}:")