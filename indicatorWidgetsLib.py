from tkinter import *
import numpy
import math
import time

class MessageLogger():
    def __init__(self, win, msgBoxHeight, msgBoxWidth):
        self.win = win
        self.messLog = StringVar()
        self.logger = []
        self.msgBoxHeight = msgBoxHeight
        self.msgBoxWidth = msgBoxWidth
        self.messageFrame = LabelFrame(self.win, labelanchor='n',font=('Times', 20, 'italic'), text="Message Readout", bd=2 )
        self.messageBox = Listbox(self.messageFrame, height=self.msgBoxHeight, width= self.msgBoxWidth, font=18, bg='black', fg='#75B676', listvariable=self.messLog).pack(fill=Y)
        self.messageFrame.pack(side = LEFT)    
    def addMessage(self, addmsg):
        self.logger.append(addmsg)
        self.messLog.set(self.logger)

class Gauge1():
    def __init__(self, win, canvSize, gaugeTitle="Equiment Gauge", gaugeNomen="No name Specified"):
        self.canvSize = canvSize
        self.canvX = self.canvSize
        self.canvY = self.canvSize
        self.x = self.canvX / 2
        self.y = self.canvY /2
        self.centerxy = self.x, self.y
        self.win = win
        self.gaugeNomen = gaugeNomen
        self.gaugeTitle=gaugeTitle     
        self.needleRadius = self.x * .60
        self.needleangle = 120
        self.gaugeWidth = self.canvX * .15
        self.canvEdgeUL = 0.2
        self.canvEdgeBR = .8
        self.arcCoordx0 = self.canvX * self.canvEdgeUL
        self.arcCoordy0 = self.canvY * self.canvEdgeUL
        self.arcCoordx1 = self.canvX * self.canvEdgeBR
        self.arcCoordy1 = self.canvY * self.canvEdgeBR
        self.arcCoords = self.arcCoordx0, self.arcCoordy0, self.arcCoordx1, self.arcCoordy1
        self.gaugeFrame = LabelFrame(self.win, labelanchor='n',font=('Times',  round(canvSize * .05), 'italic'), text=gaugeTitle, bd=2 )
        self.guageCanv = Canvas(self.gaugeFrame, height=self.canvY, width=self.canvX, bd=5, bg="black")
        self.messageList = []
        self.meterLevel = 40
    #TODO: Figure the equation to move a needle along an ellipse 
    #TODO: Allow customization of the green, yellow, and red
        self.yellowSeg = self.guageCanv.create_arc(self.arcCoords, start=359,
        extent=119,width=self.gaugeWidth, outline="#e3ca09", style=ARC)
        self.redSeg = self.guageCanv.create_arc(self.arcCoords, start=300,
        extent=59,width=self.gaugeWidth, outline="red", style=ARC)
        self.GreenSeg = self.guageCanv.create_arc(self.arcCoords, start=118,
        extent=122,width=self.gaugeWidth, outline="green", style=ARC)
        self.indCenterLine = self.guageCanv.create_arc(self.arcCoords, start=300, extent=300, width=2, style=ARC, outline='white')
        # Tick Marks
        for i in range(0, 330, 30):
            startArc = 240 - i
            if startArc == 0:
                startArc = 359
            if startArc == -60:
                startArc += 2
            self.guageCanv.create_arc(self.arcCoords, start=startArc, extent=-2,width=self.gaugeWidth*.70, outline="white", style=ARC)
        tickSpacing = 3
        if (self.gaugeWidth * .2) <= 6:
            tickSpacing = 6
        for i in range(0, 300, tickSpacing):
            startArc = 240 - i
            if startArc == 0:
                startArc = 359
            if startArc == -60:
                startArc += 2
            self.guageCanv.create_arc(self.arcCoords, start=startArc, extent=-1,width=self.gaugeWidth * .2, outline="white", style=ARC)
        
        self.needlePos = self.guageCanv.create_line(self.centerxy, self.x + (self.needleRadius * math.cos(math.radians(self.needleangle))), 
        self.y + (self.needleRadius * math.sin(math.radians(self.needleangle))) , width=self.gaugeWidth * .1, fill='#e36409', arrow=LAST)
        self.gaugeTextStr = "0\n" + self.gaugeNomen
        self.displayText = self.guageCanv.create_text(self.x, self.y * 1.7, text=self.gaugeTextStr, fill="white", justify=CENTER, font=('Times', str(int(self.canvSize / 13)), 'bold'))

        self.guageCanv.pack(side=LEFT)
        self.gaugeFrame.pack(side=LEFT)
    def updateValue (self, deflPercent=0):
            if deflPercent > 100:
                deflPercent = 100
            if deflPercent < 0:
                deflPercent = 0
            self.needleangle = (deflPercent * 3) + 120
            if self.needleangle >=360:
                self.needleangle-= 360
            self.guageCanv.coords(self.needlePos, self.x, self.y, self.x + (self.needleRadius * math.cos(math.radians(self.needleangle))), self.y + (self.needleRadius * math.sin(math.radians(self.needleangle))))    
            self.gaugeTextStr = str(deflPercent) + "\n" + self.gaugeNomen
            self.guageCanv.itemconfigure(self.displayText, font=('Times', str(int(self.canvSize / 13)), 'bold'), text=self.gaugeTextStr)
            self.guageCanv.update()
    def testGauge(self):
        for i in range(0, 201):
            self.updateValue((i / 2))
        self.updateValue()

class vertMeter1:
    def __init__(self, win, canvSize, meterTitle, red=90, yellow=60):
        self.win = win
        self.meterTitle=meterTitle
        self.canvSize = canvSize
        self.canvX = self.canvSize / 3
        self.canvY = self.canvSize
        self.x = self.canvX / 2
        self.y = self.canvY /2
        self.unitsDisc = "Percent"
        self.canvMinX = .4
        self.canvMinY = .15
        self.canvMaxX = .65
        self.canvMaxY = .85
        self.centerxy = self.x, self.y
        self.meterPixels = (self.canvMaxY * self.canvY) - (self.canvMaxX * self.canvX)
        print ("meterPixels: ", self.meterPixels)
        self.meterFrame = LabelFrame(self.win, labelanchor='n',font=('Times',  round(canvSize * .05), 'italic'), text=self.meterTitle, bd=2 ) #Changed from Font size 20
        self.meterCanv = Canvas(self.meterFrame, height=self.canvY, width=self.canvX, bd=5, bg="black")
        self.meterLevel = 40
        # Color Bands
        self.red = red
        self.yellow = yellow
        print ("self.y", self.y)
        

        print ("\n", self.canvX, self.canvY)
        print (self.canvX * self.canvMinX, self.canvY * self.canvMinY, self.canvX * self.canvMaxX, self.canvY * self.canvMaxY)
        
        #
        self.rectX0 = self.canvX * self.canvMinX
        self.rectY0 = self.canvY * self.canvMinY
        self.rectX1= self.canvX * self.canvMaxX
        self.rectY1 = self.canvY * self.canvMaxY
        self.meterPixels = (self.rectY1 - self.rectY0)
        print ("meter: ", self.meterPixels)
                
        self.meterCanv.create_rectangle(self.rectX0, self.rectY0, self.rectX1, self.rectY1, outline='white', fill='grey')
        self.meterIndication = self.meterCanv.create_rectangle(self.rectX0, self.rectY0 + self.meterLevel, self.rectX1, self.rectY1, outline='white', fill='red')
        triIndicatorPixelDist = 10
        
        self.rTriIndicator = self.meterCanv.create_polygon( self.rectX1, self.rectY0 + self.meterLevel,  self.rectX1 + triIndicatorPixelDist,(self.rectY0 + self.meterLevel) + triIndicatorPixelDist,  
        self.rectX1 + triIndicatorPixelDist,(self.rectY0 + self.meterLevel) - triIndicatorPixelDist, fill='white' )
        self.lTriIndicator = self.meterCanv.create_polygon( self.rectX0, self.rectY0 + self.meterLevel,  self.rectX0 - triIndicatorPixelDist,(self.rectY0 + self.meterLevel) + triIndicatorPixelDist,  
        self.rectX0 - triIndicatorPixelDist,(self.rectY0 + self.meterLevel) - triIndicatorPixelDist, fill='white' )
        floattostr = str(self.meterLevel)
        print (type(floattostr))
        self.indicatorNum = self.meterCanv.create_text ((self.rectX1 - (self.rectX1 - self.rectX0) /2), self.rectY1 + self.canvSize * .050, text=floattostr, fill='white', font=('Times', str(int(self.canvSize / 30)), 'bold')) # changed + 30

        bigTick = .033 * self.canvSize #20
        lilTick = .0166 * self.canvSize    #10
        xAxis = self.rectX1 + (self.rectX1 * .052)
        for i in range(101):
            offset = (self.meterPixels * (i / 100))
            print (offset, self.rectY1 - offset)
            if i == 0 or i % 10 == 0:
                self.meterCanv.create_line(xAxis, self.rectY1 - offset, xAxis + bigTick, self.rectY1 - offset, fill='orange')
                self.meterCanv.create_text(xAxis + bigTick+(self.canvSize * .0166), self.rectY1 - offset, text=str(i), fill="white") #20
            elif i % 2 == 0:
                self.meterCanv.create_line(xAxis, self.rectY1 - offset, xAxis + lilTick, self.rectY1 - offset, fill='orange')
        print ("len of unitDisc:", len(self.unitsDisc))
        print ("self.y", self.y)
        textVertCenter = self.y - (len(self.unitsDisc) / 2)
        print ("textVertCenter:", textVertCenter)
        self.meterCanv.create_text(self.rectX0 - (self.rectX1 * .30) , self.y, text=self.unitsDisc, fill='orange', angle=90, font=('Times', str(int(self.canvSize / 20)), 'bold'))

        
        
        self.meterCanv.pack(side = LEFT)
        self.meterFrame.pack(side=LEFT)
        
        #
        
    def UpdateLevel(self, percent):
        triIndicatorPixelDist = self.canvSize * .0167 #10
        if percent > 100: 
            percent = 100
        
        self.meterLevel = self.meterPixels * round((percent / 100), 2)
        self.meterCanv.coords(self.meterIndication, self.rectX0, self.rectY1 - self.meterLevel, self.rectX1, self.rectY1)
        
        
        self.meterCanv.coords(self.rTriIndicator, self.rectX1, self.rectY1 - self.meterLevel,  self.rectX1 + triIndicatorPixelDist,(self.rectY1 - self.meterLevel) + triIndicatorPixelDist,  
        self.rectX1 + triIndicatorPixelDist,(self.rectY1 - self.meterLevel) - triIndicatorPixelDist)
        
        self.meterCanv.coords(self.lTriIndicator, self.rectX0, self.rectY1 - self.meterLevel,  self.rectX0 - triIndicatorPixelDist,(self.rectY1 - self.meterLevel) + triIndicatorPixelDist,  
        self.rectX0 - triIndicatorPixelDist,(self.rectY1 - self.meterLevel) - triIndicatorPixelDist)

        self.meterCanv.itemconfigure(self.indicatorNum, text = str(round(float(percent),1)))
        self.meterCanv.update()
        if percent < self.yellow:
            self.meterCanv.itemconfigure(self.meterIndication, fill='green')
        elif percent >= self.yellow and percent < self.red:
            self.meterCanv.itemconfigure(self.meterIndication, fill='yellow')
        elif percent >= self.red:
            self.meterCanv.itemconfigure(self.meterIndication, fill='red')
    def TestMeter(self):
        for i in range(0, 201):
            self.UpdateLevel( i / 2)
            time.sleep(.02)
        self.UpdateLevel(0)
        time.sleep(.2)
        self.UpdateLevel(20)
        time.sleep(.2)
        self.UpdateLevel(40)
        time.sleep(.2)
        self.UpdateLevel(60)    
        time.sleep(.2)
        self.UpdateLevel(91)
        time.sleep(.2)
        self.UpdateLevel(33.25)
        time.sleep(.2)

class IndLights:
    def __init__(self, win, size, indicatorTitle, labelList, num_indicators):
        self.win = win
        self.num_divisions = num_indicators
        self.size=size
        self.indicatorObjs = [None] * self.num_divisions
        self.indicatorLabels = labelList
        print (self.indicatorObjs)
        x = size
        y = size / self.num_divisions #100
        self.indicatorFrame = LabelFrame (self.win, labelanchor='n',font=('Times',  round(size * .05), 'italic'), text=indicatorTitle, bd=2 )
        self.canvIndicator = Canvas(self.indicatorFrame, width=x, height=y)

        x = size / self.num_divisions
        circCent = x / 2
        circRadius = circCent / 2

        yUpper = (y / 2) + circRadius
        yLower = (y / 2) - circRadius

        print (x, circCent, circRadius)
        xpos = 0
        for i in range(self.num_divisions):
            self.indicatorObjs[i] = self.canvIndicator.create_oval(xpos + circCent - circRadius, yUpper, xpos + circCent + circRadius, yLower, fill='green')
            xpos += x

        self.canvIndicator.pack(side=LEFT) 
        self.indicatorFrame.pack(side=LEFT)


    