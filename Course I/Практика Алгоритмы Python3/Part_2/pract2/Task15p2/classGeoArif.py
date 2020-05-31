import classProgression
class Arithmetic(classProgression.Progression):
    def __init__(self, a1, a2, n):
        super().__init__(a1, a2, n)
        self.calculate()
    def calculate(self):
        self.S = (self.a1 + self.a2)*self.n/2
        return self.S
    def info(self):
        print("\n*class АРИФМЕТИЧЕСКАЯ*\n")
        print("a1 =", self.a1, "a2 =", self.a2, "n =", self.n)
        print("Сумма арифметической прогрессии:", self.S)
class Geometric(classProgression.Progression):
    def __init__(self, b1, q):
        self.b1 = b1
        self.q = q
        self.calculate()
    def calculate(self):
        self.S = self.b1 / (1 - self.q)
        return self.S
    def info(self):
        print("\n*class ГЕОМЕТРИЧЕСКАЯ*\n")
        print("b1 =", self.b1, "q =", self.q)
        print("Сумма геометрической прогрессии:", self.S)