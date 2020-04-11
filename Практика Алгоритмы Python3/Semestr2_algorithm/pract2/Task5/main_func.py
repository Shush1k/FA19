import classGoods, classParty, classPhone, classProduct
from faker import Faker
from random import randint
import check, secondpart
def main():
    find, fake, all_obj = False, Faker(["ru_RU"]), []
    d = {1: classGoods.Goods, 2: classProduct.Product, 3: classParty.Party, 4: classPhone.Phone}
    n = check.checking()
    for _ in range(n):
        r = randint(1, 4)
        data1, data2 = fake.date(pattern="%d.%m.%Y"), fake.date(pattern="%d.%m.%Y")
        d_val = {1: (fake.word(), randint(1, 100000), data1, data2), 2: (fake.word(), randint(1, 100000), data1, data2), 3: (fake.word(), randint(1, 100000), data1, data2, randint(1, 100000)), 4: (fake.word(), randint(1, 100000))}
        all_obj.append(d[r](*d_val[r]))
    for obj in all_obj:
        obj.info()
    secondpart.input_func(all_obj, find)
    