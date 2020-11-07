from cmu_112_graphics import *

import orderClockwise
import centroid
import Fruit
import blade
#import slicing
import time

def appStarted(app):
    app.fruits = []
    p = [(-50,0),(0,50),(50,0),(0,-50)]
    f = Fruit.Fruit(p, (200,200), (0,0), "orange", True)
    app.fruits.append(f)
    app.sliced = False

    blade.init(app)
   
def mousePressed(app, event):
    bladeMouse(app, event)
    fruitTest(app)

def bladeMouse(app, event):
    if (not app.mousePress):
        app.mousePress = True
        #app.startpos = (event.x, event.y)
        #app.blade.append(app.startpos)
        app.t0 = time.time()

def fruitTest(app):
    if(not(app.sliced)):
        app.sliced = True
        print("oboi")
        p0,p1 = (220,100),(200,310)
        i = 0
        while i < len(app.fruits):
            f = app.fruits[i]
            (f1, f2) = f.slice(p0, p1, app.width,app.height)
            app.fruits.pop(i)
            app.fruits.insert(i,f2)
            app.fruits.insert(i,f1)
            i += 2

def keyPressed(app, event):
    pass

def mouseReleased(app, event):
    app.mousePress = False
    blade.resetBladeCount(app,event)


def mouseDragged(app,event):
    app.lastMouseX, app.lastMouseY = event.x, event.y
    if (app.mousePress):
        #app.t1 = time.time()
        #app.bladeCounter += 1
        x1,y1 = (event.x,event.y)
        blade.insertBlade(app,0,(x1,y1))


def timerFired(app):
    app.timerDelay = 20
    doStep(app)       
            
def doStep(app):
    blade.stepBlade(app)
    for f in app.fruits:
        f.move(0)

def redrawAll(app, canvas):
    drawFruits(app, canvas)
    blade.drawBlade(app,canvas)

def drawFruits(app, canvas):
    for f in app.fruits:
        (cx, cy) = f.pos
        coords = Fruit.localToGlobal(f.points, cx,cy)
        canvas.create_polygon(coords, fill="",width=4, outline="black")

runApp(width=1100, height=800)


    





