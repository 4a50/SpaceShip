from tkinter import *
import cmath
import math
import time
def Main():
    gridYes = False
    gridInterval = 50
    win = Tk()
    win.title("Indicator Panel Widgets")
    
    
    #180 degree indicator
    
    
    canvX = 400
    canvY = 400
    x = canvX / 2
    y = canvY /2
    centerxy = x, y
    needleRadius = x * .4
    needleangle = 90
    print ("Needle Angle Radians:", math.radians(needleangle))
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

    #TODO: Figure the equation to move a needle along an ellipse 
    
    yellowSeg = ind1Canv.create_arc(arcCoord, start=359,
    extent=119,width=guageWidth, outline="yellow", style=ARC)
    redSeg = ind1Canv.create_arc(arcCoord, start=300,
    extent=59,width=guageWidth, outline="red", style=ARC)
    time.sleep(1)
    ind1Canv.update()
    GreenSeg = ind1Canv.create_arc(arcCoord, start=startArc+118,
    extent=122,width=guageWidth, outline="green", style=ARC)
    IndCenterLine = ind1Canv.create_arc(arcCoord, start=300, extent=300, width=2, style=ARC)
    ind1Canv.update()

    Needle_line = ind1Canv.create_line(centerxy, needleRadius * math.cos(needleangle), needleRadius * math.sin(needleangle))
    print (needleRadius * math.cos(needleangle), (needleRadius * math.sin(needleangle)))

    
    
    # for i in range(0, 60, 6)
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