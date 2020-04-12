from classGoods import Goods
class Toy(Goods):
    def __init__(self, name, price, manufacturer, age, material):
        super().__init__(name, price, manufacturer, age)
        self.material = str(material)

    def info(self):
        print("\n*Class ИГРУШКА*\n")
        print("Название: "+self.name+"\nЦена: "+str(self.price)+"\nПроизводитель: " +
              self.manufacturer+"\nОграничение по возрасту: "+str(self.age)+"\nМатериал: "+self.material)


class Book(Goods):
    def __init__(self, name, price, manufacturer, age, author):
        super().__init__(name, price, manufacturer, age)
        self.author = str(author)

    def info(self):
        print("\n*Class КНИГА*\n")
        print("Название: "+self.name+"\nЦена: "+str(self.price)+"\nИздательство: " +
              self.manufacturer+"\nОграничение по возрасту: "+str(self.age)+"\nАвтор: "+self.author)