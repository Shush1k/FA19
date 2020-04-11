import numpy as np
def matrix_and_matrix(matr1, matr2):
    """Матрица умножается на матрицу"""
    result = matr1.dot(matr2)
    print("Первая матрица:\n", matr1, "\nВторая матрицы:\n", matr2,"\nПолученная матрица:\n", result)
    return result
def get_matrix():
    """Создание матрицы"""
    try:
        n = int(input('Количество строк матрицы: '))
        m = int(input('Количество столбцов матрицы: '))
    except ValueError:
        return get_matrix()
    print("Можете вводить числа матрицы:")
    try:
        arr = [[int(input("Число: ")) for _ in range (m)] for _ in range (n)]
    except ValueError:
        print("Вводите матрицу снова")
        return get_matrix()    
    if type(n) == int and type(m) == int and type(arr) == list and 1 < n and 1 < m:
        matrix_arr = np.array(arr)
        len_matrix_m = m
        len_matrix_n = n
        return matrix_arr, len_matrix_m, len_matrix_n
    else:
        print("Не выполнены условия создания матрицы: 1 < n and 1 < m")
        return get_matrix()
def checking_matr(len1, len2):
    """Проверка двух длин"""
    if len1 == len2:
        print("Длины матриц равны")
        return True
    print("Длины матриц не равны")
    return False

def main():
    matr1, len1, _ = get_matrix()
    print("Вторая матрица")
    matr2, _, len2 = get_matrix()
    if checking_matr(len1, len2):
        matrix_and_matrix(matr1, matr2)
    else:
        print("Длина столбца первой матрицы должна быть равна длине строки второй матрицы")
if __name__ == "__main__":
    main()