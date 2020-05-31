import classPerson
class Teacher(classPerson.Person):
    def __init__(self, name, birthday, faculty, job, years):
        super().__init__(name, birthday)
        self.faculty = faculty
        self.job = job
        self.experience = str(years)
    
    def info(self):
        print("\n*Класс учителя*\nФИО: "+self.name+\
            "\n"+"Дата рождения: "+self.birthday+\
            "\nФакультет: "+self.faculty+\
            "\nДолжность: "+self.job+\
            "\nСтаж: "+self.experience)