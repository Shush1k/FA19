from classTriangle import Triangle
import math
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