
from cmu_112_graphics import *
import orderClockwise
import centroid
import Fruit

def appStarted(app):
    app.fruits = []
    p = [(-50,0),(0,50),(50,0),(0,-50)]
    f = Fruit.Fruit(p, (200,500), (5,-20), "orange", True)
    app.fruits.append(f)

def mousePressed(app, event):
    pass

def keyPressed(app, event):
    pass

def mouseReleased(app, event):
    pass

def mouseDragged(app,event):
    pass

def timerFired(app):
    app.timerDelay = 20
    doStep(app)       
            

def doStep(app):
    for f in app.fruits:
        f.move(.5)

def redrawAll(app, canvas):
    drawFruits(app, canvas)

def drawFruits(app, canvas):
    for f in app.fruits:
        (cx, cy) = f.pos
        coords = Fruit.localToGlobal(f.points, cx,cy)
        canvas.create_polygon(coords)



runApp(width=512, height=512)


    





