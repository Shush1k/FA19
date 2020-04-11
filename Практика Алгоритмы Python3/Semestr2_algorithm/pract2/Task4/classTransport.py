class Transport:
    def __init__(self, mark, num, speed, carrying):
        self.mark = str(mark)
        self.num = str(num)
        self.speed = speed
        self.carrying = carrying

    def info(self):
        print("\n*Class Transport*\n")
        print("Марка:", self.mark, "\nНомер:", self.num, "\nСкорость:",
              str(self.speed), "\nГрузоподъемность:", str(self.carrying))

    def carry_digit(self):
        return self.carrying
        
class Car(Transport):
    def __init__(self, mark, num, speed, carrying):
        super().__init__(mark, num, speed, carrying)

    def info(self):
        print("\n*Class Automobilius*\n")
        print("Марка: ", self.mark, "\nНомер: ", self.num, "\nСкорость: ",
              str(self.speed), "\nГрузоподъёмность: ", str(self.carrying))