import Figuremethoods as FMs
class Figure:
    """С методами вычисления площади и периметра"""
    def __init__(self, a, b, c, r, ):
        self.a = a
        self.b = b
        self.c = c
        self.r = r

    get_square = FMs.get_square
    get_perimeter = FMs.get_perimeter
    info = FMs.info

