from cmu_112_graphics import *
from orderClockwise import orderClockwise
from clipping import clip
from Fruit import Fruit
import copy

def appStarted(app):
    app.polygonList = [(50,50),(app.width-50,50),
                       (app.width-50,app.height-50),(50,app.height-50)]
    # fruit
    app.fruitList = []
    p=app.polygonList
    testfruit = Fruit(p, (app.width/2,app.height/2), (0,0), "orange", True)
    app.fruitList.append(testfruit)

    app.sliceTopPolygon = [(0,75),(500,75),(500,500),(0,500)]
    app.sliceBottomPolygon = [(0,75),(500,75),(500,500),(0,500)]
    app.slice=[None,None]

def mousePressed(app, event):
    
    start = (event.x, event.y)
    app.slice[0] = start

def keyPressed(app, event):
    if event.key == 'q':
        appStarted(app)

def mouseReleased(app, event):
    end = (event.x, event.y)
    app.slice[1] = end
    app.sliceTopPolygon, app.sliceBottomPolygon = calculateSlicePolygons(app)
    if len(app.polygonList) > 2:
        print(f"polygon:{app.polygonList}")
        print(f"clip:{app.sliceBottomPolygon}")
        app.polygonList = clip(app.polygonList, app.sliceBottomPolygon)
        print(f"polygon after:{app.polygonList}")
        print()
    

def slicePolygon(app, fruit):
    app.sliceTopPolygon, app.sliceBottomPolygon = calculateSlicePolygons(app)
    
    if len(app.polygonList) > 2:
        print(f"polygon:{app.polygonList}")
        print(f"clip:{app.sliceBottomPolygon}")
        app.polygonList = clip(app.polygonList, app.sliceBottomPolygon)
        print(f"polygon after:{app.polygonList}")
        print()

    fruit1 = (clip(fruit.points, app.sliceTopPolygon), fruit.pos, fruit.vel, 
              fruit.fruitType, fruit.uncut)
    fruit2 = (clip(fruit.points, app.sliceBottomPolygon), fruit.pos, fruit.vel, 
              fruit.fruitType, fruit.uncut)

    app.fruitList.remove(fruit)    
    app.fruitList.append(fruit1)   
    app.fruitList.append(fruit2) 

def calculateSlicePolygons(app):
    (x0,y0) = app.slice[0]
    (x1,y1) = app.slice[1]
    dx = x1 - x0
    dy = y1 - y0

    topPolygonList = []
    bottomPolygonList = []

    if dx == 0:
        topPolygonList.append(extendInDirection(app,x0,y0,dx,dy,1))
        topPolygonList.append(extendInDirection(app,x0,y0,dx,dy,-1))
        bottomPolygonList.append(extendInDirection(app,x0,y0,dx,dy,1))
        bottomPolygonList.append(extendInDirection(app,x0,y0,dx,dy,-1))

        topPolygonList.append((0,0))
        topPolygonList.append((0,app.height))
        bottomPolygonList.append((app.width,0))
        bottomPolygonList.append((app.width,app.height))
    elif dy == 0:
        topPolygonList.append(extendInDirection(app,x0,y0,dx,dy,1))
        topPolygonList.append(extendInDirection(app,x0,y0,dx,dy,-1))
        bottomPolygonList.append(extendInDirection(app,x0,y0,dx,dy,1))
        bottomPolygonList.append(extendInDirection(app,x0,y0,dx,dy,-1))

        topPolygonList.append((0,0))
        topPolygonList.append((app.width,0))
        bottomPolygonList.append((0,app.height))
        bottomPolygonList.append((app.width,app.height))
    else:
        slope = (dy/dx)
        intercept = (y0) - (slope*x0)
        topPolygonList.extend(getIntercepts(app,slope,intercept))
        bottomPolygonList.extend(getIntercepts(app,slope,intercept))

        
        for xEnd,yEnd in [(0,0),(app.width,0),
                          (app.width,app.height),
                          (0,app.height)]:
            # check if the point is above line
            if yEnd>slope*xEnd+intercept:
                bottomPolygonList.append((xEnd,yEnd))
            else:
                topPolygonList.append((xEnd,yEnd))
    
    return orderClockwise(topPolygonList), orderClockwise(bottomPolygonList)

def extendInDirection(app,x,y,dx,dy,direction):
    while (x<=app.width and y<=app.height and x>=0 and y>=0):
        x+=dx*direction
        y+=dy*direction
    return (x,y)

def getIntercepts(app,slope,intercept):
    x0=0
    y0=0
    x1=app.width
    y1=app.height

    pt1 = (x0, slope*x0+intercept)
    pt2 = ((y0-intercept)/slope , y0)
    pt3 = (x1, slope*x1+intercept)
    pt4 = ((y1-intercept)/slope , y1)

    result = []
    for x,y in [pt1,pt2,pt3,pt4]:
        if x>=0 and y>=0 and x<=app.width and y<=app.height:
            result.append((x,y))
    return result

def redrawAll(app, canvas):
    """ sliceTop = []
    for x,y in app.sliceTopPolygon:
        sliceTop.append(x)
        sliceTop.append(y)
    canvas.create_polygon(sliceTop,fill='blue')

    sliceBottom = []
    for x,y in app.sliceBottomPolygon:
        sliceBottom.append(x)
        sliceBottom.append(y)
    canvas.create_polygon(sliceBottom,fill='red') """

    """ for fruit in app.fruitList:
        drawList = []
        for x,y in fruit.points:
            drawList.append(x)
            drawList.append(y)

        if len(drawList)>=6:
            canvas.create_polygon(drawList, fill = 'orange') """

    
    polygonDrawList = []
    for x,y in app.polygonList:
        polygonDrawList.append(x)
        polygonDrawList.append(y)

    if len(polygonDrawList)>5:
        canvas.create_polygon(polygonDrawList)

runApp(width=512, height=512)