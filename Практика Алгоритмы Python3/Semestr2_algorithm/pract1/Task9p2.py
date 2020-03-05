"""
Задача  9. Создайте класс ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ с методами, 
позволяющими вывести на экран информацию о программном обеспечении,
а также определить соответствие возможности использования (на текущую дату).
Создайте дочерние классы СВОБОДНОЕ (название, производитель),
УСЛОВНО БЕСПЛАТНОЕ (название, производитель, дата установки, срок бесплатного использования),
КОММЕРЧЕСКОЕ (название, производитель, цена, дата установки, срок использования) 
со своими методами вывода информации на экран и определения возможности использования на текущую дату.
Создайте список из п видов программного обеспечения, выведите полную информацию из базы на экран,
а также организуйте поиск программного обеспечения, которое допустимо использовать на текущую дату.
"""
from datetime import datetime, timedelta
from random import randint
from faker import Faker


class ProgramSoftware:
    def __init__(self, name, manufacturer, date):
        self.name = name
        self.manufacturer = manufacturer
        self.date = str(date)

    def info(self):
        print("\n*Class ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ*\n")
        print("Название ПО:", self.name, "\nПроизводитель:", self.manufacturer,
              "\nДата установки:", self.date)

    def date_PO(self, user_date):
        """Можно было использовать pattern = '%Y.%m.%d', но я захотел так"""
        # print(fake.date(pattern='%Y.%m.%d'))
        date = self.date
        new_date = ".".join(date.split("-"))

        d1 = datetime.strptime(user_date, "%d.%m.%Y")
        d2 = datetime.strptime(new_date, "%Y.%m.%d")
        if d1 >= d2:
            return False
        return True


class Free(ProgramSoftware):
    def __init__(self, name, manufacturer, date):
        super().__init__(name, manufacturer, date)

    def info(self):
        print("\n*Class СВОБОДНОЕ*\n")
        print("Название ПО:", self.name, "\nПроизводитель:", self.manufacturer,
              "\nДата установки:", self.date)


class Shareware(ProgramSoftware):
    def __init__(self, name, manufacturer, date, free_period):
        super().__init__(name, manufacturer, date)
        self.free_period = free_period

    def info(self):
        print("\n*Class УСЛОВНО БЕСПЛАТНОЕ*\n")
        print("Название ПО:", self.name, "\nПроизводитель:", self.manufacturer,
              "\nДата установки:", self.date, "\nСрок бесплатного использования:", self.free_period)


class Commercial(ProgramSoftware):
    def __init__(self, name, manufacturer, price, date, use_period):
        super().__init__(name, manufacturer, date)
        self.price = price
        self.use_period = use_period

    def info(self):
        print("\n*Class КОММЕРЧЕСКОЕ*\n")
        print("Название ПО:", self.name, "\nПроизводитель:", self.manufacturer, "\nЦена:", self.price,
              "\nДата установки:", self.date, "\nСрок использования:", self.use_period)


def main():
    fake = Faker(['ru_RU'])
    try:
        n = int(input("Количество видов ПО = "))
    except ValueError:
        print("0_0 упс...")
        return

    d = {
        1: ProgramSoftware,
        2: Free,
        3: Shareware,
        4: Commercial
    }

    prog_list = []
    for _ in range(n):
        r = randint(1, 4)

        d_val = {

            1: (fake.word(), fake.name(), fake.date()),
            2: (fake.word(), fake.name(), fake.date()),
            3: (fake.word(), fake.name(), fake.date(), fake.date()),
            4: (fake.word(), fake.name(), randint(500, 50000), fake.date(), fake.date())
        }

        prog_list.append(d[r](*d_val[r]))

    for prog in prog_list:
        prog.info()

    try:
        print("\nПример: 20.02.2020")
        user_data = str(input("Введите дату:"))

    except ValueError:
        print("0_0 упс...")
        return

    find = False
    print("\n*ПО, которое вам доступно*")
    for prog in prog_list:
        if prog.date_PO(user_data) == True:
            prog.info()
            find = True

    if not find:
        print("*Товары не найдены*")


if __name__ == "__main__":
    main()
