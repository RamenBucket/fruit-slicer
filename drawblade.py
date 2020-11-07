from cmu_112_graphics import *
import time,random
from playsound import playsound


Sf1 = "CutAir.wav"



def appStarted(app):
    app.mousePress = False
    app.blade = list()
    app.startpos = None
    app.t0,app.t1 = 0,0
    app.bladeSize = list()
    app.color = [0,0,0]
    sizingBlade(app)
    app.bladeColor = None

def mousePressed(app, event):
    if (not app.mousePress):
        app.startpos = (event.x, event.y)
        app.blade.append(app.startpos)
        app.mousePress = True
        app.t0 = time.time()
        for i in range(3):
            app.color[i] = random.randint(0,255)
        app.bladeColor = rgbString(app.color[0],app.color[1],app.color[2])

def mouseReleased(app, event):
    app.mousePress = False
    #playsound(Sf1)

def mouseDragged(app,event):
    if (app.mousePress):
        app.t1 = time.time()
        x1,y1 = (event.x,event.y)
        x0,y0 = app.startpos
        if (dist(x0,y0,x1,y1) >= app.width/4):
            app.blade.pop(0)
        if (app.t1-app.t0 <= 5):
            app.blade.append((x1,y1))
        


def timerFired(app):
    doStep(app)       
            
def doStep(app):
    if (not app.mousePress) and (app.blade != []):
        app.startpos = app.blade[0]
        app.blade.pop(0)
        if (len(app.blade) > 2):
            app.blade.pop(1)

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

def redrawAll(app, canvas):
    for i in range(len(app.blade)):
        x,y = app.blade[i]
        s = app.bladeSize[i%len(app.bladeSize)]
        canvas.create_oval(x-s,y-s,x+s,y+s,
        fill = app.bladeColor,outline = None)

runApp(width=512, height=512)