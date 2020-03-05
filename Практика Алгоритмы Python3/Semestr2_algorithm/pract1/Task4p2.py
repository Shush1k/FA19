from random import randint
"""
Создайте класс ТРАНСПОРТ с методами, позволяющими вывести на экран информацию о 
транспортном средстве, а также определить грузоподъемность транспортного средства.
Создайте дочерние классы АВТОМОБИЛЬ (марка, номер, скорость, грузоподъемность),
МОТОЦИКЛ (марка, номер, скорость, грузоподъемность, наличие коляски,
при этом если коляска отсутствует, то грузоподъемность равна нулю),
ГРУЗОВИК (марка, номер, скорость, грузоподъемность, наличие прицепа,
при этом если есть прицеп, то грузоподъемность увеличивается в два раза)
со своими методами вывода информации на экран и определения грузоподъемности.
Создайте список из n машин, выведите полную информацию на экран, а также организуйте поиск машин, удовлетворяющих требованиям грузоподъемности.

"""


class Transport:
    def __init__(self, mark, num, speed, carrying):
        self.mark = str(mark)
        self.num = str(num)
        self.speed = speed
        self.carrying = carrying

    def info(self):
        print("\n*Class Transport*\n")
        print("Марка:", self.mark, "\nНомер:", self.num, "\nСкорость:",
              str(self.speed), "\nГрузоподъемность:", str(self.carrying))

    def carry_digit(self):
        return self.carrying


class Car(Transport):
    def __init__(self, mark, num, speed, carrying):
        super().__init__(mark, num, speed, carrying)

    def info(self):
        print("\n*Class Automobilius*\n")
        print("Марка: ", self.mark, "\nНомер: ", self.num, "\nСкорость: ",
              str(self.speed), "\nГрузоподъёмность: ", str(self.carrying))


class Motorcycle(Transport):
    def __init__(self, mark, num, speed, carrying, trailer):
        super().__init__(mark, num, speed, carrying)
        self.trailer = trailer
        self.have_trailer = {
            True: "Да",
            False: "Нет"
        }
        self.Motorcycle_carrying()

    def Motorcycle_carrying(self):
        if self.trailer == False:
            self.carrying = 0

    def info(self):
        print("\n*Class Motorcycle*\n")
        print("Марка: ", self.mark, "\nНомер: ", self.num, "\nСкорость: ", str(self.speed),
              "\nГрузоподъёмность: ", str(self.carrying), "\nНаличие коляски: ", self.have_trailer[self.trailer])


class Truck(Transport):
    def __init__(self, mark, num, speed, carrying, trailer):
        super().__init__(mark, num, speed, carrying)
        self.trailer = trailer
        self.have_trailer = {
            True: "Да",
            False: "Нет"
        }
        self.Truck_carrying()

    def Truck_carrying(self):
        if self.trailer == True:
            self.carrying *= 2

    def info(self):
        print("\n*Class Truck*\n")
        print("Марка: ", self.mark, "\nНомер: ", self.num, "\nСкорость: ", str(self.speed),
              "\nГрузоподъёмность: ", str(self.carrying), "\nНаличие прицепа: ", self.have_trailer[self.trailer])


def main():
    try:
        n = int(input("Введите количество транспорта: "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1: Transport,
        2: Car,
        3: Motorcycle,
        4: Truck
    }

    transport_list = []

    for _ in range(n):
        r = randint(1, 4)
        d_val = {
            1: (randint(1, 100), randint(1, 1000), randint(60, 300), randint(500, 10000)),
            2: (randint(1, 100), randint(1, 1000), randint(60, 300), randint(500, 10000)),
            3: (randint(1, 100), randint(1, 1000), randint(60, 300), randint(500, 10000), bool(randint(0, 1))),
            4: (randint(1, 100), randint(1, 1000), randint(60, 300), randint(500, 10000), bool(randint(0, 1))),
        }

        transport_list.append(d[r](*d_val[r]))

    for transport in transport_list:
        transport.info()

    # Организуйте поиск машин, удовлетворяющих требованиям грузоподъемности.

    try:
        carrying_input = float(input("\nГрузоподъёмность = "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    print("\n*Транспорт, грузоподъёмность которого меньше или равна заданной*")
    find = False
    for transport in transport_list:

        if transport.carry_digit() <= carrying_input:
            transport.info()
            find = True

    if find == False:
        print("Транспорт не найден")


if __name__ == "__main__":
    main()
