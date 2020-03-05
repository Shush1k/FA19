"""
Задача 2. Создайте класс ИЗДАНИЕ с методом, позволяющим вывести на экран информацию об издании,
а также определить, является ли данное издание искомым.
Создайте дочерние классы КНИГА (название, фамилия автора, год издания, издательство),
СТАТЬЯ (название, фамилия автора, название журнала, его номер и год издания),
ЭЛЕКТРОННЫЙ РЕСУРС (название, фамилия автора, ссылка, аннотация) со своими методами вывода информации 
на экран.
Создайте список из п изданий, выведите полную информацию из списка,
а также организуйте поиск изданий по фамилии автора. 
"""
from faker import Faker
from random import randint


class Izdanie:
    def __init__(self, name, aut_name):
        self.name = str(name).title()
        self.aut_name = str(aut_name)

    def info(self):
        print("\n*Class ИЗДАНИЕ*\n")
        print("Название книги:", self.name, "\nАвтор:", self.aut_name)


class Book(Izdanie):
    def __init__(self, name, aut_name, date, place_izd):
        super().__init__(name, aut_name)
        self.date = str(date)
        self.place_izd = str(place_izd)

    def info(self):
        print("\n*Class КНИГА*\n")
        print("Название книги:", self.name, "\nАвтор:", self.aut_name,
              "\nГод издания:", self.date, "\nИздательство:", self.place_izd)


class Article(Izdanie):
    def __init__(self, name, aut_name, journ_name, journ_num, journ_date):
        super().__init__(name, aut_name)
        self.journ_name = str(journ_name)
        self.journ_num = str(journ_num)
        self.journ_date = str(journ_date)

    def info(self):
        print("\n*Class СТАТЬЯ*\n")
        print("Название статьи:", self.name, "\nАвтор:", self.aut_name,
              "\nНазвание журнала:", self.journ_name, "\nНомер журнала:",
              self.journ_num, "\nГод издания:", self.journ_date)


class Web(Izdanie):
    def __init__(self, name, aut_name, link, annotation):
        super().__init__(name, aut_name)
        self.link = str(link)
        self.annotation = str(annotation)

    def info(self):
        print("\n*Class ЭЛЕКТРОННЫЙ РЕСУРС*\n")
        print("Название статьи:", self.name, "\nАвтор:", self.aut_name,
              "\nСсылка:", self.link, "\nАннотация:",
              self.annotation)


def main():
    fake = Faker(["ru_RU"])
    try:
        n = int(input("Количество изданий = "))
    except ValueError:
        print("0_0 упс...")
        return

    d = {
        1: Izdanie,
        2: Book,
        3: Article,
        4: Web
    }
    all_obj = []
    for _ in range(n):
        r = randint(1, 4)
        d_val = {
            1: (fake.word(), fake.name()),
            2: (fake.word(), fake.name(), fake.date(), fake.word()),
            3: (fake.word(), fake.name(), fake.word(), randint(1, 500), fake.date()),
            4: (fake.word(), fake.name(), fake.uri(), "Какая-то аннотация")
        }

        all_obj.append(d[r](*d_val[r]))

    for obj in all_obj:
        obj.info()

    search_author = input("Введите фамилию автора, чтобы найти издание: ")
    find = False

    for obj in all_obj:
        if search_author in obj.aut_name:
            print("\n*Издание найдено*")
            obj.info()
            find = True
    if find == False:
        print("\n*Издание не найдено*")


if __name__ == "__main__":
    main()
