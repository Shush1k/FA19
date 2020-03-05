"""
Задача  12. Создайте класс ТЕЛО с методами вычисления площади поверхности и объема,
а также методом, выводящим информацию о фигуре на экран.
Создайте дочерние классы ПАРАЛЛЕЛЕПИПЕД, ШАР, ПИРАМИДА со своими методами вычисления площади и объема.
Создайте список п фигур и выведите полную информацию о фигурах на экран.
"""
from math import pi
from random import randint


class Body:
    """с методами вычисления площади поверхности и объема"""

    def __init__(self, a, b, c, r, h):
        self.a = a
        self.b = b
        self.c = c
        self.r = r
        self.h = h

    def get_surface(self):
        self.surface_square = 0

    def get_volume(self):
        self.volume = 0

    def info(self, name_class):
        s = self.surface_square
        v = self.volume
        print("\n*class {}*".format(name_class))
        if type(self.surface_square) == float or type(self.volume) == float:
            s = str(round(self.surface_square, 2))
            v = str(round(self.volume, 2))
        if name_class == "Parallelepiped":
            print("a =", self.a, "b =", self.b, "c =", self.c)
        elif name_class == "Ball":
            print("r =", self.r)
        elif name_class == "Pyramid":
            print("h =", self.h)

        print("Площадь поверхности фигуры:", s, "\nОбъем фигуры:", v)


class Parallelepiped(Body):

    def __init__(self, a, b, c):
        #a, b, c - ребра
        self.a = a
        self.b = b
        self.c = c

        self.get_volume()
        self.get_surface()

    def get_surface(self):
        a = self.a
        b = self.b
        c = self.c
        self.surface_square = 2 * (a * b + b * c + a * c)

    def get_volume(self):
        self.volume = self.a * self.b * self.c


class Ball(Body):

    def __init__(self, r):
        self.r = r

        self.get_volume()
        self.get_surface()

    def get_surface(self):
        self.surface_square = 4 * pi * pow(self.r, 2)

    def get_volume(self):
        self.volume = (4 / 3) * pi * pow(self.r, 3)


class Pyramid(Body):

    def __init__(self, S_footprint, S_lateral, h):
        # S_footprint - площадь основания
        # S_lateral - площадь боковой поверхности
        self.S_footprint = S_footprint
        self.S_lateral = S_lateral
        self.h = h

        self.get_volume()
        self.get_surface()

    def get_surface(self):
        self.surface_square = self.S_footprint + 4 * self.S_lateral

    def get_volume(self):
        self.volume = (1 / 3) * self.S_footprint * self.h


def main():
    try:
        n = int(input("Количество фигур = "))
    except ValueError:
        print("0_0 упс...")
        return

    d = {
        1: Parallelepiped,
        2: Ball,
        3: Pyramid
    }

    figures_list = []

    for _ in range(n):
        d_args = {
            1: [randint(1, 100), randint(1, 100), randint(1, 100)],
            2: [randint(1, 100)],
            3: [randint(1, 100), randint(1, 100), randint(1, 100)],
        }

        r = randint(1, 3)
        figures_list.append(d[r](*d_args[r]))

    for figure in figures_list:
        figure.info(type(figure).__name__)


if __name__ == "__main__":
    main()
