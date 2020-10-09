import tkinter as tk
import math

WIDTH = 600
HEIGHT = 600
center_x = WIDTH / 2
center_y = HEIGHT / 2
angle = 0
angle_sin = 0

R = 200
r = 10

shag = 0.1
shag_sin = 6
speed = 0.6

root = tk.Tk()
c = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
c.pack()

ball = c.create_oval(center_x - R, center_y - R, center_x + R, center_y + R, fill='orange')
small_ball = c.create_oval(center_x - r - R, center_y - r, center_x + r - R, center_y + r, fill='black')

def get_middle(x1, x2):
    return abs(x1+x2)/2

def motion(): 
    global angle, angle_sin, speed
    
    if angle >= 360:
        angle = 0
    if angle_sin >= 360:
        angle_sin = 0
        
    x1 = center_x -(math.sin(math.radians(angle)) * R * (math.cos(math.radians(angle_sin)) + 5)/(5)) - r
    x2 = center_x -(math.sin(math.radians(angle)) * R * (math.cos(math.radians(angle_sin)) + 5)/(5)) + r
    y2 = center_y +(math.cos(math.radians(angle)) * R * (math.cos(math.radians(angle_sin)) + 5)/(5)) + r
    y1 = center_y +(math.cos(math.radians(angle)) * R * (math.cos(math.radians(angle_sin)) + 5)/(5)) - r

    c.coords(small_ball, x1, y1, x2, y2)
    x_cen = get_middle(x1, x2)
    y_cen = get_middle(y1, y2)

    c.create_oval(x_cen-1, y_cen-1, x_cen+1, y_cen+1, fill = "blue", outline = "blue")
    angle += shag
    angle_sin += shag_sin
    root.after(1000//60, motion)


motion() 
root.mainloop()
