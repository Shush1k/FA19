import numpy as np
def matrix_and_vector(matrix_arr, vector_arr):
    """Матрица умножается на вектор"""
    result = matrix_arr.dot(vector_arr) 
    print("\nИзначальная матрица:\n"+str(matrix_arr), "\nВектор:", vector_arr,"\nПолученная матрица:\n"+str(result))
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

def get_vector(len_matrix_m):
    """Создание вектора"""
    n = len_matrix_m
    try:
        arr = [int(input("Число: ")) for _ in range (n)]
    except ValueError:
        return get_vector(n)   

    if type(n) == int and type(arr) == list:
        vector_arr = np.array(arr)
    return vector_arr

def main():
    matrix_arr, len_matrix_m, _ = get_matrix()
    vector_arr = get_vector(len_matrix_m)
    matrix_and_vector(matrix_arr, vector_arr)

if __name__ == "__main__":
    main()