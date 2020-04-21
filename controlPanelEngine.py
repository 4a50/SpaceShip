from tkinter import *
import indicatorWidgetsLib
import time
win = Tk()
size = 600


# g1 = indicatorWidgetsLib.Gauge1(win, size,"Engine Total Power", "Power")
# print ("g1:", g1.win)
# g1.gaugeTextStr = ""
# g2 = indicatorWidgetsLib.Gauge1(win, size, "Engine OverSpeed", "Boost")
# hgt = int(size / 18.75) + 1 
# msg = indicatorWidgetsLib.MessageLogger(win, hgt, 30)
# msg.addMessage("[0001] This is a test to see if this stuff works! ")
m1 = indicatorWidgetsLib.vertMeter1(win, 400, "Mono\n Tank A")
m1.TestMeter()


# logger.pop(0)
# messLog.set(logger)
win.mainloop()