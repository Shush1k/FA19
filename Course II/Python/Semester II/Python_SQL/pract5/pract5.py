from sqlalchemy import select, create_engine, MetaData, Table, cast, String, Integer
from sqlalchemy.sql import func


# connection
engine = create_engine("sqlite:///Students.db")
metadata = MetaData()
connection = engine.connect()

# Загружаем таблицы
exam_marks = Table('exam_marks', metadata, autoload=True, autoload_with=engine)
lecturer = Table('lecturer', metadata, autoload=True, autoload_with=engine)
student = Table('student', metadata, autoload=True, autoload_with=engine)
subj_lect = Table('subj_lect', metadata, autoload=True, autoload_with=engine)
subject = Table('subject', metadata, autoload=True, autoload_with=engine)
university = Table('university', metadata, autoload=True, autoload_with=engine)

STR_LEN = 30


def task1():
    """
    Задание 1

    Составьте запрос для таблицы STUDENT таким образом, чтобы выходная
    таблица содержала один столбец, содержащий последовательность
    разделенных символом “;” (точка с запятой) значений всех столбцов этой
    таблицы, и при этом текстовые значения должны отображаться
    прописными символами (верхний регистр), то есть быть
    представленными в следующем виде:
    10;КУЗНЕЦОВ;БОРИС;0;БРЯНСК;8/12/1981;10.
    """

    s = select([
        cast(student.c.student_id, String(STR_LEN))+";" +
        cast(student.c.surname, String(STR_LEN))+";" +
        cast(student.c.name, String(STR_LEN))+";" +
        cast(student.c.stipend, String(STR_LEN))+";" +
        cast(student.c.city, String(STR_LEN))+";" +
        cast(func.strftime('%d/%m/%Y', student.c.birthday),  String(STR_LEN))+";" +
        cast(student.c.univ_id, String(STR_LEN))+"."
    ])

    # print(s)
    rp = connection.execute(s)
    results = rp.fetchall()
    student_list = []
    for obj in results:
        if obj[0] is not None:
            student_list.append(obj[0].upper())
    return student_list


def task2():
    """
    Задание 2

    Составьте запрос для таблицы STUDENT таким образом, чтобы выходная
    таблица содержала всего один столбец в следующем виде:
    Б.КУЗНЕЦОВ; место жительства-БРЯНСК; родился - 8.12.81.
    """
    s = select([
        cast(func.substr(student.c.name, 1, 1), String(STR_LEN))+"." +
        cast(student.c.surname, String(STR_LEN))+";" +
        cast(student.c.city, String(STR_LEN))+";" +
        cast(func.strftime('%d.%m.%Y.', student.c.birthday),  String(STR_LEN))
    ])

    # print(s)
    rp = connection.execute(s)
    results = rp.fetchall()
    student_list = []
    for obj in results:
        if obj[0] is not None:
            items = obj[0].split(";")
            items = [item.upper() for item in items]
            stud = items[0] + "; место жительства-" + \
                items[1]+"; родился - "+items[2]
            student_list.append(stud)
    return student_list


def task3():
    """
    Задание 3

    Составьте запрос для таблицы STUDENT таким образом, чтобы выходная
    таблица содержала всего один столбец в следующем виде:
    б.кузнецов; место жительства-брянск; родился: 8-дек-1981.
    """
    # func.strftime('%d-%b-%Y',student.c.birthday не работает, видимо strftime тут другой
    s = select([
        cast(func.substr(student.c.name, 1, 1), String(STR_LEN))+"." +
        cast(student.c.surname, String(STR_LEN))+"; место жительства-" +
        cast(student.c.city, String(STR_LEN))+"; родился: " +
        cast(func.strftime('%d-%m-%Y', student.c.birthday),  String(STR_LEN))+"."
    ])

    # print(s)
    rp = connection.execute(s)
    results = rp.fetchall()
    # генераторы ухх
    return [obj[0].lower() for obj in results if obj[0] is not None]


def task4():
    """
    Задание 4

    Составьте запрос для таблицы STUDENT таким образом, чтобы выходная
    таблица содержала всего один столбец в следующем виде:
    Борис Кузнецов родился в 1981 году.
    """
    s = select([
        cast(student.c.name, String(STR_LEN))+" " +
        cast(student.c.surname, String(STR_LEN))+" родился в " +
        cast(func.strftime('%Y', student.c.birthday),
             String(STR_LEN))+" году" + "."
    ])

    # print(s)
    rp = connection.execute(s)
    return rp.fetchone()[0]


def task5():
    """
    Задание 5

    Вывести фамилии, имена студентов и величину получаемых ими
    стипендий, при этом значения стипендий должны быть увеличены в 100 раз.
    """
    s = select([
        student.c.name,
        student.c.surname,
        cast((student.c.stipend * 100), Integer)
    ])

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()


def task6():
    """
    Задание 6

    Тоже, что и в задаче 4, но только для студентов 1, 2 и 4-го курсов и таким
    образом, чтобы фамилии и имена были выведены прописными буквами.
    """
    s = select([
        cast(student.c.name, String(STR_LEN))+" " +
        cast(student.c.surname, String(STR_LEN))+" родился в " +
        cast(func.strftime('%Y', student.c.birthday),
             String(STR_LEN))+" году" + "."
    ]).where(student.c.kurs.in_((1, 2, 4)))

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()


def task7():
    """
    Задание 7

    Составьте запрос для таблицы UNIVERSITY таким образом, чтобы
    выходная таблица содержала всего один столбец в следующем виде:
    Код-10; ВГУ-г.ВОРОНЕЖ; Рейтинг=296.
    """
    s = select([
        "Код-"+cast(university.c.univ_id, String(STR_LEN))+"; " +
        cast(university.c.univ_name, String(STR_LEN))+"-г." +
        cast(university.c.city, String(STR_LEN)) + "; Рейтинг=" +
        cast(university.c.rating, String(STR_LEN)) + "."
    ])

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()


def task8():
    """
    Задание 8

    Тоже, что и в задаче 7, но значения рейтинга требуется округлить до
    первого знака (например , значение 382 округляется до 400).
    """
    # функция func.round(university.c.rating, -2) не работает. В этой библе есть то, что работает?
    s = select([
        "Код-"+cast(university.c.univ_id, String(STR_LEN))+"; " +
        cast(university.c.univ_name, String(STR_LEN))+"-г." +
        cast(university.c.city, String(STR_LEN)) + "; Рейтинг=" +
        cast(func.round(university.c.rating, -2), String(STR_LEN)) + "."
    ])

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()


def task9():
    """
    Задание 9

    Напишите запрос для подсчета количества студентов , сдававших экзамен
    по предмету обучения с идентификатором, равным 20.
    """

    s = select([
        func.count(exam_marks.c.student_id)
    ]).where(exam_marks.c.subj_id == 20)

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()[0][0]


def task10():
    """
    Задание 10

    Напишите запрос, который позволяет подсчитать в таблице EXAM_MARKS
    количество различных предметов обучения.
    """
    s = select([func.count(func.distinct(exam_marks.c.subj_id))])

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()[0][0]


def task11():
    """
    Задание 11

    Напишите запрос, который выполняет выборку для каждого студента
    значения его идентификатора и минимальной из полученных им оценок.
    """
    s = select([
        exam_marks.c.student_id,
        func.min(exam_marks.c.mark)
    ]).group_by(exam_marks.c.student_id)

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()


def task12():
    """
    Задание 12

    Напишите запрос, который выполняет выборку для каждого студента
    значения его идентификатора и максимальной из полученных им оценок.
    """
    s = select([
        exam_marks.c.student_id,
        func.max(exam_marks.c.mark)
    ]).group_by(exam_marks.c.student_id)

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()


def task13():
    """
    Задание 13

    Напишите запрос, выполняющий вывод фамилии первого в алфавитном
    порядке (по фамилии) студента, фамилия которого начинается на букву “И”.
    """
    s = select([
        student.c.surname,
    ]).where(student.c.surname.like("И%")).limit(1)

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()


def task14():
    """
    Задание 14

    Напишите запрос, который выполняет вывод для каждого предмета
    обучения на именование предмета и максимальное значение номера
    семестра, в котором этот предмет преподается.
    """
    s = select([
        subject.c.subj_name,
        func.max(subject.c.semester)
    ]).group_by(subject.c.subj_name)

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()


def task15():
    """
    Задание 15

    Напишите запрос, который выполняет вывод данных для каждого
    конкретного дня сдачи экзамена о количестве студентов, сдававших
    экзамен в этот день.
    """
    s = select([
        func.count(func.distinct(exam_marks.c.student_id)
                   ).label("Кол-во студентов"),
        exam_marks.c.exam_date,
        exam_marks.c.exam_id
    ]).group_by(exam_marks.c.exam_id)

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()


def task16():
    """
    Задание 16

    Напишите запрос для получения среднего балла
    для каждого курса по каждому предмету.
    """

    tables = student.join(
        exam_marks, student.c.student_id == exam_marks.c.student_id)
    s = select([
        student.c.kurs,
        func.avg(exam_marks.c.mark),
        exam_marks.c.subj_id]
    ).select_from(tables).group_by(student.c.kurs, exam_marks.c.subj_id)

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()


def task17():
    """
    Задание 17

    Напишите запрос для получения среднего балла для каждого студента.
    """
    s = select([
        exam_marks.c.student_id,
        func.avg(exam_marks.c.mark).label("Ср. оценка")
    ]).group_by(exam_marks.c.student_id)

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()


def task18():
    """
    Задание 18

    Напишите запрос для получения среднего балла для каждого экзамена.
    """
    s = select([
        exam_marks.c.exam_id,
        func.avg(exam_marks.c.mark).label("Ср. оценка")
    ]).group_by(exam_marks.c.exam_id)

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()


def task19():
    """
    Задание 19

    Напишите запрос для определения количества студентов, сдававших каждый экзамен
    """
    s = select([
        exam_marks.c.exam_id,
        func.count(exam_marks.c.student_id).label("Кол-во студентов")
    ]).group_by(exam_marks.c.exam_id)

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()


def task20():
    """
    Задание 20

    Напишите запрос для определения количества изучаемых предметов на каждом курсе
    """
    s = select([
        cast(((subject.c.semester + 1) / 2), Integer).label("kurs"),
        func.count().label("Кол-во предметов")
    ]).group_by("kurs")

    # print(s)
    rp = connection.execute(s)
    return rp.fetchall()


def main():
    task_list = [task1, task2, task3, task4, task5,
                 task6, task7, task8, task9, task10, task11,
                 task12, task13, task14, task15, task16, task17,
                 task18, task19, task20]

    for i in range(len(task_list)):
        print(f"\nЗадание{i+1}")
        print(task_list[i]())


if __name__ == "__main__":
    main()
