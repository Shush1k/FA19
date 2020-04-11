import classGoods
class Party(classGoods.Goods):
    def __init__(self, name, price, manufacture_date, expiration_date, units):
        super().__init__(name, price, manufacture_date, expiration_date)
        self.units = str(units)

    def info(self):
        print("\n*Class ЕДИНАЯ ПАРТИЯ РОССИИ*\n")
        print("Название товара:", self.name, "\nЦена:", self.price,
              "\nДата производства:", self.manufacture_date,
              "\nСрок годности:", self.expiration_date, "\nКоличество:", self.units)