class PhoneDict:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def pers_search(self, input_name):
        if input_name in self.name:
            return True
        return False

    def info(self):
        print("\n*class ТЕЛЕФОННЫЙ СПРАВОЧНИК*\n")
        print("Имя:", self.name, "\nАдрес:", self.address,
              "\nТелефон:", self.phone_number)
class Person(PhoneDict):
    def __init__(self, name, address, phone_number):
        super().__init__(name, address, phone_number)

    def info(self):
        print("\n*class ПЕРСОНА*\n")
        print("Имя:", self.name, "\nАдрес:", self.address,
              "\nТелефон:", self.phone_number)