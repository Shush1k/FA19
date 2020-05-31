"""
Задача 14*:
Создайте двусвязный список (или массив) групп факультета. Каждая группа представляет
собой односвязный список (или массив) студентов.
"""

import yaml
# Путь к файлу
TXT_FILE = r"Priv_FA19\pract5\task14.yml"

class GetData(object):
    def __init__(self):
        self.get_dict()

    def get_dict(self):
        """Словарь группа - список из студентов"""
        with open(TXT_FILE, 'r', encoding="utf-8") as stream:
            self.d = yaml.safe_load(stream)


class Students(object):
    """
    Класс для создания коллекции студентов в виде односвязанного списка
    Поля:
    - value - значение объекта
    - next - ссылка на след объект в коллекции
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class Groups(object):
    """
    Класс для создания коллекции групп в виде двусвязного списка
    Поля:
    - value - значение объекта
    - students - список студентов
    - next - ссылка на след объект в коллекции
    - previous - ссылка на предыдущий объект коллекции
    """

    def __init__(self, value=None, students=None, next=None, previous=None):
        self.value = value
        self.students = students
        self.next = next
        self.previous = previous

    def __str__(self):
        return str(self.value)


class MainDef(object):

    def __init__(self):
        self.get_data()
        self.get_arrays()

    def get_data(self):
        # Храним тот же словарь в переменной data
        self.data = GetData().d


    def get_arrays(self):
        """Добавляем в двусвязный массив студентов из разных групп"""
        group_list = []
        for group in self.data:
            student_list = []
            for student in self.data[group]:
                student_list.append(Students(student))
                print("Добавили студента  '" + student + "' ")

                # Связываем между собой студентов группы
                for i in range(len(student_list) - 1):
                    student_list[i].next = student_list[i + 1]

            group_list.append((group, Groups(group, student_list)))
            print("Добавили всех студентов группы", group)
            # Меняем номер группы на следующий
            for i in range(len(group_list) - 1):
                group_list[i][1].next = group_list[i + 1][1]
                group_list[i + 1][1].previous = group_list[i][1]

        for group in group_list:
            print("\n")
            print("Группа предыдущая/группа следующая/список из ссылок студентов")
            print(group[1].previous, "->", group[0], "->", group[1].next)
            print("Cтуденты группы:")
            # Вывод студентов
            for student in group[1].students:
                print(student.value, "->", student.next)


if __name__ == "__main__":
    MainDef()
