"""
Задача  3. Создайте класс ТРЕУГОЛЬНИК, заданный длинами двух сторон и угла между ними,
с методами вычисления площади и периметра треугольника, а также методом,
выводящим информацию о фигуре на экран.
Создайте дочерние классы ПРЯМОУГОЛЬНЫЙ, РАВНОБЕДРЕННЫЙ, РАВНОСТОРОННИЙ со своими
методами вычисления площади и периметра.
Создайте список n треугольников и выведите полную информацию о треугольниках на экран.
"""

import math
from random import randint


class Triangle:

    def __init__(self, a, b, angle):
        self.a = a
        self.b = b
        self.angle = angle

        self.get_perimetr()
        self.get_square()

    def get_perimetr(self):
        a = self.a
        b = self.b
        angle = self.angle
        c = math.sqrt(b**2 + a**2 - 2*b*a * math.cos(math.radians(angle)))
        self.c = c
        self.perimetr = a + b + c

    def get_square(self):
        a = self.a
        b = self.b
        c = self.c
        p = (a+b+c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        self.square = s

    def info(self, name_class):
        s = self.square
        p = self.perimetr
        p = str(round(self.perimetr, 2))
        print("\n*class {}*".format(name_class))
        if type(self.square) == float:
            s = str(round(self.square, 2))
        print("Периметр: ", p, "\nПлощадь: ", s)


class RectangularTriangle(Triangle):
    def __init__(self, a, b, angle=90):
        super().__init__(a, b, angle)
        self.angle = angle
        self.a = a
        self.b = b

        self.get_square()
        self.get_perimetr()

    def get_square(self):
        self.square = (1/2)*self.a*self.b

    def get_perimetr(self):
        self.c = math.sqrt(pow(self.a, 2)+pow(self.b, 2))
        self.perimetr = self.a + self.b + self.c


class IsoscelesTriangle(Triangle):
    def __init__(self, a, b, angle):
        super().__init__(a, b, angle)
        self.a = a
        self.b = b

    def get_perimetr(self):
        self.perimetr = 2*self.b + self.a

    def get_square(self):
        a = self.a
        b = self.b
        try:
            # Половина основания
            half_a = a/2
            h = math.sqrt(pow(b, 2) - pow(half_a, 2))
            self.square = (a*h)/2
        except ValueError:
            self.square = "Ошибка площади"


class EquilateralTriangle(Triangle):
    def __init__(self, a, b, angle):
        super().__init__(a, b, angle)
        self.a = a

    def get_perimetr(self):
        self.perimetr = self.a * 3

    def get_square(self):
        try:
            a = self.a
            h = math.sqrt(pow(a, 2) - (pow(a, 2)/4))
            self.square = (a*h)/2
        except ValueError:
            self.square = "Ошибка площади"


def main():
    try:
        n = int(input("Количество треугольников = "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    triangle_list = []
    d = {
        1: Triangle,
        2: RectangularTriangle,
        3: IsoscelesTriangle,
        4: EquilateralTriangle
    }

    for _ in range(n):
        r = randint(1, 4)

        d_val = [randint(1, 100), randint(1, 100), randint(1, 100)]
        triangle_list.append(d[r](*d_val))

    for triangle in triangle_list:
        triangle.info(type(triangle).__name__)


if __name__ == "__main__":
    main()
