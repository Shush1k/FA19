import classFigure 
import classRectangle
import classCircle
import classTriangle
from math import pi, sqrt
from random import randint

"""
# Вариант который работает
person1 = classRectangle.Rectangle(3, 4) # вид: module.class_name(args)
person1.get_square()
person1.get_perimeter()
person1.info("Rectangle")
"""

# Это типо класс Прямоугольника
figure1 = classRectangle.Rectangle(3, 4)
figure1.get_square()
figure1.get_perimeter()
figure1.info("Rectangle")

# Это типо класс Треугольника
figure2 = classTriangle.Triangle(3, 4, 5)
figure2.check()
figure2.get_square()
figure2.get_perimeter()
figure2.info("Triangle")

# Это типо класс Круга
figure2 = classCircle.Circle(4)
figure2.get_square()
figure2.get_perimeter()
figure2.info("Circle")
"""
def main():
    try:
        n = int(input("Количество фигур = "))
    except ValueError:
        print("0_0 упс...")
        return

    d = {
        1: Rectangle,
        2: Circle,
        3: Triangle
    }
    figures_list = []

    for _ in range(n):

        d_val = {
            1: [randint(1, 100), randint(1, 100)],
            2: [randint(1, 100)],
            3: [randint(1, 100), randint(1, 100), randint(1, 100)]
        }

        r = randint(1, 3)
        figures_list.append(d[r](*d_val[r]))

    for figure in figures_list:
        figure.info(type(figure).__name__)
"""
