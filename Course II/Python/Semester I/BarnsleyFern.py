from tkinter import Tk, Canvas
import random


def f1(x, y):
    x = 0
    y = 0.16 * y
    return x, y


def f2(x, y):
    x = 0.85 * x + 0.04 * y
    y = -0.04 * x + 0.85 * y + 1.6

    return x, y


def f3(x, y):
    x = 0.20 * x - 0.26 * y
    y = 0.23 * x + 0.22 * y + 1.6

    return x, y


def f4(x, y):
    x = -0.15 * x + 0.28 * y
    y = 0.26 * x + 0.24 * y + 0.44

    return x, y


def esc(event):
    root.destroy()


root = Tk()
root.bind('<Escape>', esc)

W = 1200  # ширина
H = 800  # высота
size = random.choice([0.4, 0.6, 1, 1.5, 2.2])  # размер листа

c = Canvas(root, width=W, height=H, bg='black')
c.pack()


def main():
    x = 0
    y = 0
    flag = 0 # (0, 1)
    for _ in range(200):
        if flag == 0:
            c.create_oval(W/2+(55*size*x), H - (35*size*y), W/2 +
                        (55*size*x), H - (35*size*y), width=0, fill='green')
        elif flag == 1:
            c.create_oval(W/2-(55*size*x), H - (35*size*y), W/2 -
                        (55*size*x), H - (35*size*y), width=0, fill='green')

        rand = random.random()
        if rand < 0.1:
            x, y = f1(x, y)
        elif rand < 0.86:
            x, y = f2(x, y)
        elif rand < 0.93:
            x, y = f3(x, y)
        else:
            x, y = f4(x, y)

    root.after(1000//30, main)


if __name__ == "__main__":
    main()
    root.mainloop()
