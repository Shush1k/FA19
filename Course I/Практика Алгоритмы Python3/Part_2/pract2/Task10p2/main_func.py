import classTransport, classAirplane, classShip, func
from random import randint
from faker import Faker

def main():
    transport_list, find, fake = [], False, Faker(['ru_RU'])
    try:
        n = int(input("Кол-во транспортных средств = "))
    except ValueError:
        print("Упс..")
        return
    d = {1: classTransport.Transport, 2: classAirplane.Airplane, 3: classAirplane.Car, 4: classShip.Ship}
    for _ in range(n):
        r_int = randint(1, 4)
        d_args = {1: (fake.word(), [randint(1, 100), randint(1, 100)]), 2: (fake.word(), [randint(1, 100), randint(1, 100)], randint(1, 1000), randint(50, 300), randint(1000, 6000)), 3: (fake.word(), [randint(1, 100), randint(1, 100)], randint(1, 1000), randint(1960, 2020)), 4: (fake.word(), [randint(1, 100), randint(1, 100)], randint(1, 1000), randint(50, 300), fake.word()),}
        transport_list.append(d[r_int](*d_args[r_int]))
    for transport in transport_list:
        transport.info()
    func.inp(transport_list, find)