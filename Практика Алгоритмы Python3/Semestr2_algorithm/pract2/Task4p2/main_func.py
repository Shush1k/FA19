import classTransport, classMotorcycle, classTruck, inp
from random import randint
def main():
    n = inp.inputing()
    d = {1: classTransport.Transport, 2: classTransport.Car, 3: classMotorcycle.Motorcycle, 4: classTruck.Truck}
    transport_list = []
    for _ in range(n):
        r = randint(1, 4)
        d_val = {1: (randint(1, 100), randint(1, 1000), randint(60, 300), randint(500, 10000)), 2: (randint(1, 100), randint(1, 1000), randint(60, 300), randint(500, 10000)), 3: (randint(1, 100), randint(1, 1000), randint(60, 300), randint(500, 10000), bool(randint(0, 1))), 4: (randint(1, 100), randint(1, 1000), randint(60, 300), randint(500, 10000), bool(randint(0, 1))),}
        transport_list.append(d[r](*d_val[r]))
    for transport in transport_list:
        transport.info()
    try:
        carrying_input = float(input("\nГрузоподъёмность = "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    print("\n*Транспорт, грузоподъёмность которого меньше или равна заданной*")
    find = False
    for transport in transport_list:
        if transport.carry_digit() <= carrying_input:
            transport.info()
            find = True
    if find == False:
        print("Транспорт не найден")