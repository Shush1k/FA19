import classPhoneDict, func, classFriendOrganization as Fclass
from faker import Faker
from random import randint
def main():
    find, fake, persons_list = False, Faker(['ru_RU']), []
    try:
        n = int(input("Количество записей = "))
    except ValueError:
        print("Упс....")
        return
    d = {1: classPhoneDict.PhoneDict, 2: classPhoneDict.Person, 3: Fclass.Organization, 4: Fclass.Friend}
    for _ in range(n):
        r = randint(1, 4)
        d_val = {1: (fake.name(), fake.address(), fake.phone_number()), 2: (fake.name(), fake.address(), fake.phone_number()), 3: (fake.word(), fake.address(), fake.phone_number(), fake.phone_number(), fake.name()), 4: (fake.name(), fake.address(), fake.phone_number(), fake.date(pattern='%d.%m.%Y')),}
        persons_list.append(d[r](*d_val[r]))
    for pers in persons_list:
        pers.info()
    func.inp(persons_list, find)