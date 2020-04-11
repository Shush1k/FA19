import classIzdanieBook, classArticle, classWeb
from faker import Faker
from random import randint
def main():
    all_obj, find, fake = [], False, Faker(["ru_RU"])
    try:
        n = int(input("Количество изданий = "))
    except ValueError:
        print("0_0 упс...")
        return
    d = {1: classIzdanieBook.Izdanie, 2: classIzdanieBook.Book, 3: classArticle.Article, 4: classWeb.Web}
    for _ in range(n):
        r = randint(1, 4)
        d_val = {1: (fake.word(), fake.name()), 2: (fake.word(), fake.name(), fake.date(), fake.word()), 3: (fake.word(), fake.name(), fake.word(), randint(1, 500), fake.date()), 4: (fake.word(), fake.name(), fake.uri(), "Какая-то аннотация")}
        all_obj.append(d[r](*d_val[r]))
    for obj in all_obj:
        obj.info()
    search_author = input("Введите фамилию автора, чтобы найти издание: ")
    for obj in all_obj:
        if search_author in obj.aut_name:
            print("\n*Издание найдено*")
            obj.info()
            find = True
    if find == False:
        print("\n*Издание не найдено*")