import tkinter as tk
from random import randint

class Raindrop:
    def __init__(self, canvas, width, height, x, y, yspeed, length, color="blue"):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.yspeed = yspeed
        self.length = length
        self.line = canvas.create_line(self.x, self.y+self.length, self.x, self.y, fill=color)
        

    def moving(self):
        self.y += self.yspeed
        self.canvas.move(self.line, 0, self.yspeed)

        # Если выходит за границы canvas
        if self.y > self.height:
            self.canvas.move(self.line, 0, -(self.height+self.length))
            self.y -= self.height + self.length

def redraw():
    for drop in drops:
        drop.moving()

    root.after(10, redraw)


root = tk.Tk()
width = 600
height = 600
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

drops = [Raindrop(canvas, width, height, x=randint(0, width), y=randint(0, height), yspeed=randint(2, 2), length=randint(9, 18)) for i in range(100)]
redraw()

root.mainloop()