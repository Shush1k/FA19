from datetime import datetime
class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.year_find()
    
    def year_find(self):
        now = datetime.now()
        year_now = int(now.strftime("%Y"))
        year_birth, _, _ = map(int, self.birthday.split("-"))
        self.year_birth = year_now - year_birth
    
    def info(self):
        print("\n*Класс персона*\nФИО: "+self.name+\
            "\n"+"Дата рождения: "+self.birthday)
    
    def years_old(self):
        print("Возраст: "+str(self.year_birth))
            
    def int_years_old(self):
        return self.year_birth