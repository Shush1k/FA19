import tkinter as tk
import math

def getPos(data):
    """Получаем координаты"""
    x_pos, y_pos, radius, distance, angle, _ = data

    x = x_pos - distance * math.sin(math.radians(-angle))
    y = y_pos - distance * math.cos(math.radians(-angle))

    # Вычисление координат овала
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius

    return x1, y1, x2, y2
def objMove(obj, data):
    """Перемещение объекта(смена координат)"""
    x1, y1, x2, y2 = getPos(data)
    c.coords(obj, x1, y1, x2, y2)


def anime():
    point_figure[4] += point_figure[5]
    objmove(point_oval,point_figure)
    
    root.after(1, anime)

if __name__ == "__main__":
    root = tk.Tk()
    c = tk.Canvas(root, width=600, height=600, bg="white")
    c.pack()

    x1 = 600//2
    y1 = 600//2

    #[центр x, центр y, радиус, расстояние от центра, текущий угол, угловая скорость]
    main_figure = [x1, y1, 200, 0, 0, 0]
    point_figure = [x1, y1, 10, 200, 0, 0.5]
    #Создание объектов(круг и точка)
    x1, y1, x2, y2 = getPos(main_figure)
    main_oval = c.create_oval(x1, y1, x2, y2, fill="orange")

    x1, y1, x2, y2 = getPos(point_figure)
    point_oval = c.create_oval(x1, y1, x2, y2, fill = "black")

    anime()
    root.mainloop()