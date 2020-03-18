import classFigure, classRectangle, classCircle, classTriangle 
from random import randint
def main():
    try:
        n = int(input("Количество фигур = "))
    except ValueError:
        print("0_0 упс...")
        return
    d = {1: classRectangle.Rectangle, 2: classCircle.Circle, 3: classTriangle.Triangle}
    figures_list = []
    for _ in range(n):
        d_val = {1: [randint(1, 100), randint(1, 100)], 2: [randint(1, 100)], 3: [randint(1, 100), randint(1, 100), randint(1, 100)]}

        r = randint(1, 3)
        figures_list.append(d[r](*d_val[r]))
    for figure in figures_list:
        figure.info(type(figure).__name__)