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
        self.messageFrame.pack()    
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
        print ("canVsise:", self.canvSize)
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
        self.gaugeFrame = LabelFrame(self.win, labelanchor='n',font=('Times', 20, 'italic'), text=gaugeTitle, bd=2 )
        self.guageCanv = Canvas(self.gaugeFrame, height=self.canvY, width=self.canvX, bd=5, bg="black")
        self.messageLogger = StringVar()
        self.messageList = []
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
        self.displayText = self.guageCanv.create_text(self.x, self.y * 1.7, text=self.gaugeTextStr, fill="white", justify=CENTER)
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
class vertMeter1:
    def __init__(self, win, canvSize):
        self.win = win
        self.canvSize = canvSize
        self.canvX = self.canvSize
        self.canvY = self.canvSize
        self.x = self.canvX / 2
        self.y = self.canvY /2
        self.centerxy = self.x, self.y
        print ("canVsise:", self.canvSize)

        