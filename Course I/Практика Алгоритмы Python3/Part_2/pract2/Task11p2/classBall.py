import classToy
class Ball(classToy.Toy):
    def __init__(self, color, price, material, diametr):
        super().__init__(color, price, material)
        self.diametr = diametr

    def info(self):
        print("\n*Class МЯЧ*\n")
        print("Цвет:", self.color, "\nЦена:", self.price, "\nМатериал:",
              self.material, "\nДиаметр:", self.diametr)
class BabyCar(classToy.Toy):
    def __init__(self, name, price, manufacturer, color):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.color = color

    def info(self):
        print("\n*Class МАШИНКА*\n")
        print("Название:", self.name, "\nЦена:", self.price,
              "\nПроизводитель:", self.manufacturer, "\nЦвет:", self.color)