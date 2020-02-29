import math

def recurrent(x, n=0, e=0):
    if x > 1:
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
            for i in range(1, n):
                M = -M
                L = L + 2
                P = P * x**2
                res += M / (L * P)
                s += f'{M}/({L}*{P}) + '  # Проверка ряда
        return math.pi / 2 + res, s
    else:
        return None, None

# Task_1
x = float(input('x = '))
print(math.atan(x), f'- True при x = {x}')
print('//////////////////////////////////')
for i in range(5, 11):
    res, s = recurrent(x, i)
    print(res, f'- при n = {i}')
    # print(s[:-2])  # Проверка ряда
    if i == 10:
        print('//////////////////////////////////')
    else:
        print()

# Task_2
x = float(input('x = '))
print(math.atan(x), '- True')
print()
res, s = recurrent(x=x, e=10**-3)
print('С точностью E = 10^-3:', res)
print()
res, s = recurrent(x=x, e=10**-5)
print('С точностью E = 10^-5:', res)
