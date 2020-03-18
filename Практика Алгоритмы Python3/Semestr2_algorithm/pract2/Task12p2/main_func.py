import classBody, classParallelepiped, classPyramid
from random import randint
def main():
    try:
        n = int(input("Количество фигур = "))
    except ValueError:
        print("0_0 упс...")
        return
    d = {
        1: classParallelepiped.Parallelepiped,
        2: classParallelepiped.Ball,
        3: classPyramid.Pyramid
    }
    figures_list = []
    for _ in range(n):
        d_args = {
            1: [randint(1, 100), randint(1, 100), randint(1, 100)],
            2: [randint(1, 100)],
            3: [randint(1, 100), randint(1, 100), randint(1, 100)],
        }
        r = randint(1, 3)
        figures_list.append(d[r](*d_args[r]))

    for figure in figures_list:
        figure.info(type(figure).__name__)