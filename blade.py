from cmu_112_graphics import *
import time,random


def init(app):
    app.mousePress = False
    app.blade = list()
    
    #app.startpos = None
    app.t0,app.t1 = 0,0
    app.bladeTime = 0
    app.bladeMaxLength = 80 #pixel length of blade
    app.bladeMaxWidth = 5
    app.bladeColor = None



def resetBladeCount(app,event):
    app.bladeCounter = 0



def insertBlade(app,index,coord):
       app.blade.insert(index,coord) # just for the blade here
        
 
def stepBlade(app):
    app.bladeTime += 1
    fillExtraPoints(app.blade)# BROKEN
    lengthUsed = 0
    i = 0
    #tempBladeLength = min(app.bladeMaxLength, app.bladeCounter*10)
    while i < len(app.blade)-2 and lengthUsed < app.bladeMaxLength:
        (x0, y0), (x1,y1) = app.blade[i], app.blade[i+1]
        lengthUsed += dist(x0,y0,x1,y1)
        i += 1
    if lengthUsed >= app.bladeMaxLength:
        app.blade = app.blade[:i]
    
    removeDelay = int(max(100/(len(app.blade)+1)**2,1))
    #slower point removal for smaller blade size

    if(len(app.blade) > 0):
        if(app.mousePress and app.bladeTime%removeDelay == 0): #pop less
            app.blade.pop() 
        elif(not(app.mousePress)):#(app.bladeTime%3 == 0):# and not(app.mousePress)):
            app.blade.pop()
    #print(i)
    #while len(app.blade) > i:
        #app.blade.pop()

def fillExtraPoints(points):
    for i in range(len(points)-2):
        (x0,y0),(x1,y1) = points[i], points[i+1]
        if(dist(x0,y0,x1,y1) > 5):
            points.insert(i+1,((x1+x0)/2, (y1+y0)/2))

def dist(x0,y0,x1,y1):
    dx = (x0-x1)**2
    dy = (y0-y1)**2
    return (dx+dy)**0.5

def sizingBlade(app):
    part1 = 7
    part2 = 15
    for i in range(part2):
        app.bladeSize.append(i*10/part2)
    for i in range(0,part1):
        app.bladeSize.append(10-i*10/part1)

def rgbString(r, g, b):
    # Don't worry about the :02x part, but for the curious,
    # it says to use hex (base 16) with two digits.
    return f'#{r:02x}{g:02x}{b:02x}'


def drawBlade(app,canvas):
    split = 0.3
    splitIndex = int(len(app.blade)*split)
    maxSize = app.bladeMaxWidth
    dSizeUp, dSizeDown = 0, 0

    #initialize blade width constants
    try:
        dSizeUp = maxSize/splitIndex
        dSizeDown = maxSize/(len(app.blade)-splitIndex)
    except:
        pass

    for i in range(len(app.blade)-1):
        x,y = app.blade[i]
        x1,y1 = app.blade[i+1]
        s = 0
        if(i < splitIndex):
            s = i*dSizeUp
        else:
            s = maxSize-(i-splitIndex)*dSizeDown
        #s = 5#app.bladeSize[i%len(app.bladeSize)]
        canvas.create_oval(x-s,y-s,x+s,y+s,
        fill = "black",outline = '')
        canvas.create_line(x,y,x1,y1, width=2*s, fill = app.bladeColor)


