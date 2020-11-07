def slicePoly()

def calculateSlicePolygons(mousePoint1, mousePoint2, w, h):
    (x0,y0) = mousePoint1
    (x1,y1) = mousePoint2
    dx = x1 - x0
    dy = y1 - y0

    topPolygonList = []
    bottomPolygonList = []

    if dx == 0:
        topPolygonList.append(extendInDirection(x0,y0,dx,dy,1))
        topPolygonList.append(extendInDirection(x0,y0,dx,dy,-1))
        bottomPolygonList.append(extendInDirection(x0,y0,dx,dy,1))
        bottomPolygonList.append(extendInDirection(x0,y0,dx,dy,-1))

        topPolygonList.append((0,0))
        topPolygonList.append((0,h))
        bottomPolygonList.append((w,0))
        bottomPolygonList.append((w,h))
    elif dy == 0:
        topPolygonList.append(extendInDirection(x0,y0,dx,dy,1))
        topPolygonList.append(extendInDirection(x0,y0,dx,dy,-1))
        bottomPolygonList.append(extendInDirection(x0,y0,dx,dy,1))
        bottomPolygonList.append(extendInDirection(x0,y0,dx,dy,-1))

        topPolygonList.append((0,0))
        topPolygonList.append((w,0))
        bottomPolygonList.append((0,h))
        bottomPolygonList.append((w,h))
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
    while (x<=app.height and y<=app.width and x>=0 and y>=0):
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