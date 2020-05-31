"""
Task 7. 
Создайте класс ТЕЛЕФОННЫЙ СПРАВОЧНИК с методами,
позволяющими вывести на экран информацию о записях в телефонном справочнике,
а также определить соответствие записи критерию поиска.
Создайте дочерние классы ПЕРСОНА (фамилия, адрес, номер телефона),
ОРГАНИЗАЦИЯ (название, адрес, телефон, факс, контактное лицо),
ДРУГ (фамилия, адрес, номер телефона, дата рождения)
со своими методами вывода информации на экран и определения соответствия заданной фамилии.
Создайте список из n записей, выведите полную информацию из базы на экран,
 а также организуйте поиск в базе по фамилии.
"""
from faker import Faker
from random import randint


class PhoneDict:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def pers_search(self, input_name):
        if input_name in self.name:
            return True
        return False

    def info(self):
        print("\n*class ТЕЛЕФОННЫЙ СПРАВОЧНИК*\n")
        print("Имя:", self.name, "\nАдрес:", self.address,
              "\nТелефон:", self.phone_number)


class Person(PhoneDict):
    def __init__(self, name, address, phone_number):
        super().__init__(name, address, phone_number)

    def info(self):
        print("\n*class ПЕРСОНА*\n")
        print("Имя:", self.name, "\nАдрес:", self.address,
              "\nТелефон:", self.phone_number)


class Organization(PhoneDict):
    def __init__(self, name, address, phone_number, fax, contact_person):
        super().__init__(name, address, phone_number)
        self.fax = fax
        self.contact_person = contact_person

    def info(self):
        print("\n*class ОРГАНИЗАЦИЯ*\n")
        print("Имя:", self.name, "\nАдрес:", self.address, "\nТелефон:", self.phone_number,
              "\nФакс:", self.fax, "\nКонтактное лицо:", self.contact_person)


class Friend(PhoneDict):
    def __init__(self, name, address, phone_number, birthday):
        super().__init__(name, address, phone_number)
        self.birthday = birthday

    def info(self):
        print("\n*class ДРУГ*\n")
        print("Имя:", self.name, "\nАдрес:", self.address, "\nТелефон:", self.phone_number,
              "\nДата рождения:", self.birthday)


def main():
    fake = Faker(['ru_RU'])
    persons_list = []
    try:
        n = int(input("Количество записей = "))
    except ValueError:
        print("Упс....")
        return
    d = {
        1: PhoneDict,
        2: Person,
        3: Organization,
        4: Friend
    }
    for _ in range(n):
        r = randint(1, 4)
        d_val = {
            1: (fake.name(), fake.address(), fake.phone_number()),
            2: (fake.name(), fake.address(), fake.phone_number()),
            3: (fake.word(), fake.address(), fake.phone_number(), fake.phone_number(), fake.name()),
            4: (fake.name(), fake.address(), fake.phone_number(), fake.date(pattern='%d.%m.%Y')),
        }

        persons_list.append(d[r](*d_val[r]))

    for pers in persons_list:
        pers.info()

    try:
        input_name = input("Введите фамилию, чтобы найти персону: ")
    except ValueError:
        print("Упс....")
        return
    print("\n*Персоны:*")
    find = False
    for pers in persons_list:
        if pers.pers_search(input_name):
            find = True
            pers.info()

    if not find:
        print("*Персоны не найдены*")


if __name__ == "__main__":
    main()
