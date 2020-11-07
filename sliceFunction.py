from orderClockwise import orderClockwise
from clipping import clip

def slicePoly(polyList, mousePoint1, mousePoint2, w, h):
    topPoly, bottomPoly = calculateSlicePolygons(mousePoint1, 
                                                 mousePoint2, w, h)
    poly1 = clip(polyList, topPoly)
    poly2 = clip(polyList, topPoly)
    return poly1, poly2

def calculateSlicePolygons(mousePoint1, mousePoint2, w, h):
    (x0,y0) = mousePoint1
    (x1,y1) = mousePoint2
    dx = x1 - x0
    dy = y1 - y0

    topPolygonList = []
    bottomPolygonList = []

    if dx == 0:
        topPolygonList.append(extendInDirection(x0,y0,dx,dy,1,w,h))
        topPolygonList.append(extendInDirection(x0,y0,dx,dy,-1,w,h))
        bottomPolygonList.append(extendInDirection(x0,y0,dx,dy,1,w,h))
        bottomPolygonList.append(extendInDirection(x0,y0,dx,dy,-1,w,h))

        topPolygonList.append((0,0))
        topPolygonList.append((0,h))
        bottomPolygonList.append((w,0))
        bottomPolygonList.append((w,h))
    elif dy == 0:
        topPolygonList.append(extendInDirection(x0,y0,dx,dy,1,w,h))
        topPolygonList.append(extendInDirection(x0,y0,dx,dy,-1,w,h))
        bottomPolygonList.append(extendInDirection(x0,y0,dx,dy,1,w,h))
        bottomPolygonList.append(extendInDirection(x0,y0,dx,dy,-1,w,h))

        topPolygonList.append((0,0))
        topPolygonList.append((w,0))
        bottomPolygonList.append((0,h))
        bottomPolygonList.append((w,h))
    else:
        slope = (dy/dx)
        intercept = (y0) - (slope*x0)
        topPolygonList.extend(getIntercepts(slope,intercept,w,h))
        bottomPolygonList.extend(getIntercepts(slope,intercept,w,h))
        
        for xEnd,yEnd in [(0,0),(w,0),
                          (w,h),
                          (0,h)]:
            # check if the point is above line
            if yEnd>slope*xEnd+intercept:
                bottomPolygonList.append((xEnd,yEnd))
            else:
                topPolygonList.append((xEnd,yEnd))
    
    return orderClockwise(topPolygonList), orderClockwise(bottomPolygonList)

def extendInDirection(x,y,dx,dy,direction,width,height):
    while (x<=width and y<=height and x>=0 and y>=0):
        x+=dx*direction
        y+=dy*direction
    return (x,y)

def getIntercepts(slope,intercept,width,height):
    x0=0
    y0=0
    x1=width
    y1=height

    pt1 = (x0, slope*x0+intercept)
    pt2 = ((y0-intercept)/slope , y0)
    pt3 = (x1, slope*x1+intercept)
    pt4 = ((y1-intercept)/slope , y1)

    result = []
    for x,y in [pt1,pt2,pt3,pt4]:
        if x>=0 and y>=0 and x<=width and y<=height:
            result.append((x,y))
    return result