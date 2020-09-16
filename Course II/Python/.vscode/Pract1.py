import tkinter as tk
import math


def objMove(obj, data):
    """Перемещение объекта"""
    x1, y1, x2, y2 = newPosition(data)
    c.coords(obj, x1, y1, x2, y2)


def anime():
    # перемещение точки - угол += угловая скорость
    point_figure[4] += point_figure[5]
    objMove(redOval, point_figure)

    # анимация в 1мс
    root.after(1, anime)


def newPosition(data):
    """Высчитывание новой позиции объекта"""
    pos_x, pos_y, radius, distance, angle, _ = data

    x = pos_x - distance * math.sin(math.radians(-angle))
    y = pos_y - distance * math.cos(math.radians(-angle))

    # Координаты овала
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius

    return x1, y1, x2, y2


if __name__ == "__main__":

    width = 600
    height = 600
    pos_x = width // 2
    pos_y = height // 2

    # [центр x, центр y, радиус, расстояние от центра, текущий угол, угловая скорость]
    main_figure = [pos_x, pos_y, 200, 0, 0, 0]
    point_figure = [pos_x, pos_y, 10, 200, 0, 1]

    root = tk.Tk()
    c = tk.Canvas(root, width=width, heigh=height)
    c.pack()

    # Создание объектов
    x1, y1, x2, y2 = newPosition(main_figure)
    greenOval = c.create_oval(x1, y1, x2, y2, fill="green")
    x1, y1, x2, y2 = newPosition(point_figure)
    redOval = c.create_oval(x1, y1, x2, y2, fill="red")

    anime()
    root.mainloop()