from martix_and_vector_methods import get_matrix, get_vector, matrix_and_vector
from matrix_and_numb_methods import matrix_and_numb
from matrix_and_matrix_methods import matrix_and_matrix, checking_matr
def red_text(text):
    print("\033[31m"+str(text)+"\033[0m")
def info():
    print("""
    Доступные действия:
    1) умножение матрицы на вектор
    2) умножение матрицы на число
    3) умножение матрицы на матрицу
    """)

def start_matr():
    """Выбор действия и проверка условий ввода"""
    info()
    find = False
    while not find:
        try:
            choice = int(input("Выбор: "))
            if 0 < choice < 4:
                find = True
            else:
                print("Выбрать можно только действия: 1, 2, 3")
        except ValueError:
            print("Вводить нужно число...")

    if choice == 1:
        red_text("Ввод первой матрицы")
        matrix_arr, len_matrix_m, _ = get_matrix()
        red_text("Ввод вектора")
        vector_arr = get_vector(len_matrix_m)
        matrix_and_vector(matrix_arr, vector_arr)
    elif choice == 2:
        numb = int
        while type(numb) != int:
            try:
                numb = int(input("Введите число: "))
            except:
                print("Вы ввели не целое число!")
        red_text("Ввод матрицы")
        matrix_arr, _, _ = get_matrix()
        matrix_and_numb(numb, matrix_arr)

    elif choice == 3:
        red_text("Ввод первой матрицы")
        matr1, len1, _ = get_matrix()
        red_text("Ввод второй матрицы")
        matr2, _, len2 = get_matrix()
        if checking_matr(len1, len2):
            matrix_and_matrix(matr1, matr2)
        else:
            red_text("Нужно соблюдать условие, когда длина столбца первой матрицы равна длине строки другой матрицы")

if __name__ == "__main__":
    start_matr()