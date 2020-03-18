import math
class Triangle:
    def __init__(self, a, b, angle):
        self.a, self.b, self.angle = a, b, angle
        self.get_perimetr()
        self.get_square()
    def get_perimetr(self):
        a, b, angle = self.a, self.b, self.angle
        c = math.sqrt(b**2 + a**2 - 2*b*a * math.cos(math.radians(angle)))
        self.c = c
        self.perimetr = a + b + c
    def get_square(self):
        a, b, c = self.a, self.b, self.c
        p = (a+b+c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        self.square = s
    def info(self, name_class):
        s, p = self.square, self.perimetr
        p = str(round(self.perimetr, 2))
        print("\n*class {}*".format(name_class))
        if type(self.square) == float:
            s = str(round(self.square, 2))
        print("Периметр: ", p, "\nПлощадь: ", s)