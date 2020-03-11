import classFigure
class Triangle(classFigure.Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if self.check():
            self.get_square()
            self.get_perimeter()

    def check(self):
        a = self.a
        b = self.b
        c = self.c

        if a + b <= c or a + c <= b or b + c <= a:
            self.square = "Не существует"
            self.perimeter = "Не существует"
            return False
        return True

    def get_square(self):
        p = (self.a+self.b+self.c)/2
        s = sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))
        self.square = s

    def get_perimeter(self):
        self.perimeter = self.a + self.b + self.c