"""
Задача 8. Создайте класс КЛИЕНТ с методами,
позволяющими вывести на экран информацию о клиентах банка,
а также определить соответствие клиента критерию поиска.
Создайте дочерние классы ВКЛАДЧИК (фамилия, дата открытия вклада, размер вклада, процент по вкладу),
КРЕДИТОР (фамилия, дата выдачи кредита, размер кредита, процент по кредиту, остаток долга),
ОРГАНИЗАЦИЯ (название, дата открытия счета, номер счета, сумма на счету)
со своими методами вывода информации на экран и определения соответствия дате 
(открытия вклада, выдаче кредита, открытия счета).
Создайте список из п клиентов, выведите полную информацию из базы на экран,
а также организуйте поиск клиентов, начавших сотрудничать с банком в заданную дату.
"""
from faker import Faker
from random import randint


class Client:
    def __init__(self, surname, date, size, percent):
        self.surname = surname
        self.date = date
        self.size = size
        self.percent = percent

    def info(self):
        print("\n*Class КЛИЕНТ*")
        print("Фамилия:", self.surname, "\nДата открытия вклада:", self.date,
              "\nРазмер вклада:", self.size, "\nПроцент по вкладу:", self.percent)

    def client_date(self, user_date):
        if user_date == str(self.date):
            return True
        return False


class Investor(Client):
    """
    ВКЛАДЧИК 
    1)фамилия
    2)дата открытия вклада
    3)размер вклада
    4)процент по вкладу
    """

    def __init__(self, surname, date, size, percent):
        super().__init__(surname, date, size, percent)

    def info(self):
        print("\n*Class ВКЛАДЧИК*")
        print("Фамилия:", self.surname, "\nДата открытия вклада:", self.date,
              "\nРазмер вклада:", self.size, "\nПроцент по вкладу:", self.percent)


class Creditor(Client):
    """
    КРЕДИТОР 
    1)фамилия
    2)дата выдачи кредита
    3)размер кредита
    4)процент по кредиту
    5)остаток долга)
    """

    def __init__(self, surname, date, size, percent, debt):
        super().__init__(surname, date, size, percent)
        self.debt = debt

    def info(self):
        print("\n*Class КРЕДИТОР*")
        print("Фамилия:", self.surname, "\nДата открытия вклада:", self.date,
              "\nРазмер вклада:", self.size, "\nПроцент по вкладу:", self.percent,
              "\nОстаток долга:", self.debt)


class Organization(Client):
    """
    ОРГАНИЗАЦИЯ 
    1)название
    2)дата открытия счета
    3)номер счета 
    4)сумма на счету
    """

    def __init__(self, surname, date, size, percent):
        super().__init__(surname, date, size, percent)

    def info(self):
        print("\n*Class ОРГАНИЗАЦИЯ*")
        print("Название:", self.surname, "\nДата открытия счета:", self.date,
              "\nНомер счета", self.size, "\nСумма на счету:", self.percent)


def main():
    fake = Faker("ru_Ru")
    try:
        n = int(input("Количество клиентов = "))
    except ValueError:
        print("0_0 упс...")
        return

    client_list = []
    d = {
        1: Client,
        2: Investor,
        3: Creditor,
        4: Organization
    }
    for _ in range(n):
        r = randint(1, 4)

        surname = fake.name().split(" ", 1)[0]
        d_val = {
            1: (surname, fake.date(pattern='%d.%m.%Y'), randint(1000, 100000), randint(1, 20)),
            2: (surname, fake.date(pattern='%d.%m.%Y'), randint(1000, 100000), randint(1, 20)),
            3: (surname, fake.date(pattern='%d.%m.%Y'), randint(1000, 100000), randint(1, 20), randint(1000, 20000)),
            4: (fake.word(), fake.date(pattern='%d.%m.%Y'), randint(1, 500), randint(5000, 1400000))
        }

        client_list.append(d[r](*d_val[r]))

    for client in client_list:
        client.info()
    try:
        print("\nПример: 20.02.2020")
        user_date = input("Введите дату, чтобы найти клиента: ")
    except ValueError:
        print("0_0 упс...")
        return

    find = False
    print("\n*Клиенты, которые начали сотрудничать с банком в заданную дату*")
    for client in client_list:
        if client.client_date(user_date) == True:
            client.info()
            find = True
    if not find:
        print("*Клиенты не найдены*")


if __name__ == "__main__":
    main()
