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
    def __init__(self, c, x1, y1, x2, y2, radius, color="white"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.radius = radius
        self.c = c
        # coeff_radius можно придумать что-нибудь интереснее
        self.coeff_radius = radius/5
        self.ball = c.create_oval(self.x1, self.y1, self.x2, self.y2, fill=color, outline='white', width=2)

    def move_ball(self):
        # Отпринтовка координат шара
        # print(c.coords(self.ball)[3])
        if c.coords(self.ball)[3] < 300:
            c.move(self.ball, 0, 9)
            c.after(1000//60, self.move_ball)
        elif 300 <= c.coords(self.ball)[3] < 600:
            c.move(self.ball, 0, self.coeff_radius)
            c.after(1000//60, self.move_ball)

        #TODO если координата 600, сделать отскакивание
        #Добавьте учёт инерции частиц в зависимости от их массы.

def esc(event):
    root.destroy()

root.bind('<Escape>', esc)


# Создание мячей 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
r1 = 20
ball1 = Ball(c, 100 - r1, 120 - r1, 100 + r1, 120 + r1, r1, color="#a0a0a0")
ball1.move_ball()

r2 = 30
ball2 = Ball(c, 200 - r2, 120 - r2, 200 + r2, 120 + r2, r2, color="#a0a0a0")
ball2.move_ball()

r3 = 10
ball2 = Ball(c, 300 - r3, 120 - r3, 300 + r3, 120 + r3, r3, color="#a0a0a0")
ball2.move_ball()

r4 = 35
ball2 = Ball(c, 400 - r4, 120 - r4, 400 + r4, 120 + r4, r4, color="#a0a0a0")
ball2.move_ball()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


root.mainloop()