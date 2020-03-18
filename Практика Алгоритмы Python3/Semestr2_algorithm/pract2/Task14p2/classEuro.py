import classCurency
class Euro(classCurency.Currency):

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