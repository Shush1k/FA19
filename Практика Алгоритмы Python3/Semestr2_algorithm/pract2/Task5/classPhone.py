import classGoods
class Phone(classGoods.Goods):
    def __init__(self, name, price):
        self.name = name.title()
        self.price = price

    def info(self):
        print("\n*Class ТЕЛЕФОН*\n")
        print("Название мобилы:", self.name, "\nЦена:", self.price)