from cmu_112_graphics import *

def drawBackdrop(app, canvas): 
    rings = 20
    cx, cy = app.width/2, app.height/2
    xUnit = cx/rings
    yUnit = cy/rings
    for i in range(1,rings*2):
        canvas.create_oval(cx-xUnit*i,cy-yUnit*i,cx+xUnit*i,cy+yUnit*i)

def getShade(n):
    return

def redrawAll(app, canvas):
    drawBackdrop(app, canvas)

runApp(width=500, height=300)