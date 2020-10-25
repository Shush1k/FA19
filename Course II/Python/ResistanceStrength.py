"""
Реализуйте систему разноразмерных частиц, имеющих одинаковую вертикальную скорость. При прохождении границы сред частицами должны испытывать сопротивление.
Реализуйте более физически достоверную модель сопротивления, зависящего от размера частицы.
Добавьте учёт инерции частиц в зависимости от их массы.
"""
import tkinter as tk


root = tk.Tk()
root.title("Силы Сопротивления")
width = 600
height = 600
c = tk.Canvas(root, width=width, height=height, bg="black")
c.pack()
c.create_rectangle(0, height//2, width+2, height+2, fill='grey')

class Ball:

    def __init__(self, c, x1, y1, x2, y2, radius, mass, color="white"):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.radius = radius
        self.c = c

        # Формула лобового сопротивления
        # v - скорость, F_str = лобовое сопротивление, mass - масса, Acceleration - ускорение
        self.v = 3
        self.F_str = 0.47 * self.v**2 * radius
        self.mass = mass
        self.Acceleration = self.F_str / mass
        self.ball = c.create_oval(self.x1 - self.radius, self.y1 - self.radius, self.x2 +
                                  self.radius, self.y2 + self.radius, fill=color, outline='white', width=2)

    def move_ball(self):
        if c.coords(self.ball)[3] < 300:
            c.move(self.ball, 0, self.v)
            c.after(1000//60, self.move_ball)
        elif 300 <= c.coords(self.ball)[3] < 600:
            c.move(self.ball, 0, self.F_str*0.1)
            c.after(1000//60, self.move_ball)
        elif c.coords(self.ball)[3] >= 600:
            c.after(1000//60, self.iter_1)

    def iter_1(self):
        if c.coords(self.ball)[3] >= 585:
            c.move(self.ball, 0, -self.Acceleration)
            c.after(1000//60, self.iter_1)
        elif c.coords(self.ball)[3] <= 600:
            c.after(1000//60, self.iter_2)

    def iter_2(self):
        if c.coords(self.ball)[3] < 600:
            c.move(self.ball, 0, self.Acceleration)
            c.after(1000//60, self.iter_2)
        else:
            c.after(1000//60, self.iter_3)

    def iter_3(self):
        if c.coords(self.ball)[3] >= 595:
            c.move(self.ball, 0, -self.Acceleration)
            c.after(1000//60, self.iter_3)
        elif c.coords(self.ball)[3] <= 600:
            c.after(1000//60, self.iter_stop)

    def iter_stop(self):
        if c.coords(self.ball)[3] + self.Acceleration < 600:
            c.move(self.ball, 0, self.Acceleration)
            c.after(1000//60, self.iter_stop)

        else:
            # Конечная координата частицы равна 601
            c.move(self.ball, 0, 601 -c.coords(self.ball)[3])

def esc(event):
    root.destroy()

root.bind('<Escape>', esc)


# Создание частиц
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
r1 = 20
mass1 = 25
ball1 = Ball(c, 100, 120, 100,
             120, r1, mass1, color="#a0a0a0")
ball1.move_ball()

r2 = 30
mass2 = 35
ball2 = Ball(c, 200, 120, 200,
             120, r2, mass2, color="#a0a0a0")
ball2.move_ball()

r3 = 10
mass3 = 15
ball2 = Ball(c, 300, 120, 300,
             120, r3, mass3, color="#a0a0a0")
ball2.move_ball()

r4 = 36
mass4 = 20
ball2 = Ball(c, 400, 120, 400,
             120, r4, mass4, color="#a0a0a0")
ball2.move_ball()

r5 = 15
mass5 = 14
ball2 = Ball(c, 530, 120, 530,
             120, r5, mass5, color="#a0a0a0")
ball2.move_ball()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


root.mainloop()