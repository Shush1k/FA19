import classPart1
class Free(classPart1.ProgramSoftware):
    def __init__(self, name, manufacturer, date):
        super().__init__(name, manufacturer, date)
    def info(self):
        print("\n*Class СВОБОДНОЕ*\n")
        print("Название ПО:", self.name, "\nПроизводитель:", self.manufacturer,
              "\nДата установки:", self.date)
class Shareware(classPart1.ProgramSoftware):
    def __init__(self, name, manufacturer, date, free_period):
        super().__init__(name, manufacturer, date)
        self.free_period = free_period
    def info(self):
        print("\n*Class УСЛОВНО БЕСПЛАТНОЕ*\n")
        print("Название ПО:", self.name, "\nПроизводитель:", self.manufacturer,
              "\nДата установки:", self.date, "\nСрок бесплатного использования:", self.free_period)
class Commercial(classPart1.ProgramSoftware):
    def __init__(self, name, manufacturer, price, date, use_period):
        super().__init__(name, manufacturer, date)
        self.price = price
        self.use_period = use_period
    def info(self):
        print("\n*Class КОММЕРЧЕСКОЕ*\n")
        print("Название ПО:", self.name, "\nПроизводитель:", self.manufacturer, "\nЦена:", self.price,
              "\nДата установки:", self.date, "\nСрок использования:", self.use_period)