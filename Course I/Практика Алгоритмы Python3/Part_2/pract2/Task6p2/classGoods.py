class Goods:
    def __init__(self, name, price, manufacturer, age):
        self.name = str(name)
        self.price = str(price)
        self.manufacturer = str(manufacturer)
        self.age = str(age)

    def info(self):
        print("\n*Class ТОВАРЫ*\n")
        print("Название: "+self.name+"\nЦена: "+str(self.price) +
              "\nПроизводитель: "+self.manufacturer+"\nОграничение по возрасту: "+str(self.age))

    def user_age(self, age_input):
        if age_input >= int(self.age):
            return True
        return False
class SportStock(Goods):
    def __init__(self, name, price, manufacturer, age):
        super().__init__(name, price, manufacturer, age)

    def info(self):
        print("\n*Class СПОРТИНВЕНТАРЬ*\n")
        print("Название: "+self.name+"\nЦена: "+str(self.price)+"\nПроизводитель: " +
              self.manufacturer+"\nОграничение по возрасту: "+str(self.age))