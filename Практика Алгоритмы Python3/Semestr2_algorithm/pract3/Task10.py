def seq_of_ones_and_zeros(a, b):
    """Даны числа a и b. Определите, сколько существует последовательностей из a нулей и b
    единиц, в которых никакие два нуля не стоят рядом"""
    if a > b + 1:
        return 0

    elif a == 0 or b == 0:
        return 1

    return seq_of_ones_and_zeros(a, b - 1) + seq_of_ones_and_zeros(a - 1, b - 1)


print(seq_of_ones_and_zeros(1, 2))