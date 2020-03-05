"""
Задача 1. Создайте класс ФИГУРА с методами вычисления площади и периметра,
а также методом, выводящим информацию о фигуре на экран.
Создайте дочерние классы ПРЯМОУГОЛЬНИК, КРУГ, ТРЕУГОЛЬНИК со своими методами вычисления площади и периметра.
Создайте список n фигур и выведите полную информацию о фигурах на экран.
"""

from math import pi, sqrt
from random import randint


class Figure:
    """С методами вычисления площади и периметра"""

    def __init__(self, a, b, c, r, ):
        self.a = a
        self.b = b
        self.c = c
        self.r = r

    def get_perimeter(self):
        self.perimeter = 0

    def get_square(self):
        self.square = 0

    def info(self, name_class):
        s = self.square
        p = self.perimeter
        print("\n*class {}*".format(name_class))
        if type(self.square) == float or type(self.perimeter) == float:
            s = str(round(self.square, 2))
            p = str(round(self.perimeter, 2))
        if name_class == "Rectangle":
            print("a =", self.a, "b =", self.b)
        elif name_class == "Circle":
            print("r =", self.r)
        elif name_class == "Triangle":
            print("a =", self.a, "b =", self.b, "c =", self.c)
        print("Площадь фигуры:", s, "\nПериметр фигуры:", p)


class Rectangle(Figure):
    """
    Класс прямоугольника
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.get_perimeter()
        self.get_square()

    def get_perimeter(self):
        self.perimeter = (self.a + self.b) * 2

    def get_square(self):
        self.square = self.a * self.b


class Circle(Figure):
    def __init__(self, r):
        self.r = r
        self.get_perimeter()
        self.get_square()

    def get_square(self):
        self.square = pi*self.r ** 2

    def get_perimeter(self):
        self.perimeter = 2*pi*self.r


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if self.check():
            self.get_square()
            self.get_perimeter()

    def check(self):
        a = self.a
        b = self.b
        c = self.c

        if a + b <= c or a + c <= b or b + c <= a:
            self.square = "Не существует"
            self.perimeter = "Не существует"
            return False
        return True

    def get_square(self):
        p = (self.a+self.b+self.c)/2
        s = sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))
        self.square = s

    def get_perimeter(self):
        self.perimeter = self.a + self.b + self.c


def main():
    try:
        n = int(input("Количество фигур = "))
    except ValueError:
        print("0_0 упс...")
        return

    d = {
        1: Rectangle,
        2: Circle,
        3: Triangle
    }
    figures_list = []

    for _ in range(n):

        d_val = {
            1: [randint(1, 100), randint(1, 100)],
            2: [randint(1, 100)],
            3: [randint(1, 100), randint(1, 100), randint(1, 100)]
        }

        r = randint(1, 3)
        figures_list.append(d[r](*d_val[r]))

    for figure in figures_list:
        figure.info(type(figure).__name__)


if __name__ == "__main__":
    main()
