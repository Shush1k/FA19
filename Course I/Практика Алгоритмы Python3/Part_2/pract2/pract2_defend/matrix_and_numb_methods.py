import numpy as np
def matrix_and_numb(numb, matrix_arr):
    """Матрица умножается на число"""
    result = matrix_arr.dot(numb) 
    print("\nИзначальная матрица:\n", matrix_arr, "\nЧисло на которое умножали:", numb, "\nПолученная матрица:\n"+str(result))
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

def main():
    numb = int
    while type(numb) != int:
        try:
            numb = int(input("Введите число: "))
        except:
            print("Вы ввели не целое число!")
    matrix_arr, _, _ = get_matrix()
    matrix_and_numb(numb, matrix_arr)

if __name__ == "__main__":
    main()