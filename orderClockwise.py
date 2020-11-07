import math

def orderClockwise(points): #jarvis
    if (len(points)<3) : return None # check actual polygon

    Hull = list()
    leftPoint = leftmostPoint(points)
    pointOnHull = leftPoint
    currPoint = 0

    while(True):
        Hull.append(points[pointOnHull])
        print(Hull)
        currPoint = (pointOnHull+1)%len(points)
        for i in range(len(points)):
            if (calculateOrientation(points[pointOnHull],points[i],points[currPoint]) == 2):
                currPoint = i
        pointOnHull = currPoint
        if (pointOnHull == leftPoint): #when we found all points
            break 
    Hull.reverse()
    return Hull

def calculateOrientation(p,q,r): # 0  if colinear, 1 if clockwise, 2 if counterclockwise
    orientation = ((q[1]-p[1]) * (r[0]-q[0])) - ((q[0]-p[0]) * (r[1]-q[1]))
    if(orientation == 0):
        return 0
    elif(orientation > 0):
        return 1
    else:
        return 2

def leftmostPoint(points):
    leftIndex = 0
    for i in range(1,len(points)): 
        if points[i][0] < points[leftIndex][0]: 
            leftIndex = i 
        elif points[i][0] == points[leftIndex][0]: 
            if points[i][1] > points[leftIndex][1]: 
                leftIndex = i 
    return leftIndex 


def testOrdering():
    points = [] 
    '''
    points.append((0, 3)) #with points inside
    points.append((2, 2)) 
    points.append((1, 1)) 
    points.append((2, 1)) 
    points.append((3, 0)) 
    points.append((0, 0)) 
    points.append((3, 3)) 
    '''

    points.append((1, 4))   # with all convex
    points.append((4, 6)) 
    points.append((4, 2)) 
    points.append((6, 4)) 

    print(points)
    answer = orderClockwise(points) 
    print(answer)
    print("done")

testOrdering()