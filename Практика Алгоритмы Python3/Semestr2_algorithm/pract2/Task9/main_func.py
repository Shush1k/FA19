from random import randint
from faker import Faker
import classPart1, classPart2, func
def main():
    fake = Faker(['ru_RU'])
    try:
        n = int(input("Количество видов ПО = "))
    except ValueError:
        print("0_0 упс...")
        return
    d = {1: classPart1.ProgramSoftware, 2: classPart2.Free, 3: classPart2.Shareware, 4: classPart2.Commercial}
    prog_list = []
    for _ in range(n):
        r = randint(1, 4)
        d_val = {1: (fake.word(), fake.name(), fake.date(pattern='%d.%m.%Y')), 2: (fake.word(), fake.name(), fake.date(pattern='%d.%m.%Y')), 3: (fake.word(), fake.name(), fake.date(pattern='%d.%m.%Y'), fake.date(pattern='%d.%m.%Y')), 4: (fake.word(), fake.name(), randint(500, 50000), fake.date(pattern='%d.%m.%Y'), fake.date(pattern='%d.%m.%Y'))}
        prog_list.append(d[r](*d_val[r]))
    for prog in prog_list:
        prog.info()
    func.inp(prog_list)