import classmethods
class Task4:
    """
    Разработайте класс с соответствующими методами, обеспечивающий нахождение
    значения функции г и вывод на экран результатов вычислений, Исходные данные в соответстви
    с вариантом функции первого семестра.
    """
    def __init__(self):
        print("Task4")
        try:
            self.x = float(input("x=:",))
            self.equation()
        except ValueError:
            print("Введите только число")
    equation = classmethods.equation