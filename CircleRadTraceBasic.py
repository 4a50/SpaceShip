import time
import math
from tkinter import *

deg = 90
radius = 13
win = Tk()
x = 200 + (100 * math.cos(deg))
y = 200 + (100 * math.sin(deg))
canv1 = Canvas(win, height=400, width=400)
canv1.update()
canv1.create_oval(100,100, 300, 300)
canv1.create_line(200, 200, 200, 100)
meterLine = canv1.create_line(200, 200, x, y, fill="red")
print("x:", x, "y:", y)
print (meterLine)
canv1.pack()
for q in range(10):
    for i in range(0, 360):
        deg = math.radians(i)
        x = 200 + (100 * math.cos(deg))
        y = 200 + (100 * math.sin(deg))
        canv1.coords(meterLine, (200, 200, x, y))
        time.sleep(.02)
        canv1.update()
        print("i:", i, "x:", x, "y:", y, "COS deg:", math.cos(deg), "SIN deg:", math.sin(deg))


win.mainloop()

