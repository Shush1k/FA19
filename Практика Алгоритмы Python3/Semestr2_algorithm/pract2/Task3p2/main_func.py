import classTriangle
from classRectangularTriangle import RectangularTriangle
from classIsoscelesTriangle import IsoscelesTriangle
from classEquilateralTriangle import EquilateralTriangle
from random import randint
def main():
    try:
        n = int(input("Количество треугольников = "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    triangle_list = []
    d = {
        1: classTriangle.Triangle,
        2: RectangularTriangle,
        3: IsoscelesTriangle,
        4: EquilateralTriangle
    }

    for _ in range(n):
        r = randint(1, 4)
        d_val = [randint(1, 100), randint(1, 100), randint(1, 100)]
        triangle_list.append(d[r](*d_val))
    for triangle in triangle_list:
        triangle.info(type(triangle).__name__)