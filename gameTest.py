
from cmu_112_graphics import *
import orderClockwise
import centroid
import Fruit

def appStarted(app):
    app.fruits = []
    p = [(-50,0),(0,50),(50,0),(0,-50)]
    f = Fruit.Fruit(p, (200,200), (0,0), "orange", True)
    app.fruits.append(f)
    app.sliced = False

def mousePressed(app, event):
    if(not(app.sliced)):
        app.sliced = True
        print("oboi")
        p0,p1 = (50,200),(300,250)
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
    pass

def mouseDragged(app,event):
    pass

def timerFired(app):
    app.timerDelay = 20
    doStep(app)       
            

def doStep(app):
    for f in app.fruits:
        f.move(0)

def redrawAll(app, canvas):
    drawFruits(app, canvas)
    canvas.create_line(50,200,300,250)

def drawFruits(app, canvas):
    for f in app.fruits:
        (cx, cy) = f.pos
        coords = Fruit.localToGlobal(f.points, cx,cy)
        canvas.create_polygon(coords, fill="",width=4, outline="black")



runApp(width=512, height=512)


    





