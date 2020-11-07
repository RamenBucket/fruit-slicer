from cmu_112_graphics import *

import orderClockwise
import centroid
import Fruit
import blade
#import slicing
import time

def appStarted(app):
    blade.init(app)
   
def mousePressed(app, event):
    if (not app.mousePress):
        app.mousePress = True
        #app.startpos = (event.x, event.y)
        #app.blade.append(app.startpos)
        app.t0 = time.time()
    print(event.x,event.y)

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

def redrawAll(app, canvas):
    blade.drawBlade(app,canvas)

runApp(width=1024, height=1024)


    





