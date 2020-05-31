<<<<<<< HEAD:Практика Алгоритмы Python3/Semestr2_algorithm/pract2/Task1p2/classCircle.py
from classFigure import Figure
from math import pi
class Circle(Figure):
=======
import classFigure
from math import pi
class Circle(classFigure.Figure):
>>>>>>> dev:Практика Алгоритмы Python3/Semestr2_algorithm/pract2/Task1/classCircle.py
    def __init__(self, r):
        self.r = r
        self.get_perimeter()
        self.get_square()

    def get_square(self):
        self.square = pi*self.r ** 2

    def get_perimeter(self):
        self.perimeter = 2*pi*self.r