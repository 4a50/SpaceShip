from tkinter import *
import indicatorWidgetsLib
import time
win = Tk()
size = 600


g1 = indicatorWidgetsLib.Gauge1(win, size,"Engine Total Power", "Power")
print ("g1:", g1.win)
g1.gaugeTextStr = ""
g2 = indicatorWidgetsLib.Gauge1(win, size, "Engine OverSpeed", "Boost")
hgt = int(size / 18.75) + 1 
msg = indicatorWidgetsLib.MessageLogger(win, hgt, 30)
msg.addMessage("[0001] This is a test to see if this stuff works! ")


print (hgt)
for i in range(0, 400):
    g1.updateValue((i / 4))
    g2.updateValue(i + 20)
    time.sleep(.05)
# logger.pop(0)
# messLog.set(logger)
win.mainloop()