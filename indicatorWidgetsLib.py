from tkinter import *
import numpy
import math
import time
class Gauge1:
    def __init__(self):
        self.win = Tk()
        self.win.title("Indicator Panel Widgets")
        
        #180 degree indicator
        
        self.scanvSize = 200
        self.canvX = canvSize
        self.canvY = canvSize
        self.x = canvX / 2
        self.y = canvY /2
        self.centerxy = x, y
        self.needleRadius = x * .60
        self.needleangle = 0
        self.gaugeWidth = canvX * .15
        self.canvEdgeUL = 0.2
        self.canvEdgeBR = .8
        self.arcCoordx0 = canvX * canvEdgeUL
        self.arcCoordy0 = canvY * canvEdgeUL
        self.arcCoordx1 = canvX * canvEdgeBR
        self.arcCoordy1 = canvY * canvEdgeBR
        self.arcCoords = arcCoordx0, arcCoordy0, arcCoordx1, arcCoordy1
        self.frameIndicator = LabelFrame(self.win, labelanchor='n',text="240 Degree Radial Indicator", bd=2 )
        self.ind1Canv = Canvas(frameIndicator, height=self.canvY, width=self.canvX, bd=5, bg="black")
        self.ind1Canv.pack()
        self.frameIndicator.pack()

    #TODO: Figure the equation to move a needle along an ellipse 
    #TODO: Allow customization of the green, yellow, and red

        self.yellowSeg = ind1Canv.create_arc(arcCoords, start=359,
        extent=119,width=gaugeWidth, outline="#e3ca09", style=ARC)
        self.redSeg = ind1Canv.create_arc(arcCoords, start=300,
        extent=59,width=gaugeWidth, outline="red", style=ARC)
        self.GreenSeg = ind1Canv.create_arc(arcCoords, start=118,
        extent=122,width=gaugeWidth, outline="green", style=ARC)
        self.indCenterLine = ind1Canv.create_arc(arcCoords, start=300, extent=300, width=2, style=ARC, outline='white')
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
        
            self.needlePos = ind1Canv.create_line(centerxy, x + (needleRadius * math.cos(math.radians(needleangle))), y + (needleRadius * math.sin(math.radians(needleangle))) , width=gaugeWidth * .1, 
            fill='#e36409', arrow=LAST)
            percentage = 0
            gaugeTextStr = str(percentage) + "\n%"
            displayText = ind1Canv.create_text(x, y * 1.7, text=gaugeTextStr, fill="white")
    def updateValue (self, percentage)
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