"""
Задача 16*:
Выполнить программную реализацию калькулятора матриц.
"""
import numpy as np
import random
class Matrix:
    def __init__(self):
        """Выбор действия и проверка условий ввода"""
        # Создание матриц
        print("Заполните первую матрицу!")
        self.matr1, len1_1, len1_2 = self.get_matrix()
        print("Заполните вторую матрицу!")
        self.matr2, len2_1, len2_2 = self.get_matrix()
        print("Первая матрица: \n", self.matr1)
        print("Вторая матрица: \n", self.matr2)

        print("\nБазовые операции с матрицами:")
        # Сумма
        if self.checking_matr_plus(len1_1, len1_2, len2_1, len2_2, "Сложение"):
            self.A_plus_B()
            
        # Разность
        if self.checking_matr_plus(len1_1, len1_2, len2_1, len2_2, "Вычитание"):
            self.A_minus_B()

        # Произведение
        if self.checking_matr_multi(len1_2, len2_1):
            self.matrix_and_matrix(self.matr1, self.matr2)


    def A_plus_B(self):
        result = self.matr1 + self.matr2
        print("\nСумма матриц:\n", result)
        return result

    def A_minus_B(self):
        result = self.matr1 - self.matr2
        print("\nРазность матриц:\n", result)
        return result


    def matrix_and_matrix(self, matr1, matr2):
        """Матрица умножается на матрицу"""
        result = matr1.dot(matr2)
        print(f"\nПроизведение матриц:\n", result)
        return ""
        
    def get_matrix(self):
        """Создание матрицы"""
        try:
            n = int(input('Количество строк матрицы: '))
            m = int(input('Количество столбцов матрицы: '))
        except ValueError:
            return self.get_matrix()
        print("Можете вводить числа матрицы:")
        try:
            arr = [[int(input("Число: ")) for _ in range (m)] for _ in range (n)]
        except ValueError:
            print("Вводите матрицу снова")
            return self.get_matrix()    
        if type(n) == int and type(m) == int and type(arr) == list and 1 < n and 1 < m:
            self.matrix_arr = np.array(arr)
            self.len_matrix_m = m  
            self.len_matrix_n = n  
            return self.matrix_arr, self.len_matrix_m, self.len_matrix_n
        else:
            print("Не выполнены условия создания матрицы: 1 < n and 1 < m")
            return self.get_matrix()

    
    def checking_matr_plus(self, len1_1, len1_2, len2_1, len2_2, text):
        """Проверка длин"""
        if len1_1 == len1_2 == len2_1 == len2_2:
          return True
        print(f"{text} данных матриц невозможно")
        return False
    
    def checking_matr_multi(self, len1, len2):
        """Проверка столбца matr1 и строки matr2"""
        if len1 == len2:
            return True
        print("Произведение данных матриц невозможно")
        return False


if __name__ == "__main__":
    Matrix()