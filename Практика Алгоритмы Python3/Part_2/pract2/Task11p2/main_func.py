import classToy, classBall, func
from random import randint, choice
from faker import Faker
def main():
    toy_list, fake = [], Faker(['ru_RU'])
    try:
        n = int(input("Количество товара = "))
    except ValueError:
        print("0_0 упс...")
        return
    d = {1: classToy.Toy, 2: classToy.Cube, 3: classBall.Ball, 4: classBall.BabyCar}
    for _ in range(n):
        materials = ["дерево", "пластик", "хлопок", "металл"]
        k = randint(1, 4)
        d_val = {1: (fake.color_name(), randint(1, 10000), choice(materials)), 2: (fake.color_name(), randint(1, 5000), choice(materials), randint(3, 12)), 3: (randint(1, 5000), fake.color_name(), randint(1, 18), choice(materials)),4: (fake.word(), randint(1, 10000), fake.word(), fake.color_name())}
        toy_list.append(d[k](*d_val[k]))
    for toy in toy_list:
        toy.info()
    func.inp(toy_list)