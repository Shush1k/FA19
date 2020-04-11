from datetime import datetime, timedelta
class ProgramSoftware:
    def __init__(self, name, manufacturer, date):
        self.name = name
        self.manufacturer = manufacturer
        self.date = str(date)

    def info(self):
        print("\n*Class ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ*\n")
        print("Название ПО:", self.name, "\nПроизводитель:", self.manufacturer,
              "\nДата установки:", self.date)

    def date_PO(self, user_date):
        d1 = datetime.now() # 
        try:
            d1 = datetime.strptime(user_date, "%d.%m.%Y")
        except:
            return
        d2 = datetime.strptime(self.date, "%d.%m.%Y")
        if d1 >= d2:
            return False
        return True