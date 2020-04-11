import classTransport
class Motorcycle(classTransport.Transport):
    def __init__(self, mark, num, speed, carrying, trailer):
        super().__init__(mark, num, speed, carrying)
        self.trailer = trailer
        self.have_trailer = {
            True: "Да",
            False: "Нет"
        }
        self.Motorcycle_carrying()

    def Motorcycle_carrying(self):
        if self.trailer == False:
            self.carrying = 0

    def info(self):
        print("\n*Class Motorcycle*\n")
        print("Марка: ", self.mark, "\nНомер: ", self.num, "\nСкорость: ", str(self.speed),
              "\nГрузоподъёмность: ", str(self.carrying), "\nНаличие коляски: ", self.have_trailer[self.trailer])