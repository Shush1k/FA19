class Body:
    def __init__(self, a, b, c, r, h):
        self.a = a
        self.b = b
        self.c = c
        self.r = r
        self.h = h
    def get_surface(self):
        self.surface_square = 0
    def get_volume(self):
        self.volume = 0
    def info(self, name_class):
        s = self.surface_square
        v = self.volume
        print("\n*class {}*".format(name_class))
        if type(self.surface_square) == float or type(self.volume) == float:
            s = str(round(self.surface_square, 2))
            v = str(round(self.volume, 2))
        if name_class == "Parallelepiped":
            print("a =", self.a, "b =", self.b, "c =", self.c)
        elif name_class == "Ball":
            print("r =", self.r)
        elif name_class == "Pyramid":
            print("h =", self.h)
        print("Площадь поверхности фигуры:", s, "\nОбъем фигуры:", v)