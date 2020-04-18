from tkinter import *
import numpy
import math
import time
def Main():
    gridYes = False
    gridInterval = 50
    win = Tk()
    win.title("Indicator Panel Widgets")
    
    #180 degree indicator
    
    canvSize = 200
    canvX = canvSize
    canvY = canvSize
    x = canvX / 2
    y = canvY /2
    centerxy = x, y
    needleRadius = x * .60
    needleangle = 0
    gaugeWidth = canvX * .15
    canvEdgeUL = 0.2
    canvEdgeBR = .8
    arcCoordx0 = canvX * canvEdgeUL
    arcCoordy0 = canvY * canvEdgeUL
    arcCoordx1 = canvX * canvEdgeBR
    arcCoordy1 = canvY * canvEdgeBR
    arcCoords = arcCoordx0, arcCoordy0, arcCoordx1, arcCoordy1
    frameIndicator = LabelFrame(win, labelanchor='n',text="240 Degree Radial Indicator", bd=2 )
    ind1Canv = Canvas(frameIndicator, height=canvY, width=canvX, bd=5, bg="black")
    ind1Canv.pack()
    frameIndicator.pack()
    
    if gridYes == True:
        for i in range(0, canvX, gridInterval):
            ind1Canv.create_line(0,i, canvX, i)
            ind1Canv.create_line(i,0,i, canvY,)

    #TODO: Figure the equation to move a needle along an ellipse 
    
    yellowSeg = ind1Canv.create_arc(arcCoords, start=359,
    extent=119,width=gaugeWidth, outline="#e3ca09", style=ARC)
    redSeg = ind1Canv.create_arc(arcCoords, start=300,
    extent=59,width=gaugeWidth, outline="red", style=ARC)
    GreenSeg = ind1Canv.create_arc(arcCoords, start=118,
    extent=122,width=gaugeWidth, outline="green", style=ARC)
    indCenterLine = ind1Canv.create_arc(arcCoords, start=300, extent=300, width=2, style=ARC, outline='white')
    print ("gaugeWidth", gaugeWidth)
    # Tick Marks
    for i in range(0, 330, 30):
        startArc = 240 - i
        if startArc == 0:
            startArc = 359
            print ("If Statement Reached")
        if startArc == -60:
            startArc += 2
        ind1Canv.create_arc(arcCoords, start=startArc, extent=-2,width=gaugeWidth*.70, outline="white", style=ARC)
        print (startArc)
    tickSpacing = 3
    if (gaugeWidth * .2) <= 6:
        tickSpacing = 6
        print("Tickspacing set to six")
    for i in range(0, 300, tickSpacing):
        print ("inner tick width", gaugeWidth * .2)
        startArc = 240 - i
        if startArc == 0:
            startArc = 359
        if startArc == -60:
            startArc += 2
        ind1Canv.create_arc(arcCoords, start=startArc, extent=-1,width=gaugeWidth * .2, outline="white", style=ARC)
        print (startArc)
    
    needlePos = ind1Canv.create_line(centerxy, x + (needleRadius * math.cos(math.radians(needleangle))), y + (needleRadius * math.sin(math.radians(needleangle))) , width=gaugeWidth * .1, 
    fill='#e36409', arrow=LAST)
    percentage = 0
    gaugeTextStr = str(percentage) + "\n%"
    displayText = ind1Canv.create_text(x, y * 1.7, text=gaugeTextStr, fill="white")
    for i in range(0, 101, 1):
        percentage = (i * 3) + 120
        needleangle = percentage
        if i >=360:
            needleangle-= 360
        ind1Canv.coords(needlePos, x, y, x + (needleRadius * math.cos(math.radians(needleangle))), y + (needleRadius * math.sin(math.radians(needleangle))))    
        print ("Percentage:", i)
        gaugeTextStr = str(i) + "\n%"
        ind1Canv.itemconfigure(displayText, font=('Times', str(int(canvSize / 13)), 'bold'), text=gaugeTextStr)
        ind1Canv.update()
        time.sleep(.05)    
    win.mainloop()


if __name__ == '__main__':
    Main()