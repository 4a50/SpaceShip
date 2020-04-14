from tkinter import *
import cmath
import time
def Main():
    gridYes = True
    gridInterval = 50
    win = Tk()
    win.title("Indicator Panel Widgets")
    
    
    #180 degree indicator
    
    
    canvX = 400
    canvY = 400
    guageWidth = canvX * .15
    startArc = 0
    extentArc = 60
    canvEdgeUL = 0.1
    canvEdgeBR = .9
    frameIndicator = LabelFrame(win, labelanchor='n',text="180 Degree Radial Indicator", bd=2 )
    ind1Canv = Canvas(frameIndicator, height=canvY, width=canvX, bd=5)
    ind1Canv.pack()
    frameIndicator.pack()
    
    if gridYes == True:
        for i in range(0, canvX, gridInterval):
            ind1Canv.create_line(0,i, canvX, i)
            ind1Canv.create_line(i,0,i, canvY,)

    
    
    
    
    #ind1Canv.create_arc(0, 0, 100, 100, width=6,start=0,extent=180)
    seg1 = ind1Canv.create_arc(canvX * canvEdgeUL, canvY * canvEdgeUL, canvX * canvEdgeBR, canvY * canvEdgeBR, start=startArc, 
    extent=-60,width=guageWidth, outline="red", style=ARC, fill="grey")
    ind1Canv.update()
    seg2 = ind1Canv.create_arc(canvX * canvEdgeUL, canvY * canvEdgeUL, canvX * canvEdgeBR, canvY * canvEdgeBR, start=startArc+60, 
    extent=-60,width=guageWidth, outline="green", style=ARC)
    ind1Canv.update()
    seg3 = ind1Canv.create_arc(canvX * canvEdgeUL, canvY * canvEdgeUL, canvX * canvEdgeBR, canvY * canvEdgeBR, start=startArc+120,
    extent=-60,width=guageWidth, outline="blue", style=ARC)
    ind1Canv.update()
    seg4 = ind1Canv.create_arc(canvX * canvEdgeUL, canvY * canvEdgeUL, canvX * canvEdgeBR, canvY * canvEdgeBR, start=startArc+180,
    extent=-60,width=guageWidth, outline="yellow", style=ARC)
    ind1Canv.update()
    seg5 = ind1Canv.create_arc(canvX * canvEdgeUL, canvY * canvEdgeUL, canvX * canvEdgeBR, canvY * canvEdgeBR, start=startArc+240,
    extent=-60,width=guageWidth, outline="orange", style=ARC)
    ind1Canv.update()
    #seg6 = ind1Canv.create_arc(canvX * canvEdgeUL, canvY * canvEdgeUL, canvX * canvEdgeBR, canvY * canvEdgeBR, start=startArc+300,
    #extent=-60, width=guageWidth, outline="pink", style=ARC)
    #ind1Canv.update()
    
    
    
    win.mainloop()


if __name__ == '__main__':
    Main()