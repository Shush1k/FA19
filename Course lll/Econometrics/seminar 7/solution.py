def interval(b, sigma, t):
    return (b - sigma * t, b + sigma * t)


def sigma_(b, t):
    return b / t


def long_short_test(RSS_short, RSS_long, n, m, q):
    return (RSS_short - RSS_long) / RSS_long * (n - m) / q

def t_(b, sigma):
    return b / (sigma * b)

def DW(n, k, RSS):
    """Дербина-Уотсона"""
    return 1 / (n-k-1) * RSS


# \frac{-2 - 1.5 * 3}{-2 + 1.5 * 3}

# -6,5 \leq B_{j} \leq 2,5

# 5.4 - 0.01 * 3
# 5.37 \leq B_{j} \leq 5.43

# Задача 3
# 102.5 - 102.5/7.07, 2.3
s1 = sigma_(46.9, 11)
s2 = sigma_(102.5, 7.07)
print(interval(102.5, sigma_(102.5, 7.07), 2.3))  # sigma_ число в скобках под B^

print("Задача 3:", interval(46.9, sigma_(46.9, 11), 2.3))

print("Задача 4:", long_short_test(60, 10, 55, 5, 2))

print("Задача 7:")

print(t_(1, 2))
print(t_(0.14, 0.02))
# tb1 = 0.5 tb2=7
# t_набл < t_tabl
# 0.5 < 2 незначим
# 7 > 2 значим
# СТЬЮДЕНТ.РАСПОБР()

print("Задача 8:")
DW = DW(13, 2, 40)
D_B0 = 4.08 * DW
D_B1 = 0.02 * DW
D_B2 = 0.01 * DW

print(D_B0, D_B1, D_B2)
# n- кол-во наблюдений
# K - кол-во x