"""
Задача  11. Создайте класс ИГРУШКА с методами, позволяющими вывести на экран информацию о товаре,
а также определить соответствие игрушки критерию поиска.
Создайте дочерние классы КУБИК (цвет, цена, материал, размер ребра),
МЯЧ (цена, цвет, диаметр, материал),
МАШИНКА (название, цена, производитель, цвет) со своими методами вывода информации на экран и 
определения соответствия заданному цвету.
Создайте список из п игрушек, выведите полную информацию из базы на экран,
а также организуйте поиск игрушек заданного цвета.
"""
from random import randint, choice
from faker import Faker


class Toy:
    def __init__(self, color, price, material):
        self.color = color
        self.price = price
        self.material = material

    def info(self):
        print("\n*Class ИГРУШКА*\n")
        print("Цвет:", self.color, "\nЦена:",
              self.price, "\nМатериал:", self.material)

    def toy_color(self, user_color):
        if user_color == self.color:
            return True
        return False


class Cube(Toy):
    """КУБИК (цвет, цена, материал, размер ребра)"""

    def __init__(self, color, price, material, rib_size):
        super().__init__(color, price, material)
        self.rib_size = rib_size

    def info(self):
        print("\n*Class КУБИК*\n")
        print("Цвет:", self.color, "\nЦена:", self.price, "\nМатериал:",
              self.material, "\nРазмер ребра:", self.rib_size)


class Ball(Toy):
    """МЯЧ (цена, цвет, диаметр, материал)"""

    def __init__(self, color, price, material, diametr):
        super().__init__(color, price, material)
        self.diametr = diametr

    def info(self):
        print("\n*Class МЯЧ*\n")
        print("Цвет:", self.color, "\nЦена:", self.price, "\nМатериал:",
              self.material, "\nДиаметр:", self.diametr)


class BabyCar(Toy):
    """МАШИНКА (название, цена, производитель, цвет)"""

    def __init__(self, name, price, manufacturer, color):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.color = color

    def info(self):
        print("\n*Class МАШИНКА*\n")
        print("Название:", self.name, "\nЦена:", self.price,
              "\nПроизводитель:", self.manufacturer, "\nЦвет:", self.color)


def main():
    fake = Faker(['ru_RU'])
    try:
        n = int(input("Количество товара = "))
    except ValueError:
        print("0_0 упс...")
        return

    d = {
        1: Toy,
        2: Cube,
        3: Ball,
        4: BabyCar
    }

    toy_list = []
    for _ in range(n):
        materials = ["дерево", "пластик", "хлопок", "металл"]
        k = randint(1, 4)

        d_val = {

            1: (fake.color_name(), randint(1, 10000), choice(materials)),
            # кубик из хлопка бывает, я гуглил :D
            2: (fake.color_name(), randint(1, 5000), choice(materials), randint(3, 12)),
            3: (randint(1, 5000), fake.color_name(), randint(1, 18), choice(materials)),
            4: (fake.word(), randint(1, 10000), fake.word(), fake.color_name())
        }

        toy_list.append(d[k](*d_val[k]))

    for toy in toy_list:
        toy.info()

    try:
        user_color = str(input("\nВведите цвет!\nВаш цвет: "))

    except ValueError:
        print("0_0 упс...")
        return

    find = False
    print("\n*Игрушки с заданным цветом*")
    for toy in toy_list:
        if toy.toy_color(user_color) == True:
            toy.info()
            find = True

    if not find:
        print("*Товары не найдены*")


if __name__ == "__main__":
    main()
