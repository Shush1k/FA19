"""
Задача 10. Создайте класс ТРАНСПОРТ с методами,
позволяющими вывести на экран информацию о транспортном средстве, а также определить,
находится ли транспортное средство в пределах заданных координат.
Создайте дочерние классы САМОЛЕТ (марка, максимальные скорость и высота, количество пассажиров, координаты),
АВТОМОБИЛЬ (марка, номер, год выпуска, координаты),
КОРАБЛЬ (название, координаты, скорость, количество пассажиров, порт приписки)
со своими методами вывода информации на экран и определения присутствия
транспортного средства в пределах заданных координат.
Создайте список из п транспортных средств, выведите полную информацию из базы на экран,
а также организуйте поиск транспортных средств, которые сейчас находятся в пределах заданных координат.
"""
from random import randint
from faker import Faker


class Transport:
    def __init__(self, mark, coordinate):
        self.mark = mark
        self.coordinate = coordinate

    def info(self):
        print("\n*Class ТРАНСПОРТ*\n")
        print("Марка:", self.mark, "\nКоординаты:", self.coords_to_str())

    def Coord_func(self, coord_list):
        y_list, x_list = coord_list
        y1, y2 = y_list
        x1, x2 = x_list

        locale_x, locale_y = self.coordinate

        if x1 <= locale_x <= x2 and y1 <= locale_y <= y2:
            return True
        return False

    def coords_to_str(self):
        x, y = self.coordinate
        return "["+str(x)+", "+str(y)+"]"


class Airplane(Transport):
    """САМОЛЕТ (марка, максимальные скорость и высота, количество пассажиров, координаты)"""

    def __init__(self, mark, coordinate, persons, speed, height):
        super().__init__(mark, coordinate)
        self.height = height
        self.speed = speed
        self.persons = persons

    def info(self):
        print("\n*Class САМОЛЕТ*\n")
        print("Марка:", self.mark, "\nСкорость:", self.speed, "\nВысота:", self.height, "\nКоординаты:",
              self.coords_to_str(), "\nКоличество пассажиров:", self.persons)


class Car(Transport):
    """АВТОМОБИЛЬ (марка, номер, год выпуска, координаты)"""

    def __init__(self, mark, coordinate, num, year_release):
        self.mark = mark
        self.num = num
        self.year_release = year_release
        self.coordinate = coordinate

    def info(self):
        print("\n*Class АВТОМОБИЛЬ*\n")
        print("Марка: ", self.mark, "\nНомер: ", self.num, "\nГод выпуска: ", self.year_release,
              "\nКоординаты:", self.coords_to_str())


class Ship(Transport):
    """КОРАБЛЬ (название, координаты, скорость, количество пассажиров, порт приписки)"""

    def __init__(self, mark, coordinate, persons, speed, port):
        super().__init__(mark, coordinate)
        self.port = port
        self.speed = speed
        self.persons = persons

    def info(self):
        print("\n*Class КОРАБЛЬ*\n")
        print("Название: ", self.mark, "\nКоординаты", self.coords_to_str(), "\nСкорость: ", self.speed,
              "\nКоличество пассажиров: ", self.persons, "\nПорт приписки: ", self.port)


def main():
    fake = Faker(['ru_RU'])
    """
    Создайте список из п транспортных средств, выведите полную информацию из базы на экран,
    а также организуйте поиск транспортных средств, которые сейчас находятся в пределах заданных координат.
    """
    try:
        n = int(input("Кол-во транспортных средств = "))

    except ValueError:
        print("Упс..")
        return

    d = {
        1: Transport,
        2: Airplane,
        3: Car,
        4: Ship
    }

    transport_list = []
    for _ in range(n):

        r_int = randint(1, 4)

        d_args = {
            1: (fake.word(), [randint(1, 100), randint(1, 100)]),
            2: (fake.word(), [randint(1, 100), randint(1, 100)], randint(1, 1000), randint(50, 300), randint(1000, 6000)),
            3: (fake.word(), [randint(1, 100), randint(1, 100)], randint(1, 1000), randint(1960, 2020)),
            4: (fake.word(), [randint(1, 100), randint(1, 100)], randint(1, 1000), randint(50, 300), fake.word()),
        }

        transport_list.append(d[r_int](*d_args[r_int]))

    for transport in transport_list:
        transport.info()

    find = False
    try:
        x1_input = int(input("Введите координату x1 -> "))
        y1_input = int(input("Ввдетие координату y1 -> "))

        x2_input = int(input("Введите координату x2 -> "))
        y2_input = int(input("Ввдетие координату y2 -> "))

        if x1_input < x2_input:
            x2_input, x1_input = x1_input, x2_input

        if y1_input < y2_input:
            y2_input, y1_input = y1_input, y2_input

    except ValueError:
        print("Упс..")
        return

    l = ([x1_input, y1_input], [x2_input, y2_input])
    print("\n*Транспорт, который вам доступен*")
    for transport in transport_list:
        if transport.Coord_func(l):
            transport.info()
            find = True

    if not find:
        print("Транспорт не найден")


if __name__ == "__main__":
    main()
