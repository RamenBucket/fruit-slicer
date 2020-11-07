from cmu_112_graphics import *

def appStarted(app):
    app.polygonList = [(50,50),(100,50),(100,100),(50,100)]
    app.sliceTopPolygon = [(0,75),(500,75),(500,500),(0,500)]
    app.sliceBottomPolygon = [(0,75),(500,75),(500,500),(0,500)]
    app.slice=[None,None]

def mousePressed(app, event):
    
    start = (event.x, event.y)
    app.slice[0] = start

def mouseReleased(app, event):
    end = (event.x, event.y)
    app.slice[1] = end
    app.sliceTopPolygon = calculateTopPolygon(app)
    app.sliceBottomPolygon = calculateBottomPolygon(app)
    print (app.sliceBottomPolygon)

def calculateTopPolygon(app):
    (x0,y0) = app.slice[0]
    (x1,y1) = app.slice[1]
    dx = x1 - x0
    dy = y1 - y0

    topPolygonList = []

    if dx == 0:
        topPolygonList.append((0,0))
        topPolygonList.append((0,app.height))
        topPolygonList.append(extendPositive(app,x0,y0,dx,dy))
        topPolygonList.append(extendNegative(app,x0,y0,dx,dy))
        return topPolygonList
    elif dy == 0:
        topPolygonList.append((0,0))
        topPolygonList.append((app.width,0))
        topPolygonList.append(extendPositive(app,x0,y0,dx,dy))
        topPolygonList.append(extendNegative(app,x0,y0,dx,dy))
        return topPolygonList
    else:
        topPolygonList.append(extendPositive(app,x0,y0,dx,dy))
        topPolygonList.append(extendNegative(app,x0,y0,dx,dy))
        slope = (dy/dx)
        intercept = (y0) - (slope*x0)
        for xEnd,yEnd in [(0,0),(app.width,0),(app.width,app.height),
                          (0,app.height)]:
            # check if the point is above line
            if yEnd<slope*xEnd+intercept:
                topPolygonList.append((xEnd,yEnd))
        return topPolygonList

def calculateBottomPolygon(app):
    (x0,y0) = app.slice[0]
    (x1,y1) = app.slice[1]
    dx = x1 - x0
    dy = y1 - y0

    bottomPolygonList = []

    if dx == 0:
        bottomPolygonList.append((app.width,0))
        bottomPolygonList.append((app.width,app.height))
        bottomPolygonList.append(extendPositive(app,x0,y0,dx,dy))
        bottomPolygonList.append(extendNegative(app,x0,y0,dx,dy))
        return bottomPolygonList
    elif dy == 0:
        bottomPolygonList.append((0,app.height))
        bottomPolygonList.append((app.width,app.height))
        bottomPolygonList.append(extendPositive(app,x0,y0,dx,dy))
        bottomPolygonList.append(extendNegative(app,x0,y0,dx,dy))
        return bottomPolygonList
    else:
        bottomPolygonList.append(extendPositive(app,x0,y0,dx,dy))
        bottomPolygonList.append(extendNegative(app,x0,y0,dx,dy))
        slope = (dy/dx)
        intercept = (y0) - (slope*x0)
        for xEnd,yEnd in [(0,0),(app.width,0),(app.width,app.height),
                          (0,app.height)]:
            # check if the point is above line
            if yEnd>slope*xEnd+intercept:
                bottomPolygonList.append((xEnd,yEnd))
        return bottomPolygonList

def extendPositive(app,x,y,dx,dy):
    while (x<=app.height and y<=app.width and x>=0 and y>=0):
        x+=dx
        y+=dy
    return (x,y)

def extendNegative(app,x,y,dx,dy):
    while (x<=app.height and y<=app.width and x>=0 and y>=0):
        x-=dx
        y-=dy
    return (x,y)

def redrawAll(app, canvas):
    sliceTop = []
    for x,y in app.sliceTopPolygon:
        sliceTop.append(x)
        sliceTop.append(y)
    canvas.create_polygon(sliceTop,fill='blue')

    sliceBottom = []
    for x,y in app.sliceBottomPolygon:
        sliceBottom.append(x)
        sliceBottom.append(y)
    canvas.create_polygon(sliceBottom,fill='red')

    polygonDrawList = []
    for x,y in app.polygonList:
        polygonDrawList.append(x)
        polygonDrawList.append(y)
    canvas.create_polygon(polygonDrawList)

# from http://rosettacode.org/wiki/Sutherland-Hodgman_polygon_clipping#Python
def clip(subjectPolygon, clipPolygon):
    def inside(p):
        return(cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])

    def computeIntersection():
        dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ]
        dp = [ s[0] - e[0], s[1] - e[1] ]
        n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
        n2 = s[0] * e[1] - s[1] * e[0] 
        n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
        return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]
 
    outputList = subjectPolygon
    cp1 = clipPolygon[-1]
 
    for clipVertex in clipPolygon:
        cp2 = clipVertex
        inputList = outputList
        outputList = []
        s = inputList[-1]
 
        for subjectVertex in inputList:
            e = subjectVertex
            if inside(e):
                if not inside(s):
                    outputList.append(computeIntersection())
                outputList.append(e)
            elif inside(s):
                outputList.append(computeIntersection())
            s = e
        cp1 = cp2
    return(outputList)

runApp(width=512, height=512)