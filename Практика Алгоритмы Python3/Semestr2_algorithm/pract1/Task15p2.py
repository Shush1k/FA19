"""
Задача 15. Создайте класс ПРОГРЕССИЯ с методами вычисления N-го элемента прогрессии,
ее суммы и методом, выводящим сумму на экран.
Создайте дочерние классы: АРИФМЕТИЧЕСКАЯ, ГЕОМЕТРИЧЕСКАЯ со своими методами вычисления.
Создайте список п прогрессий и выведите сумму каждой из них экран.
"""
from random import randint


class Progression:
    def __init__(self, a1, a2, n):
        self.a1 = a1
        self.a2 = a2
        self.n = n

    def calculate(self):
        pass

    def info(self):
        pass


class Arithmetic(Progression):
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


class Geometric(Progression):
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


def main():
    try:
        n = int(input("Кол-во прогрессий = "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1: Arithmetic,
        2: Geometric
    }

    prog_list = []

    for _ in range(n):
        d_args = {
            1: [randint(-1000, 1000), randint(-1000, 1000), randint(1, 10)],
            2: [randint(-1000, 1000), randint(-1000, 1000)],
        }

        r = randint(1, 2)
        prog_list.append(d[r](*d_args[r]))

    for prog in prog_list:
        prog.info()


if __name__ == "__main__":
    main()
