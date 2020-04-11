import classProgression, classGeoArif
from random import randint
def main():
    try:
        n = int(input("Кол-во прогрессий = "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    d = {
        1: classGeoArif.Arithmetic,
        2: classGeoArif.Geometric
    }
    prog_list = []

    for _ in range(n):
        d_args = {
            1: [randint(-1000, 1000), randint(-1000, 1000), randint(1, 10)],
            2: [randint(-1000, 1000), randint(-1000, 1000)],
        }
        r = randint(1, 2)
        prog_list.append(d[r](*d_args[r]))

    for prog in prog_list:
        prog.info()