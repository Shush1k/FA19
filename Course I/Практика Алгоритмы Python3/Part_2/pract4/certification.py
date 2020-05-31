import datetime
import pandas as pd
"""
Разработать программное средство с использованием ООП для
представления успеваемости студентов по дисциплине:

1) Промежуточная аттестация максимум 20 баллов, разбитые
по количеству работ (практики, контрольная и тестирование в 1
половине семестра);
2) Работа в семестре 20 баллов (практики, контрольная и
тестирование во 2 половине семестра);
3) Экзамен 60 баллов;
4) Выставление итоговой оценки.
Объект класса должен содержать поля для сохранения имени
студента и истории получения баллов (по практикам, контрольным и
тестированиям) с учетом даты получения оценки по схеме: выполнено,
защищено.
"""
# Список полезностей: работа с датами, функции на проверку ввода
class Student:
    """Студент Вуза"""
    def __init__(self, name, surname, birthday, faculty, course, certification, date_list_one, semester_work, date_list_two, exam):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.faculty = faculty
        self.course = str(course)
        self.certification = certification
        self.date_list_one = date_list_one
        self.semester_work = semester_work
        self.date_list_two = date_list_two
        self.exam = exam
    def get_sem_points(self, *args):
        """Баллы за практики, КР, тесты"""
        return sum(*args)


    def get_points(self):
        """Подсчет баллов за весь курс"""
        return self.get_sem_points(self.certification) + self.get_sem_points(self.semester_work) + self.exam


    def info(self):
        """
        print("Имя: "+self.name+\
            "\nФамилия: "+self.surname+\
            "\n"+"Дата рождения: "+self.birthday+\
            "\nФакультет: "+self.faculty+\
            "\nКурс: " + self.course+\
            "\nПромежуточная аттестация: "+str(self.certification)+\
            "\nРабота в семестре: "+str(self.semester_work)+\
            "\nЭкзамен: "+str(self.exam)+\
            "\nИтоговая оценка: " + str(self.get_points())
        )
        """

        return "Фамилия: "+self.surname+\
            "\nИмя: "+self.name+\
            "\n"+"Дата рождения: "+self.birthday+\
            "\nФакультет: "+self.faculty+\
            "\nКурс: " + self.course+\
            "\n\n   Промежуточная аттестация: "+str(self.get_sem_points(self.certification))+\
            "\n\tКР от "+str(self.date_list_one[0])+"  Баллы за КР: "+str(self.certification[0])+\
            "\n\tБаллы за тест1: "+str(self.certification[1])+\
            "\n\tБаллы за тест2: "+str(self.certification[2])+\
            "\n\tБаллы за тест3: "+str(self.certification[3])+\
            "\n\tБаллы за практику1: "+str(self.certification[4])+"  Дата: "+str(self.date_list_one[1])+\
            "\n\tБаллы за практику2: "+str(self.certification[5])+"  Дата: "+str(self.date_list_one[2])+\
            "\n\tБаллы за практику3: "+str(self.certification[6])+"  Дата: "+str(self.date_list_one[3])+\
            "\n   Работа в семестре: "+str(self.get_sem_points(self.semester_work))+\
            "\n\tКР от "+str(self.date_list_two[0])+"  Баллы за КР: "+str(self.semester_work[0])+\
            "\n\tБаллы за тест1: "+str(self.semester_work[1])+\
            "\n\tБаллы за тест2: "+str(self.semester_work[2])+\
            "\n\tБаллы за тест3: "+str(self.semester_work[3])+\
            "\n\tБаллы за практику1: "+str(self.semester_work[4])+"  Дата: "+str(self.date_list_two[1])+\
            "\n\tБаллы за практику2: "+str(self.semester_work[5])+"  Дата: "+str(self.date_list_two[2])+\
            "\n\tБаллы за практику3: "+str(self.semester_work[6])+"  Дата: "+str(self.date_list_two[3])+\
            "\nЭкзамен: "+str(self.exam)+" баллов"\
            "\nИтоговая оценка: "+str(self.get_points())+" баллов"

# Добавить студента// Весь ввод!
def create_Student():
    print("Заполните данные о студенте!\n")
    surname = input("Фамилия: ").title()
    name = input("Имя: ").title()

    date_flag = False
    while not date_flag:
        birthday = input("Введите дату рождения вида: 13.03.2020 \n>>>  ")
        date_flag, _ = string_to_datetime(birthday)
        if date_flag:
            ...
        else:
            print("Некорректная дата!")  
    
    faculty = "ПМИИТ"
    course = 1
    
    print("\nПромежуточная аттестация\nВсего: 1 - КР, 3 - Теста, 3 - Практики\n")
    points_flag = False
    while not points_flag:
        certification = []
        date_list = []
        CONTROL_DATE, _ = input_DATE("КР")
        CONTROL_POINTS = input_N("Баллы за КР")
        certification.append(CONTROL_POINTS)
        date_list.append(CONTROL_DATE)
        # На случай, если нужна будет дата за тест
        """    
        #_, TEST1_DETERMINED = input_DATE("назначенную вами для теста 1")
        #TEST1_DATE, TEST1_DATETIME = input_DATE("учеником теста 1")
        #date_penalty(TEST1_DATETIME, TEST1_DETERMINED)
        """

        TEST1_POINTS = input_N("Баллы за тест 1")
        certification.append(TEST1_POINTS)
        
        TEST2_POINTS = input_N("Баллы за тест 2")
        certification.append(TEST2_POINTS)

        TEST3_POINTS = input_N("Баллы за тест 3")
        certification.append(TEST3_POINTS)
        
        _, PRACT1_DETERMINED = input_DATE("назначенную вами для практики 1")
        PRACT1_DATE, PRACT1_DATETIME= input_DATE("учеником практики 1")
        date_penalty(PRACT1_DATETIME, PRACT1_DETERMINED)
        PRACT1_POINTS = input_N("Баллы за практику 1")
        certification.append(PRACT1_POINTS)
        date_list.append(PRACT1_DATE)

        _, PRACT2_DETERMINED = input_DATE("назначенную вами для практики 2")
        PRACT2_DATE, PRACT2_DATETIME= input_DATE("учеником практики 2")
        date_penalty(PRACT2_DATETIME, PRACT2_DETERMINED)
        PRACT2_POINTS = input_N("Баллы за практику 2")
        certification.append(PRACT2_POINTS)
        date_list.append(PRACT2_DATE)

        _, PRACT3_DETERMINED = input_DATE("назначенную вами для практики 3")
        PRACT3_DATE, PRACT3_DATETIME = input_DATE("учеником практики 3")
        date_penalty(PRACT3_DATETIME, PRACT3_DETERMINED)
        PRACT3_POINTS = input_N("Баллы за практику 3")
        certification.append(PRACT3_POINTS)
        date_list.append(PRACT3_DATE)
        if sum(certification) < 21:
            points_flag = True
        else:
            print("\033[31m"+"Сумма баллов должна быть меньше 20! Вам придется заполнить промежуточную аттестацию ещё раз"+"\033[0m")

    
    print("\nРабота за второй семестр\nВсего: 1 - КР, 3 - Теста, 3 - Практики\n")
    points_sem2_flag = False
    while not points_sem2_flag:
        semester_work = []
        date_list_two = []
        CONTROL_DATE, _ = input_DATE("КР")
        CONTROL_POINTS = input_N("Баллы за КР")
        semester_work.append(CONTROL_POINTS)
        date_list_two.append(CONTROL_DATE)


        TEST1_POINTS = input_N("Баллы за тест 1")
        semester_work.append(TEST1_POINTS)
        
        TEST2_POINTS = input_N("Баллы за тест 2")
        semester_work.append(TEST2_POINTS)

        TEST3_POINTS = input_N("Баллы за тест 3")
        semester_work.append(TEST3_POINTS)
        
        _, PRACT1_DETERMINED = input_DATE("назначенную вами для практики 1")
        PRACT1_DATE, PRACT1_DATETIME= input_DATE("учеником практики 1")
        date_penalty(PRACT1_DATETIME, PRACT1_DETERMINED)
        PRACT1_POINTS = input_N("Баллы за практику 1")
        semester_work.append(PRACT1_POINTS)
        date_list_two.append(PRACT1_DATE)

        _, PRACT2_DETERMINED = input_DATE("назначенную вами для практики 2")
        PRACT2_DATE, PRACT2_DATETIME= input_DATE("учеником практики 2")
        date_penalty(PRACT2_DATETIME, PRACT2_DETERMINED)
        PRACT2_POINTS = input_N("Баллы за практику 2")
        semester_work.append(PRACT2_POINTS)
        date_list_two.append(PRACT2_DATE)

        _, PRACT3_DETERMINED = input_DATE("назначенную вами для практики 3")
        PRACT3_DATE, PRACT3_DATETIME = input_DATE("учеником практики 3")
        date_penalty(PRACT3_DATETIME, PRACT3_DETERMINED)
        PRACT3_POINTS = input_N("Баллы за практику 3")
        semester_work.append(PRACT3_POINTS)
        date_list_two.append(PRACT3_DATE)
        if sum(semester_work) < 21:
            points_sem2_flag = True
        else:
            print("\033[31m"+"Сумма баллов должна быть меньше 20! Вам придется заполнить работу за второй семестр ещё раз"+"\033[0m")
    # EXAM
    exam_points = input_exam("Баллы за экзамен")
    
    return name, surname, birthday, faculty, course, certification, date_list, semester_work, date_list_two, exam_points

def string_to_datetime(date):
    """Функция проверки даты ОЧЕНЬ НУЖНАЯ"""
    try:
        date = datetime.datetime.strptime(date, "%d.%m.%Y")
        return True, date
    except:
        return False, None

def input_N(name):
    try:
        N = int(input(f"{name}: "))
        return N
    except ValueError:
        print("Вводить число!")
        return input_N(name)


def input_exam(name):
    try:
        N = int(input(f"{name}: "))
        if 0 <= N < 61:
            return N
        else:
            if N < 0:
                print("Число должно быть положительным!")
                return input_exam(name)
            else:
                print("Число баллов за экзамен не может превышать 60!")
                return input_exam(name)
    except ValueError:
        print("Вводить число!")
        return input_exam(name)

def input_DATE(work_type):
    """work_type - тип работы(кр, тест, практика)"""
    test_date_flag = False
    while not test_date_flag:
        date = input(f"Введите дату выполнения {work_type}\nПример: 13.03.2020 \n>>>  ")
        test_date_flag, datetime_date = string_to_datetime(date)
        if test_date_flag:
            ...
        else:
            print("Некорректная дата!")  
    return date, datetime_date

def date_penalty(performance_date, assigned_date):
    """
    Функция для штрафа по дате
    performance_date - сдача работы студентом
    assigned_date - установленная преподавателем дата
    """
    delta = (performance_date - assigned_date).days
    if -6 <= delta < 1:
        print("Студент сдал в срок(первая неделя)")
    elif 1 <= delta < 8:
        print("Студент сдал спустя примерно неделю. Просрочено на количество дней: ", delta)
    elif 8 <= delta < 15:
        print(" Просрочено на количество дней: ", delta)
    else:
        print("Можно считать, что студент не сдал. Просрочено на количество дней: ", delta)


def save_Student(stud):
    with open("Priv_FA19/pract4/students.txt", "a", encoding="utf-8") as file:
        file.write(stud.info()+"\n"+"\n")


def get_stud_info(surname_input):
    with open('Priv_FA19/pract4/students.txt', encoding="utf-8") as f:
        for index, line in enumerate(f):
            if surname_input == line.strip():
                return index
        return 0


def main():
    while True:
        print("\nСписок действий:\n1 - Информация о студентах\n2 - Добавить студента\n3 - Вывод информации по ученику\n0 - Выход")
        choice = input_N("Выберите действие")
        if choice == 0:
            print("...")
            break
        elif choice == 1:
            with open('Priv_FA19/pract4/students.txt', encoding="utf-8") as f:
                print("\n"+f.read())
        elif choice == 2:
            stud = create_Student()
            # Вместо создания
            #stud = ('Александр', 'Баранов', '18.08.2001', 'ПМИИТ', 1, [4, 1, 1, 1, 3, 4, 4], ['11.03.2020', '18.03.2020', '25.03.2020', '1.04.2020'], [3, 1, 2, 2, 2, 2, 3], ['8.04.2020', '15.04.2020', '22.04.2020', '29.03.2020'], 55)
            save_Student(Student(*stud))
            print("Студент создан")
        elif choice == 3:
            surname_input = "Фамилия: "
            surname_input += input("Введите фамилию: ")
            index = get_stud_info(surname_input)
            if index != 0:
                text = open('Priv_FA19/pract4/students.txt', 'r', encoding="utf-8").readlines()[index:index+24]
                text = ''.join(text)
                print("\n"+text)
            else:
                print("Студент не найден")
        else:
            pass
    


if __name__ == "__main__":
    main()
    input()