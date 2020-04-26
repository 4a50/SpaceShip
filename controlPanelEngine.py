from tkinter import *
import indicatorWidgetsLib
import time

win = Tk()
win.configure(bg='black')
size = 400


#objInits
g1 = indicatorWidgetsLib.Gauge1(win, size,"Engine Total Power", "Power")
m1 = indicatorWidgetsLib.vertMeter1(win, size, "Tank A")
indicatorTitle = ["Mag Field", "Charge Sync", "Fuel Pump"] #, "H4", "H5", "H6"]
indicatorTitle2 = ["H1", "H2", "H3", "H4", "H5", "H6"]
indVert = indicatorWidgetsLib.IndLights(win, size, "Hatch", indicatorTitle2, False )
indHoriz = indicatorWidgetsLib.IndLights(win, size, "VASIMIR Flow Status ", indicatorTitle, True )
dockingClamps = indicatorWidgetsLib.IndLights(win, size, "Docking Clamps", ['FWD', 'AFT', 'PORT', 'STBD', 'UP', 'LOW'], True )
msg1 = indicatorWidgetsLib.MessageLogger(win, 21,25)

#setPos in window
g1.setPosFrame(row=0, column=2, rowspan=2)
indVert.setPosFrame(row=0, column=3, rowspan=2)
m1.setPosFrame(row=0, column=0, rowspan=2)
indHoriz.setPosFrame(row=0, column=1)
dockingClamps.setPosFrame(row=1, column=1)
msg1.setPosFrame(row=0, column=4, rowspan=2)

win.mainloop()