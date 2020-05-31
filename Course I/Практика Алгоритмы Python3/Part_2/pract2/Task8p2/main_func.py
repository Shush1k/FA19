import classClient, classPart2, func
from faker import Faker
from random import randint
def main():
    client_list, fake, find = [], Faker("ru_Ru"), False
    try:
        n = int(input("Количество клиентов = "))
    except ValueError:
        print("0_0 упс...")
        return
    d = {1: classClient.Client, 2: classClient.Investor, 3: classPart2.Creditor, 4: classPart2.Organization}
    for _ in range(n):
        r, surname = randint(1, 4), fake.name().split(" ", 1)[0]
        d_val = {1: (surname, fake.date(pattern='%d.%m.%Y'), randint(1000, 100000), randint(1, 20)), 2: (surname, fake.date(pattern='%d.%m.%Y'), randint(1000, 100000), randint(1, 20)), 3: (surname, fake.date(pattern='%d.%m.%Y'), randint(1000, 100000), randint(1, 20), randint(1000, 20000)), 4: (fake.word(), fake.date(pattern='%d.%m.%Y'), randint(1, 500), randint(5000, 1400000))}
        client_list.append(d[r](*d_val[r]))
    for client in client_list:
        client.info()
    func.inp(client_list, find)