from classTransport import Transport
class Airplane(Transport):
    """САМОЛЕТ (марка, максимальные скорость и высота, количество пассажиров, координаты)"""
    def __init__(self, mark, coordinate, persons, speed, height):
        super().__init__(mark, coordinate)
        self.height = height
        self.speed = speed
        self.persons = persons

    def info(self):
        print("\n*Class САМОЛЕТ*\n")
        print("Марка:", self.mark, "\nСкорость:", self.speed, "\nВысота:", self.height, "\nКоординаты:",
              self.coords_to_str(), "\nКоличество пассажиров:", self.persons)
class Car(Transport):
    """АВТОМОБИЛЬ (марка, номер, год выпуска, координаты)"""

    def __init__(self, mark, coordinate, num, year_release):
        self.mark = mark
        self.num = num
        self.year_release = year_release
        self.coordinate = coordinate
    def info(self):
        print("\n*Class АВТОМОБИЛЬ*\n")
        print("Марка: ", self.mark, "\nНомер: ", self.num, "\nГод выпуска: ", self.year_release,
              "\nКоординаты:", self.coords_to_str())