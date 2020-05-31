from faker import Faker
from random import randint, choice
import classGoods, classToyBook, func_methods
def main():
    find, goods_list, fake = False, [], Faker(['ru_RU'])
    try:
        n = int(input("Количество товара = "))
    except ValueError:
        print("0_0 упс...")
        return
    d = {1: classGoods.Goods, 2: classToyBook.Toy, 3: classToyBook.Book, 4: classGoods.SportStock}
    for _ in range(n):
        materials = ["дерево", "пластик", "хлопок", "металл"]
        k = randint(1, 4)
        d_val = {1: (fake.word(), randint(1, 10000), fake.word(), randint(1, 18)), 2: (fake.word(), randint(1, 5000), fake.word(), randint(3, 12), choice(materials)), 3: (fake.word(), randint(1, 10000), fake.word(), randint(1, 18), fake.name()), 4: (fake.word(), randint(1, 100000), fake.word(), randint(6, 18))}
        goods_list.append(d[k](*d_val[k]))
    for goods in goods_list:
        goods.info()
    func_methods.input_func(goods_list, find)
