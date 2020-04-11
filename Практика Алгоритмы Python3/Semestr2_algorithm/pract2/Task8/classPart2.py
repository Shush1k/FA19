import classClient
class Creditor(classClient.Client):
    def __init__(self, surname, date, size, percent, debt):
        super().__init__(surname, date, size, percent)
        self.debt = debt

    def info(self):
        print("\n*Class КРЕДИТОР*")
        print("Фамилия:", self.surname, "\nДата открытия вклада:", self.date,
              "\nРазмер вклада:", self.size, "\nПроцент по вкладу:", self.percent,
              "\nОстаток долга:", self.debt)
class Organization(classClient.Client):
    def __init__(self, surname, date, size, percent):
        super().__init__(surname, date, size, percent)
    def info(self):
        print("\n*Class ОРГАНИЗАЦИЯ*")
        print("Название:", self.surname, "\nДата открытия счета:", self.date,
              "\nНомер счета", self.size, "\nСумма на счету:", self.percent)