def N_REVERSED(n, n_rev=0):
    """Дано число n, десятичная запись которого не содержит нулей. Получите число,
    записанное теми же цифрами, но в противоположном порядке."""
    if n == 0:
        return n_rev
    else:
        return N_REVERSED(n//10, n_rev*10 + n%10)

def input_N():
    #Ввод числа N
    try:
        N = int(input("Ввод: "))
        return N
    except ValueError:
        print("Вводить число!")
        return input_N()

print(N_REVERSED(input_N()))