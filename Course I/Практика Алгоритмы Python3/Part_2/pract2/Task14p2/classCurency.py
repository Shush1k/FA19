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