import classPerson
class Abiturient(classPerson.Person):
    def __init__(self, name, birthday, faculty):
        super().__init__(name, birthday)
        self.faculty = faculty
        
    def info(self):
        print("\n*Класс абитуриента*\nФИО: "+self.name+\
            "\n"+"Дата рождения: "+self.birthday+\
            "\nФакультет: "+self.faculty)
        
class Student(classPerson.Person):
    def __init__(self, name, birthday, faculty, course):
        super().__init__(name, birthday)
        self.faculty = faculty
        self.course = str(course)
        
    def info(self):
        print("\n*Класс абитуриента*\nФИО: "+self.name+\
            "\n"+"Дата рождения: "+self.birthday+\
            "\nФакультет: "+self.faculty+\
            "\nКурс: " + self.course)    