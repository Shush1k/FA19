import numpy as np
import random
class Matrix:
    def __init__(self):
        """Выбор действия и проверка условий ввода"""
        # Часть 1
        print("Задание 1")
        #self.matr1, len1_1, len1_2 = self.get_matrix()
        #print("Вторая матрица")
        #self.matr2, len2_1, len2_2 = self.get_matrix()
        self.matr1 = np.matrix( "-4 -1 2; 10 4 -1; 8 3 1")
        self.matr2 = np.matrix( "2 3 2; 5 5 3; 4 4 6")

        # Матрицы созданные
        print("Первая матрица: \n", self.matr1)
        print("Вторая матрица: \n", self.matr2)
        # Сумма
        #if self.checking_matr_plus(len1_1, len1_2, len2_1, len2_2):
        self.A_plus_B()
            
        # Разность
        #if self.checking_matr_plus(len1_1, len1_2, len2_1, len2_2):
        self.A_minus_B()
        
        # Определитель1
        print("Определитель 1")
        print(np.linalg.det(self.matr1))

        # Определитель2
        print("Определитель 2")
        print(np.linalg.det(self.matr2))

        # Трансп1
        print("Транспонированная 1")
        print(self.matr1.T)
        # Трансп2
        print("Транспонированная 2")
        print(self.matr2.T)
        # Обратная матрица 1 и 2
        print("Обратная матрица 1")
        print(np.linalg.inv(self.matr1))
        print("Обратная матрица 2")
        print(np.linalg.inv(self.matr2))

        # Матрицы A B C D
        A_matr = []
        A_matr.append(self.list_generate(2))
        A_matr.append(self.list_generate(2))
        A_matr = np.array(A_matr)
        print("Матрица А:\n", A_matr)

        B_matr = []
        B_matr.append(self.list_generate(3))
        B_matr.append(self.list_generate(3))
        B_matr = np.array(B_matr)
        print("Матрица B:\n", B_matr)

        C_matr = []
        C_matr.append(self.list_generate(2))
        C_matr.append(self.list_generate(2))
        C_matr.append(self.list_generate(2))
        C_matr = np.array(C_matr)
        print("Матрица C:\n", C_matr)

        D_matr = []
        D_matr.append(self.list_generate(1))
        D_matr.append(self.list_generate(1))
        D_matr = np.array(D_matr)
        print("Матрица D:\n", D_matr)
        # A*B, C*D, B*C, C*B
        print(self.matrix_and_matrix(A_matr, B_matr, "A*B"))
        print(self.matrix_and_matrix(C_matr, D_matr, "C*D"))
        print(self.matrix_and_matrix(B_matr, C_matr, "B*C"))
        print(self.matrix_and_matrix(C_matr, B_matr, "C*B"))

        # Часть 2
        print("Задание 2")

        self.matrix = [
                    [-8, 2, 0, -2],
                    [-6, -4, -2, -2],
                    [-10, 2, 0, 4],
                    [-2, -6, 8, -4]
                ]
        self.vector = [
                    [34],
                    [24],
                    [68],
                    [-36]
                ]

        print("\nРешение с помощью обратной матрицы")
        print('Результат вычислений:')
        answers_inv = self.get_inv()
        print(self.matrix_trans(answers_inv))

        print("\nРешение матрицы методом Крамера")
        print('Результат вычислений:')
        answers_kram = self.get_Kramer()
        print(self.matrix_trans(answers_kram))
        print('\nПроверка\nПолучим матрицу свободных коэффициентов')
        print('Результаты вычисления:')
        print(self.matrix_trans(self.matrix_mult(self.matrix, answers_inv)))
      

        
    def get_inv(self):
        inverse = self.matrix_inverse(self.matrix)
        answers = self.matrix_mult(inverse, self.vector)
        return answers
    
    def get_Kramer(self):
        kramer = [a + b for a,b in zip(self.matrix, self.vector)]
        det = self.matrix_det(self.matrix)
        n = len(kramer)
        tmp = list(zip(*kramer))
        b = tmp[-1]
        del tmp[-1]
     
        if not det:
            raise RuntimeError("Решения нет")
     
        result = []
        for i in range(n):
            a = tmp[:]
            a[i] = b
            result.append(self.matrix_det(a) / det)
        return [result]
    
    def matrix_det(self, matrix, total=0):
        indices = list(range(len(matrix)))

        if len(matrix) == 2 and len(matrix[0]) == 2:
            val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            return val
     
        for fc in indices:
            minor = self.matrix_minor(0, fc, matrix) 
            sub_det = self.matrix_det(minor)
            total += ((-1)**(fc % 2)) * matrix[0][fc] * sub_det 
     
        return total
        
    
    def matrix_trans(self, matrix):
        output_result = []
        for index_i in range(len(matrix[0])):
            temp_list = []
            for index_j in range(len(matrix)):
                temp_list.append(matrix[index_j][index_i])
            output_result.append(temp_list)
        return output_result
    
    
    def matrix_inverse(self, matrix):
        
        determ = self.matrix_det(matrix)
        
        if (determ != 0):
            inverse_matrix = self.matrix_mult_n(self.matrix_union(matrix), 1/determ)
            return inverse_matrix
        else:
            print("Матрица вырожденная\nОбратная для неё не существует")
            return None
        
        
    def matrix_mult_n(self, matrix, number):
        for index_i in range(len(matrix)):
            for index_j in range(len(matrix[0])):
                matrix[index_i][index_j] *= number
        return matrix
    
    
    def matrix_union(self, matrix):

        transp_matrix = self.matrix_trans(matrix)
        
        union = []
        
        for i in range(len(transp_matrix)):
            temp = []
            for j in range(len(transp_matrix[0])):
                minor_determ = (-1)**(i+1 + j+1) * self.matrix_det(self.matrix_minor(matrix = transp_matrix, i=i, j=j))
                temp.append(minor_determ)
            union.append(temp)
        
        return union
    
    
    def matrix_minor(self, i, j, matrix):
        
        matrix_minor = []
        for row in (matrix[:i]+matrix[i+1:]):
            matrix_minor.append(row[:j] + row[j+1:]) 
        
        return matrix_minor
    
    
    def matrix_mult (self, first_matrix, second_matrix):
        output_res = [[0 for _ in range(len(second_matrix[0]))] for _ in range(len(first_matrix))]
        for i in range(len(first_matrix)):
            for j in range(len(second_matrix[0])):
                for k in range(len(first_matrix[0])):
                    output_res[i][j] += first_matrix[i][k] * second_matrix[k][j]
                output_res[i][j] = round(output_res[i][j])
        return output_res


    def A_plus_B(self):
        result = self.matr1 + self.matr2
        print("\nСумма матриц:\n", result)
        return result

    def A_minus_B(self):
        result = self.matr1 - self.matr2
        print("\nРазность матриц\n", result)
        return result


    def matrix_and_matrix(self, matr1, matr2, name):
        """Матрица умножается на матрицу"""
        result = matr1.dot(matr2)
        print(f"\nПроизведение матриц {name}:\n", result)
        return ""
        
    def get_matrix(self):
        """Создание матрицы"""
        #try:
        #    n = int(input('Количество строк матрицы: '))
        #    m = int(input('Количество столбцов матрицы: '))
        #except ValueError:
        #    return self.get_matrix()
        n, m = 3, 3
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

    
    def checking_matr_plus(self, len1_1, len1_2, len2_1, len2_2):
        """Проверка на количество столбцов у матрицы и количество строк вектора"""
        if len1_1 == len1_2 == len2_1 == len2_2:
          return True
        return False
    
    def checking_matr_multi(self, len1, len2):
        """Проверка двух длин"""
        if len1 == len2:
            print("Длины матриц равны")
            return True
        print("Длины матриц не равны")
        return False

    def list_generate(self, list_r):
        res = [random.randint(1, 10) for i in range(list_r)]
        return res


if __name__ == "__main__":
    Matrix()