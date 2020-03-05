from random import randint

"""
Задача 14. Создайте класс ВАЛЮТА с методами перевода денежной суммы в рубли и вывода на экран.
Создайте дочерние классы ДОЛЛАР, ЕВРО со своими методами перевода и вывода на экран.
Создайте список п валютных денежных сумм и выведите полную информацию о них на экран.
"""


class Currency:
    cur_eur = 70
    cur_dollar = 65

    def __init__(self, user_money, trade):
        self.user_money = user_money
        self.trade = trade

    def info(self):
        print("\n*Class ВАЛЮТА*")
        print("Количество рублей:", self.user_money, "\nКурс обмена",
              self.trade, "\nСконвертированная валюта:", self.transfer())

    def transfer(self):
        return self.trade * self.user_money


class Euro(Currency):

    def __init__(self, user_money):
        self.trade = super().cur_eur
        self.user_money = user_money

    def transfer(self):
        return self.user_money * self.trade

    def info(self):
        print("\n*class ЕВРО*\n")
        print("Количество Euro:", self.user_money, "\nКурс обмена",
              self.trade, "\nСконвертированная валюта в RUB:", self.transfer())


class Dollar(Currency):

    def __init__(self, user_money):
        self.trade = super().cur_dollar
        self.user_money = user_money

    def transfer(self):
        return self.user_money * self.trade

    def info(self):
        print("\n*class ДОЛЛАР*\n")
        print("Количество Dollars:", self.user_money, "\nКурс обмена",
              self.trade, "\nСконвертированная валюта в RUB:", self.transfer())


def main():
    try:
        n = int(input("Кол-во валютных денежных сумм:"))
    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1: Euro,
        2: Dollar
    }
    currency_list = [d[randint(1, 2)](randint(1, 1000)) for _ in range(n)]

    for curr in currency_list:
        curr.info()


if __name__ == "__main__":
    main()
