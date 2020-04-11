import classTriangle
import classRectangularTriangle as RTclass
import classIsoscelesTriangle as ITclass
import classEquilateralTriangle as ETclass
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
        2: RTclass.RectangularTriangle,
        3: ITclass.IsoscelesTriangle,
        4: ETclass.EquilateralTriangle
    }

    for _ in range(n):
        r = randint(1, 4)
        d_val = [randint(1, 100), randint(1, 100), randint(1, 100)]
        triangle_list.append(d[r](*d_val))
    for triangle in triangle_list:
        triangle.info(type(triangle).__name__)