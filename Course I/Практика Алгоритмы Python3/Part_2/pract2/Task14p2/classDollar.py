import classCurency
class Dollar(classCurency.Currency):

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