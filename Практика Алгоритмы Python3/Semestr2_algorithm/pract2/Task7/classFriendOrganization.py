import classPhoneDict
class Organization(classPhoneDict.PhoneDict):
    def __init__(self, name, address, phone_number, fax, contact_person):
        super().__init__(name, address, phone_number)
        self.fax = fax
        self.contact_person = contact_person

    def info(self):
        print("\n*class ОРГАНИЗАЦИЯ*\n")
        print("Имя:", self.name, "\nАдрес:", self.address, "\nТелефон:", self.phone_number,
              "\nФакс:", self.fax, "\nКонтактное лицо:", self.contact_person)
class Friend(classPhoneDict.PhoneDict):
    def __init__(self, name, address, phone_number, birthday):
        super().__init__(name, address, phone_number)
        self.birthday = birthday

    def info(self):
        print("\n*class ДРУГ*\n")
        print("Имя:", self.name, "\nАдрес:", self.address, "\nТелефон:", self.phone_number,
              "\nДата рождения:", self.birthday)