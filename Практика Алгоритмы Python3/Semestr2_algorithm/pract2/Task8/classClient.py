class Client:
    def __init__(self, surname, date, size, percent):
        self.surname = surname
        self.date = date
        self.size = size
        self.percent = percent

    def info(self):
        print("\n*Class КЛИЕНТ*")
        print("Фамилия:", self.surname, "\nДата открытия вклада:", self.date,
              "\nРазмер вклада:", self.size, "\nПроцент по вкладу:", self.percent)

    def client_date(self, user_date):
        if user_date == str(self.date):
            return True
        return False

class Investor(Client):
    def __init__(self, surname, date, size, percent):
        super().__init__(surname, date, size, percent)
    def info(self):
        print("\n*Class ВКЛАДЧИК*")
        print("Фамилия:", self.surname, "\nДата открытия вклада:", self.date,
              "\nРазмер вклада:", self.size, "\nПроцент по вкладу:", self.percent)