def enn_plus_odin(N_max, N_index = 1):
    """Дано натуральное число n. Выведите все числа от 1 до n."""
    if N_index > N_max:
        return
    print(N_index, end= " ")
    enn_plus_odin(N, N_index+1)

def input_N():
    """Ввод числа N"""
    try:
        N = int(input("Ввод: "))
        return N
    except ValueError:
        print("Вводить число!")
        return input_N()
    
N = input_N()
enn_plus_odin(N)
