import classTriangle
import math
class IsoscelesTriangle(classTriangle.Triangle):
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