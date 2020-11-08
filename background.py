from cmu_112_graphics import *

def drawBackdrop(app, canvas): 
    rings = 5
    cx, cy = app.width/2, app.height/2
    xUnit = cx/rings
    yUnit = cy/rings
    
    for i in range(rings*2,int(rings/2),-1):
        g = getShade(i,rings)
        c = rgbString(g,g,g)
        canvas.create_oval(cx-xUnit*i,cy-yUnit*i,cx+xUnit*i,cy+yUnit*i,fill=c,outline = "")

def rgbString(r, g, b):
    # Don't worry about the :02x part, but for the curious,
    # it says to use hex (base 16) with two digits.
    return f'#{r:02x}{g:02x}{b:02x}'

def getShade(n,rings):
    return int(100*(rings*2/n)+155)

def redrawAll(app, canvas):
    drawBackdrop(app, canvas)

runApp(width=500, height=300)