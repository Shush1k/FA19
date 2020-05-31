class Toy:
    def __init__(self, color, price, material):
        self.color = color
        self.price = price
        self.material = material

    def info(self):
        print("\n*Class ИГРУШКА*\n")
        print("Цвет:", self.color, "\nЦена:",
              self.price, "\nМатериал:", self.material)

    def toy_color(self, user_color):
        if user_color == self.color:
            return True
        return False
class Cube(Toy):
    def __init__(self, color, price, material, rib_size):
        super().__init__(color, price, material)
        self.rib_size = rib_size

    def info(self):
        print("\n*Class КУБИК*\n")
        print("Цвет:", self.color, "\nЦена:", self.price, "\nМатериал:",
              self.material, "\nРазмер ребра:", self.rib_size)