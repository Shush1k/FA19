from classTransport import Transport
class Truck(Transport):
    def __init__(self, mark, num, speed, carrying, trailer):
        super().__init__(mark, num, speed, carrying)
        self.trailer = trailer
        self.have_trailer = {
            True: "Да",
            False: "Нет"
        }
        self.Truck_carrying()

    def Truck_carrying(self):
        if self.trailer == True:
            self.carrying *= 2

    def info(self):
        print("\n*Class Truck*\n")
        print("Марка: ", self.mark, "\nНомер: ", self.num, "\nСкорость: ", str(self.speed),
              "\nГрузоподъёмность: ", str(self.carrying), "\nНаличие прицепа: ", self.have_trailer[self.trailer])