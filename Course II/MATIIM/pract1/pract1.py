import numpy as np

def task3(p, k):
    """Вероятность первого перехода за k шагов p^ ** k"""
    matrix_p = p
    len_p = len(p)          # Длина матрицы переходов
    for _ in range(1, k):
        new_matrix = np.zeros((len_p, len_p))    # Создание пустой матрицы заполненой 0
        for i in range(len_p):
            for j in range(len_p):
                s = 0
                for m in range(len_p):
                    if m != j:                        # пропуск перехода в состояние j
                        print(p[i, m], matrix_p[m, j])
                        s += p[i, m] * matrix_p[m, j] # сумма произведений вероятностей
                new_matrix[i, j] = s                  # добавляем вероятность перехода в новую матрицу  
        matrix_p = new_matrix
    return matrix_p

def task2(p, k, a0):
    """Вероятность состояний спустя k шагов A(k)"""
    result = np.linalg.matrix_power(p, k) # матрица p в k степени
    result = a0.dot(result)
    return result

def task1(p, k):
    """Вероятность перехода за k шагов p ** k"""
    result = np.linalg.matrix_power(p, k) # матрица p в k степени
    return result


# Входные данные
p = np.array([          # Матрица вероятностей перехода
    [0.1, 0.3, 0.4],
    [0.29, 0.21, 0.5],
    [0.2, 0.67, 0.13]]
)

k = 4   # Кол-во k = 4 шагам
a0 = np.array([0.2, 0.4, 0.1]) # вектор A0 вероятности начальных состояний
print("Матрица состояний:\n", p)
print("Кол-во шагов:", k)
print("A0:\n", a0)

# Task1
print("\nTask1")
print("p ** k =\n", task1(p, k))

# Task2
print("\nTask2:")
print("A(k) =", task2(p, k, a0))

# Task3
print("\nTask3:")
print("p^ ** k =\n", task3(p, k))
