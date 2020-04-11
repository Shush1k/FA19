import numpy as np
class Matrix:
    def __init__(self):
        self.start_matr()

    def info(self):
        print(        """
        Доступные действия:
        1) умножение матрицы на вектор
        2) умножение матрицы на число
        3) умножение матрицы на матрицу
        """)

    def start_matr(self):
        """Выбор действия и проверка условий ввода"""
        self.info()
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
            self.get_matrix()
            self.get_vector()
            if self.checking_vect():
                self.matrix_and_vector()
        elif choice == 2:
            numb = int
            while type(numb) != int:
                try:
                    numb = int(input("Введите число: "))
                except:
                    print("Вы ввели не целое число!")
            self.get_matrix()
            self.matrix_and_numb(numb)

        elif choice == 3:
            self.matr1, len1, _ = self.get_matrix()
            print("Вторая матрица")
            self.matr2, _, len2 = self.get_matrix()
            if self.checking_matr(len1, len2):
                self.matrix_and_matrix()
        else:
            pass

    def matrix_and_vector(self):
        """Матрица умножается на вектор"""
        result = self.matrix_arr.dot(self.vector_arr) 
        print("\nИзначальная матрица:\n"+str(self.matrix_arr), "\nВектор:", self.vector_arr,"\nПолученная матрица:\n"+str(result))
        return result

    def matrix_and_numb(self, numb):
        """Матрица умножается на число"""
        result = self.matrix_arr.dot(numb) 
        print("\nИзначальная матрица:\n", self.matrix_arr, "\nЧисло на которое умножали:", numb, "\nПолученная матрица:\n"+str(result))
        return result

    def matrix_and_matrix(self):
        """Матрица умножается на матрицу"""
        result = self.matr1.dot(self.matr2)
        print("Первая матрица:\n", self.matr1, "\nВторая матрицы:\n", self.matr2,"\nПолученная матрица:\n", result)
        return result
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

    def get_vector(self):
        """Создание вектора"""
        n = self.len_matrix_m
        print("Можете вводить числа вектора:")
        try:
            arr = [int(input("Число: ")) for _ in range (n)]
        except ValueError:
            return self.get_vector()   

        if type(n) == int and type(arr) == list:
            self.vector_arr = np.array(arr)
            self.len_vector = n
        return self.vector_arr, self.len_vector
    
    def checking_vect(self):
        """Проверка на количество столбцов у матрицы и количество строк вектора"""
        if self.len_matrix_m == self.len_vector:
          return True
        return False
    
    def checking_matr(self, len1, len2):
        """Проверка двух длин"""
        if len1 == len2:
            print("Длины матриц равны")
            return True
        print("Длины матриц не равны")
        return False


def main():
    Matrix()
    

if __name__ == "__main__":
    main()