from tkinter import *
import cmath
import time
def Main():
    gridYes = False
    gridInterval = 50
    win = Tk()
    win.title("Indicator Panel Widgets")
    
    
    #180 degree indicator
    
    
    canvX = 400
    canvY = 400
    guageWidth = canvX * .15
    startArc = 0
    canvEdgeUL = 0.2
    canvEdgeBR = .8
    arcCoord = canvX * canvEdgeUL, canvY * canvEdgeUL, canvX * canvEdgeBR, canvY * canvEdgeBR
    frameIndicator = LabelFrame(win, labelanchor='n',text="240 Degree Radial Indicator", bd=2 )
    ind1Canv = Canvas(frameIndicator, height=canvY, width=canvX, bd=5)
    ind1Canv.pack()
    frameIndicator.pack()
    
    if gridYes == True:
        for i in range(0, canvX, gridInterval):
            ind1Canv.create_line(0,i, canvX, i)
            ind1Canv.create_line(i,0,i, canvY,)

    
    
    
    
    #ind1Canv.create_arc(0, 0, 100, 100, width=6,start=0,extent=180)
   
    
    redSeg = ind1Canv.create_arc(arcCoord, start=300,
    extent=120,width=guageWidth, outline="red", style=ARC)
    yellowSeg = ind1Canv.create_arc(arcCoord, start=startArc+1,
    extent=119,width=guageWidth, outline="yellow", style=ARC)
    GreenSeg = ind1Canv.create_arc(arcCoord, start=startArc+120,
    extent=120,width=guageWidth, outline="green", style=ARC)
    needleCenter = ind1Canv.create_arc(arcCoord, start=0, extent=359, width=2)
    ind1Canv.update()
    
    
    # for i in range(0, 60, 6):
    #     ind1Canv.create_arc(canvX * canvEdgeUL, canvY * canvEdgeUL, canvX * canvEdgeBR, canvY * canvEdgeBR, start=startArc+(240 - i), 
    #     extent=-1, width=guageWidth/2, style=ARC, outline="black")
    #     ind1Canv.create_arc(canvX * canvEdgeUL, canvY * canvEdgeUL, canvX * canvEdgeBR, canvY * canvEdgeBR, start=startArc+ (180 - i),
    #     extent=-1,width=guageWidth/2, style=ARC)
    #     ind1Canv.create_arc(canvX * canvEdgeUL, canvY * canvEdgeUL, canvX * canvEdgeBR, canvY * canvEdgeBR, start=startArc+ (120 - i),
    #     extent=-1,width=guageWidth/2, style=ARC)
    #     ind1Canv.create_arc(canvX * canvEdgeUL, canvY * canvEdgeUL, canvX * canvEdgeBR, canvY * canvEdgeBR, start=startArc+ (60 - i),
    #     extent=-1,width=guageWidth/2, style=ARC)
    #     time.sleep(.25) 
    #     if (i == 0):
    #         ind1Canv.create_arc(canvX * canvEdgeUL, canvY * canvEdgeUL, canvX * canvEdgeBR, canvY * canvEdgeBR, start=(startArc),
    #         extent=-1,width=guageWidth/2, style=ARC)
    #     else:
    #         ind1Canv.create_arc(canvX * canvEdgeUL, canvY * canvEdgeUL, canvX * canvEdgeBR, canvY * canvEdgeBR, start=(startArc - i),
    #         extent=-1,width=guageWidth/2, style=ARC)
    #     ind1Canv.update()
    
    
    
    
    win.mainloop()


if __name__ == '__main__':
    Main()