from random import randint

"""
Задача 14. Создайте класс ВАЛЮТА с методами перевода денежной суммы в рубли и вывода на экран.
Создайте дочерние классы ДОЛЛАР, ЕВРО со своими методами перевода и вывода на экран.
Создайте список п валютных денежных сумм и выведите полную информацию о них на экран.
"""


class Currency:
    # Покупка
    cur_eur = 85
    cur_dollar = 75
    # Продажа
    sell_eur = 80
    sell_dollar = 70

    def __init__(self, user_money, trade):
        self.user_money = user_money
        self.trade = trade

    def info(self, choice):
        print("\n*Class ВАЛЮТА*")
        print("Количество рублей:", self.user_money,
              "\nКурс обмена", self.trade)

    def transfer(self):
        # Рубли
        return self.trade * self.user_money

    def transfer_back(self):
        # Из рублей в валюту
        return self.user_money / self.trade


class Euro(Currency):

    def __init__(self, user_money, choice):
        if choice == "1":
            self.trade = super().cur_eur
        elif choice == "2":
            self.trade = super().sell_eur
        self.user_money = user_money

    def info(self, choice):
        print("\n*class ЕВРО*\n")
        if choice == "2":
            print("Количество евро у вас:", self.user_money,
                  "\nКурс обмена", self.trade)
            print("Сконвертированная валюта(RUB):", self.transfer())
        elif choice == "1":
            print("Количество рублей у вас:", self.user_money,
                  "\nКурс обмена", self.trade)
            print("Сконвертированная валюта(Euro):",
                  round(self.transfer_back(), 2))
        else:
            print("Некорректный ввод данных")


class Dollar(Currency):

    def __init__(self, user_money, choice):
        self.user_money = user_money
        if choice == "1":
            self.trade = super().cur_dollar
        elif choice == "2":
            self.trade = super().sell_dollar

    def info(self, choice):
        print("\n*class ДОЛЛАР*\n")
        if choice == "2":
            print("Количество долларов у вас:",
                  self.user_money, "\nКурс обмена", self.trade)
            print("Сконвертированная валюта(RUB):", self.transfer())
        elif choice == "1":
            print("Количество рублей у вас:", self.user_money,
                  "\nКурс обмена", self.trade)
            print("Сконвертированная валюта(DOL):",
                  round(self.transfer_back(), 2))
        else:
            print("Некорректный ввод данных")


def main():
    try:
        choice = input("1)Купить\n2)Продать\nВыбор:")
        curr_choice = int(input("1)Евро\n2)Доллары\nВыбор:"))
        if curr_choice != 1 and curr_choice != 2:
            raise KeyError
        pers_money = float(input("Ваше количество денег:"))
        n = 1
        #n = int(input("Кол-во валютных денежных сумм: "))
    except ValueError:
        print("Некорректный ввод данных")
    except KeyError:
        print("Некорректный ввод данных")
        return

    d = {
        1: Euro,
        2: Dollar
    }
    currency_list = [d[curr_choice](pers_money, choice) for _ in range(n)]

    # random choice
    #currency_list = [d[curr_choice](randint(1, 1000), choice) for _ in range(n)]

    for curr in currency_list:
        curr.info(choice)


if __name__ == "__main__":
    main()
