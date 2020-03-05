from faker import Faker
from random import randint

"""
Создайте класс ТОВАР с методами, позволяющими вывести на экран информацию о товаре,
а также определить, может ли приобрести товар покупатель, имеющий заданную сумму денег.
Создайте дочерние классы
ПРОДУКТ (название, цена, дата производства, срок годности),
ПАРТИЯ (название, цена, дата производства, срок годности, количество штук),
ТЕЛЕФОН (название, цена) со своими методами вывода информации на экран и определения соответствия заданной цене.
Создайте список из п товаров, выведите полную информацию из базы на экран,
а также организуйте поиск товара, который может приобрести покупатель, имеющий заданную сумму денег.
"""


class Goods:
    def __init__(self, name, price, manufacture_date, expiration_date):
        self.name = str(name).title()
        self.price = str(price)
        self.manufacture_date = str(manufacture_date)
        self.expiration_date = str(expiration_date)

    def info(self):
        print("\n*Class ТОВАРЫ*\n")
        print("Название товара:", self.name, "\nЦена:", self.price,
              "\nДата производства:", self.manufacture_date,
              "\nСрок годности:", self.expiration_date)

    def SUBJ(self, user_money):
        if user_money >= int(self.price):
            return True
        return False


class Product(Goods):
    """Very strange class"""

    def __init__(self, name, price, manufacture_date, expiration_date):
        super().__init__(name, price, manufacture_date, expiration_date)

    def info(self):
        print("\n*Class ПРОДУКТЫ*\n")
        print("Название товара:", self.name, "\nЦена:", self.price,
              "\nДата производства:", self.manufacture_date,
              "\nСрок годности:", self.expiration_date)


class Party(Goods):
    def __init__(self, name, price, manufacture_date, expiration_date, units):
        super().__init__(name, price, manufacture_date, expiration_date)
        self.units = str(units)

    def info(self):
        print("\n*Class ЕДИНАЯ ПАРТИЯ РОССИИ*\n")
        print("Название товара:", self.name, "\nЦена:", self.price,
              "\nДата производства:", self.manufacture_date,
              "\nСрок годности:", self.expiration_date, "\nКоличество:", self.units)


class Phone(Goods):
    def __init__(self, name, price):
        self.name = name.title()
        self.price = price
        # super().__init__(name, price, _, _)  работает в Jupyter но на VS code отказывается

    def info(self):
        print("\n*Class ТЕЛЕФОН*\n")
        print("Название мобилы:", self.name, "\nЦена:", self.price)


def main():

    fake = Faker(["ru_RU"])
    d = {
        1: Goods,
        2: Product,
        3: Party,
        4: Phone
    }

    try:
        n = int(input("Количество товаров = "))
    except ValueError:
        print("0_0 упс...")
        return
    all_obj = []
    for _ in range(n):
        r = randint(1, 4)
        data1 = fake.date(pattern="%d.%m.%Y")
        data2 = fake.date(pattern="%d.%m.%Y")
        d_val = {
            1: (fake.word(), randint(1, 100000), data1, data2),
            2: (fake.word(), randint(1, 100000), data1, data2),
            3: (fake.word(), randint(1, 100000), data1, data2, randint(1, 100000)),
            4: (fake.word(), randint(1, 100000))
        }

        all_obj.append(d[r](*d_val[r]))

    for obj in all_obj:
        obj.info()

    try:
        user_money = float(input("Кол-во денег пользователя = "))
    except ValueError:
        print("0_0 упс...")
        return

    find = False
    print("Вам хватает денег на эти товары:")
    for obj in all_obj:
        if obj.SUBJ(user_money) == True:
            obj.info()
            find = True
    if find == False:
        print("*Товары не найдены*")


if __name__ == "__main__":
    main()
