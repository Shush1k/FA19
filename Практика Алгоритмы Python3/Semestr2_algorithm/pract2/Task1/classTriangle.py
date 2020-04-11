import classFigure
import Trianglemethoods as TMs
class Triangle(classFigure.Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if self.check():
            self.get_square()
            self.get_perimeter()


    
    check = TMs.check
    get_square = TMs.get_square
    get_perimeter = TMs.get_perimeter