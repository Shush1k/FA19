import classTransport
class Ship(classTransport.Transport):
    """КОРАБЛЬ (название, координаты, скорость, количество пассажиров, порт приписки)"""

    def __init__(self, mark, coordinate, persons, speed, port):
        super().__init__(mark, coordinate)
        self.port = port
        self.speed = speed
        self.persons = persons

    def info(self):
        print("\n*Class КОРАБЛЬ*\n")
        print("Название: ", self.mark, "\nКоординаты", self.coords_to_str(), "\nСкорость: ", self.speed,
              "\nКоличество пассажиров: ", self.persons, "\nПорт приписки: ", self.port)