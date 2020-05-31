"""
Task 6.
Создайте класс ТОВАР с методами, позволяющими вывести на экран
информацию о товаре, а также определить, предназначен ли он для заданного возраста потребителя.
Создайте дочерние классы ИГРУШКА (название, цена, производитель, возраст, на который рассчитана, материал),
КНИГА (название, цена, издательство, возраст, на который рассчитана, автор),
СПОРТИНВЕНТАРЬ (название, цена, производитель, возраст, на который рассчитан)
со своими методами вывода информации на экран и определения соответствия возрасту потребителя.
Создайте список из n товаров, выведите полную информацию из базы на экран,
а также организуйте поиск товаров для потребителя в заданном возрастном диапазоне.
"""

from faker import Faker
from random import randint, choice


class Goods:
    def __init__(self, name, price, manufacturer, age):
        self.name = str(name)
        self.price = str(price)
        self.manufacturer = str(manufacturer)
        self.age = str(age)

    def info(self):
        print("\n*Class ТОВАРЫ*\n")
        print("Название: "+self.name+"\nЦена: "+str(self.price) +
              "\nПроизводитель: "+self.manufacturer+"\nОграничение по возрасту: "+str(self.age))

    def user_age(self, age_input):
        if age_input >= int(self.age):
            return True
        return False


class Toy(Goods):
    def __init__(self, name, price, manufacturer, age, material):
        super().__init__(name, price, manufacturer, age)
        self.material = str(material)

    def info(self):
        print("\n*Class ИГРУШКА*\n")
        print("Название: "+self.name+"\nЦена: "+str(self.price)+"\nПроизводитель: " +
              self.manufacturer+"\nОграничение по возрасту: "+str(self.age)+"\nМатериал: "+self.material)


class Book(Goods):
    def __init__(self, name, price, manufacturer, age, author):
        super().__init__(name, price, manufacturer, age)
        self.author = str(author)

    def info(self):
        print("\n*Class КНИГА*\n")
        print("Название: "+self.name+"\nЦена: "+str(self.price)+"\nИздательство: " +
              self.manufacturer+"\nОграничение по возрасту: "+str(self.age)+"\nАвтор: "+self.author)


class SportStock(Goods):
    def __init__(self, name, price, manufacturer, age):
        super().__init__(name, price, manufacturer, age)

    def info(self):
        print("\n*Class СПОРТИНВЕНТАРЬ*\n")
        print("Название: "+self.name+"\nЦена: "+str(self.price)+"\nПроизводитель: " +
              self.manufacturer+"\nОграничение по возрасту: "+str(self.age))


def main():
    fake = Faker(['ru_RU'])
    try:
        n = int(input("Количество товара = "))
    except ValueError:
        print("0_0 упс...")
        return

    d = {
        1: Goods,
        2: Toy,
        3: Book,
        4: SportStock
    }

    goods_list = []
    for _ in range(n):
        materials = ["дерево", "пластик", "хлопок", "металл"]
        k = randint(1, 4)

        d_val = {

            1: (fake.word(), randint(1, 10000), fake.word(), randint(1, 18)),
            2: (fake.word(), randint(1, 5000), fake.word(), randint(3, 12), choice(materials)),
            3: (fake.word(), randint(1, 10000), fake.word(), randint(1, 18), fake.name()),
            4: (fake.word(), randint(1, 100000), fake.word(), randint(6, 18))
        }

        goods_list.append(d[k](*d_val[k]))

    for goods in goods_list:
        goods.info()

    try:
        age_input = int(input("\nСколько вам лет? \
        \nВы же не собираетесь обманывать машину?\nВам "))

    except ValueError:
        print("0_0 упс...")
        return

    find = False
    print("\n*Товары, которые вы можете купить*")
    for goods in goods_list:
        if goods.user_age(age_input) == True:
            goods.info()
            find = True

    if not find:
        print("*Товары не найдены*")


if __name__ == "__main__":
    main()
