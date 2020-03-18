import classFigure
import Trianglemethoods as TMethhod
class Triangle(classFigure.Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if self.check():
            self.get_square()
            self.get_perimeter()

    check = TMethhod.check
    get_square = TMethhod.get_square
    get_perimeter = TMethhod.get_perimeter