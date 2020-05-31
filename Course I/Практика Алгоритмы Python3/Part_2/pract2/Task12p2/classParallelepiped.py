import classBody
from math import pi
class Parallelepiped(classBody.Body):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.get_volume()
        self.get_surface()
    def get_surface(self):
        a = self.a
        b = self.b
        c = self.c
        self.surface_square = 2 * (a * b + b * c + a * c)
    def get_volume(self):
        self.volume = self.a * self.b * self.c
class Ball(classBody.Body):
    def __init__(self, r):
        self.r = r
        self.get_volume()
        self.get_surface()
    def get_surface(self):
        self.surface_square = 4 * pi * pow(self.r, 2)
    def get_volume(self):
        self.volume = (4 / 3) * pi * pow(self.r, 3)