<<<<<<< HEAD:Практика Алгоритмы Python3/Semestr2_algorithm/pract2/Task1p2/classRectangle.py
from classFigure import Figure
class Rectangle(Figure):
=======
import classFigure
class Rectangle(classFigure.Figure):
>>>>>>> dev:Практика Алгоритмы Python3/Semestr2_algorithm/pract2/Task1/classRectangle.py
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
