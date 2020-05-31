from classTriangle import Triangle
import math
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