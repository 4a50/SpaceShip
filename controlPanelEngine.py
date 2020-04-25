from tkinter import *
import indicatorWidgetsLib
import time
win = Tk()
size = 400


g1 = indicatorWidgetsLib.Gauge1(win, size,"Engine Total Power", "Power")

m1 = indicatorWidgetsLib.vertMeter1(win, size, "Tank A")

indicatorTitle = ["H1", "H2", "H3", "H4", "H5", "H6"]
ind1 = indicatorWidgetsLib.IndLights(win, 200, "Hatch Status", indicatorTitle, len(indicatorTitle) )
m1.TestMeter()
g1.testGauge()


# logger.pop(0)
# messLog.set(logger)
win.mainloop()