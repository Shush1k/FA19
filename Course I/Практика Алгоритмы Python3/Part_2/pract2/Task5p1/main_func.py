from faker import Faker
import random, lists, classPerson, classTeacher, classAbiturStudent
def main():
    try:
        count_pers = int(input("Количество персон = "))
        age_range = list(map(int, input("Введите диапозон возраста персон!"+\
        "\nПример:18 40"+"\n").split(" ")))
        min_age, max_age = sorted(age_range)
    except ValueError:
        print("Сосредоточтесь...")
        return
    faculty, all_persons, fake, jobs = lists.faculty,[], Faker(['ru_RU']), lists.jobs
    d = {1: classPerson.Person, 2: classAbiturStudent.Abiturient, 3: classAbiturStudent.Student, 4: classTeacher.Teacher}
    for _ in range(count_pers):
        d_pers = {1: [fake.name(), fake.date()], 2: [fake.name(), fake.date(), random.choice(faculty)], 3: [fake.name(), fake.date(), random.choice(faculty), random.randint(1,4)], 4: [fake.name(), fake.date(), random.choice(faculty), random.choice(jobs), random.randint(2,20)],}
        k = random.randint(1, 4)
        all_persons.append(d[k](*d_pers[k]))
        all_persons.sort(key=lambda x: x.int_years_old())
    for pers in all_persons:
        pers.info()
        pers.years_old()
        if pers.int_years_old() in range(min_age, max_age+1):
            print("\033[31m"+"Персона попадает в заданный диапазон"+"\033[0m")