class Goods:
    def __init__(self, name, price, manufacture_date, expiration_date):
        self.name = str(name).title()
        self.price = str(price)
        self.manufacture_date = str(manufacture_date)
        self.expiration_date = str(expiration_date)

    def info(self):
        print("\n*Class ТОВАРЫ*\n")
        print("Название товара:", self.name, "\nЦена:", self.price,
              "\nДата производства:", self.manufacture_date,
              "\nСрок годности:", self.expiration_date)

    def SUBJ(self, user_money):
        if user_money >= int(self.price):
            return True
        return False