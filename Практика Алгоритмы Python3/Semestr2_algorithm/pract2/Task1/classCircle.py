import classFigure
from math import pi, sqrt
class Circle(classFigure.Figure):
    def __init__(self, r):
        self.r = r
        self.get_perimeter()
        self.get_square()

    def get_square(self):
        self.square = pi*self.r ** 2

    def get_perimeter(self):
        self.perimeter = 2*pi*self.r