# Figure methods
def get_perimeter(self):
    self.perimeter = 0
def get_square(self):
    self.square = 0
def info(self, name_class):
    s = self.square
    p = self.perimeter
    print("\n*class {}*".format(name_class))
    if type(self.square) == float or type(self.perimeter) == float:
        s = str(round(self.square, 2))
        p = str(round(self.perimeter, 2))
    if name_class == "Rectangle":
        print("a =", self.a, "b =", self.b)
    elif name_class == "Circle":
        print("r =", self.r)
    elif name_class == "Triangle":
        print("a =", self.a, "b =", self.b, "c =", self.c)
    print("Площадь фигуры:", s, "\nПериметр фигуры:", p)