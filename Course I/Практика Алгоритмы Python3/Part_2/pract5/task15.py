"""
Задача 15*:
Дан список студентов. Элемент списка содержит фамилию, имя, отчество, год рождения, курс,
номер группы, оценки по пяти предметам. Упорядочите студентов по курсу, причем студенты
одного курса располагались в алфавитном порядке.
Найдите средний балл каждой группы по каждому предмету. Определите самого старшего
студента и самого младшего студентов.
Для каждой группы найдите лучшего с точки зрения успеваемости студента. Выберете
структуру данных для программной реализации.
""" 

class Main(object):
    def __init__(self):

        self.student_list = [
            ["Деменчук", "Георгий", "Максимович", "1999", 3, "ПИ19-4", [2, 5, 3, 4, 5]],
            ["Бедак", "Иван", "Иванович", "2001", 1, "ПИ19-2", [3, 5, 3, 4, 4]],
            ["Баранов", "Александр", "Вячеславович", "2001", 2, "ПИ19-3", [2, 5, 3, 4, 5]],
            ["Максим", "Максим", "Максимович", "2001", 2, "ПИ19-2", [2, 3, 3, 4, 5]],
            
        ]
        self.datadict = {"oldest": 9999, "youngest": 0, "data": {}}

        self.main_func()
        self.out_data()

    def main_func(self):

        datadict = self.datadict
        student_list = self.student_list
        student_list.sort(key=lambda x: (x[4], x[0]))

        for collection in student_list:

            # Проверка на лучшего студента
            best_student = {
                "fio": collection[0] + " " + collection[1] + " " + collection[2],
                "date": collection[3],
                "course": collection[4],
                "sum": sum(collection[6]),
            }

            if collection[5] in datadict["data"]:
                # Проверка на максимальную сумму баллов, нахождение лучшего студента
                if datadict["data"][collection[5]]["best"]["sum"] < sum(collection[6]):
                    datadict["data"][collection[5]] = {"best": best_student}
                # Cумма баллов по группе
                datadict["data"][collection[5]]["subjects"]["sum"] = [
                    sum(x) for x in zip(collection[6], datadict["data"][collection[5]]["subjects"]["sum"])
                ]
                # Кол-во студентов
                datadict["data"][collection[5]]["subjects"]["count"] += 1

            else:
                datadict["data"][collection[5]] = {"best": best_student, "subjects": {"count": 1, "sum": collection[6]}}
            # Находим младшего и старшего студента
            if int(datadict["youngest"]) < int(collection[3]):
                datadict["youngest"] = collection[3]
            if int(datadict["oldest"]) > int(collection[3]):
                datadict["oldest"] = collection[3]

        for group in datadict["data"]:
            # Среднее арифметическое
            datadict["data"][group]["subjects"] = [x / datadict["data"][group]["subjects"]["count"] for x in datadict["data"][group]["subjects"]["sum"]]

        self.student_list = student_list
        self.datadict = datadict

    def out_data(self):
        d = self.datadict
        print("Отсортированный словарь:\n", self.student_list, "\n")
        print("Самый старший студент " + d["oldest"] + "-го года")
        print("Самый младший студент " + d["youngest"] + "-го года")
        for group, data in d["data"].items():
            print("\n*Группа " + group + "*")
            b = data["best"]
            print("Луший студент группы:\n" + b["fio"] + " " + b["date"] + ",", b["course"], "курс,", "cумма баллов",
                  b["sum"])
            print("Средние баллы группы по предметам:", data["subjects"])


if __name__ == "__main__":
    Main()