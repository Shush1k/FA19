from tkinter import *
from math import *
import time
root = Tk()
root.title("Спираль_Архимеда")
c = Canvas(root, width = 600, height = 600, bg = "orange")
c.pack()
radius = 10; Radius = 200
center_1 = 300; center_2 = 300
c.create_oval(center_1-Radius, center_2 -Radius, center_1+Radius, center_2+ Radius, fill = "green")
m_p = c.create_oval(center_1-radius, center_2 -radius, center_1+radius, center_2+ radius, fill = "red")
iteration_g = 0; scale_a = 9; num_of_step = 1000

def motion():
    global iteration_g; global scale_a; global num_of_step
    fi_1 = pi*iteration_g/num_of_step; fi_2 = pi*(iteration_g+1)/num_of_step
    r_1 = scale_a * fi_1; r_2 = scale_a * fi_2
    c.move(m_p, r_2*cos(fi_2)-r_1*cos(fi_1), r_2*sin(fi_2)- r_1*sin(fi_1))
    c.create_line(center_1+r_1*cos(fi_1), center_2 +r_2*sin(fi_1), center_1 +r_2*cos(fi_2), center_2+r_2*sin(fi_2), fill ="orange")
    if iteration_g < 7000:
        root.after(1, motion)
    iteration_g += 1

motion()
root.mainloop()