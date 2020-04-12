from classGoods import Goods
class Product(Goods):
    def __init__(self, name, price, manufacture_date, expiration_date):
        super().__init__(name, price, manufacture_date, expiration_date)

    def info(self):
        print("\n*Class ПРОДУКТЫ*\n")
        print("Название товара:", self.name, "\nЦена:", self.price,
              "\nДата производства:", self.manufacture_date,
              "\nСрок годности:", self.expiration_date)