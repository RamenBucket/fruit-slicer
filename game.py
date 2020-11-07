from cmu_112_graphics import *
#from shapely.geometry import Point
#from shapely.geometry.polygon import Polygon

import orderClockwise
import centroid
import Fruit
import blade
import random
#import slicing
import time


#point = Point(0.5, 0.5)
#polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
#print(polygon.contains(point))

fruitOutlines = [
    [(-50,0),(-35,35),(0,50),(35,35),(50,0),(35,-35),(0,-50),(-35,-35)],
    [(-50,0),(-35,35),(0,50),(35,35),(50,0),(35,-35),(0,-50),(-35,-35)],
    [(-50,0),(-35,35),(0,50),(35,35),(50,0),(35,-35),(0,-50),(-35,-35)],
    [(-50,0),(-35,35),(0,50),(35,35),(50,0),(35,-35),(0,-50),(-35,-35)],
    [(-50,0),(-35,35),(0,50),(35,35),(50,0),(35,-35),(0,-50),(-35,-35)]
]

fruitTypes = [
    "orange",
    "lemon",
    "lime",
    "strawberry"
]

def getFruit():
    i = random.randint(0,3)
    return (fruitTypes[i],fruitOutlines[i])

def appStarted(app):
    app.fruits = []
    #p = [(-50,0),(-35,35),(0,50),(35,35),(50,0),(35,-35),(0,-50),(-35,-35)]
    (f, outline) = getFruit()
    f0 = Fruit.Fruit(outline, (200,200), (0,0), f, True)
    #f1 = Fruit.Fruit(p, (300,500), (0,0), "orange", True)
    #f2 = Fruit.Fruit(p, (600,700), (0,0), "orange", True)
    app.fruits.append(f0)
    #app.fruits.extend([f0,f1,f2])
    app.sliced = False

    blade.init(app)

    #TEMPORARY!!!
    app.slice=[None,None]

def mousePressed(app, event):
    bladeMouse(app, event)
    #fruitTest(app)

    #TEMPORARY
    start = (event.x, event.y)
    app.slice[0] = start

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
            
            if(sliceFunction.sliceIntersectsPolygon(f.points,p0,p1)):
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

    #TEMPORARY
    print("bruh")
    end = (event.x, event.y)
    app.slice[1] = end
    p0,p1 = app.slice[0], app.slice[1]
    i = 0
    print("bruh")
    while i < len(app.fruits):
        f = app.fruits[i]
        (f1, f2) = f.slice(p0, p1, app.width,app.height)
        app.fruits.pop(i)
        app.fruits.insert(i,f2)
        app.fruits.insert(i,f1)
        i += 2

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
        c = "black"
        if(f.fruitType == "orange"):
            c = "orangered"
        elif(f.fruitType == "lemon"):
            c = "gold"
        elif(f.fruitType == "lime"):
            c = "forestgreen"
        elif(f.fruitType == "strawberry"):
            c = "firebrick"
        canvas.create_polygon(coords, fill=c,width=4, outline="black")
        canvas.create_oval(cx-5,cy-5,cx+5,cy+5,fill="red")

runApp(width=1100, height=800)


    





